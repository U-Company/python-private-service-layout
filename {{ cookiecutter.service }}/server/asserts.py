import json

from fastapi import HTTPException
from loguru import logger

import copy
import dataclasses
import typing
import collections


Variable = collections.namedtuple('Variable', ['deleted', 'value'])


@dataclasses.dataclass
class Context:
    def __init__(
            self,
            *,
            handler: str,
            method: str,
            body: typing.Dict = None,
            query_params: typing.Dict = None,
            headers: typing.Dict = None,
    ):
        """

        :param handler: handler path
        :param method: POST, GET, HEAD, etc...
        :param body: pydantic.BaseModel
        :param query_params: typing.Dict
        :param headers: typing.Dict
        """
        self.vars = {
            'handler': Variable(value=handler, deleted=False),
            'method': Variable(value=method, deleted=False),
            'body': Variable(value=body, deleted=False),
            'query_params': Variable(value=query_params, deleted=False),
            'headers': Variable(value=headers, deleted=False),
        }
        self.__cache = []

    def __enter__(self):
        v = copy.deepcopy(self.vars)
        self.__cache.append(v)

    def __exit__(self, *args, **kwargs):
        self.vars = self.__cache.pop()

    def __getitem__(self, key):
        v = self.vars.get(key)
        if v is None:
            return None
        if v.deleted:
            return None
        return v.value

    def __str__(self):
        vars_ = {}
        for k, v in self.vars.items():
            vars_[k] = v.value
        return json.dumps(vars_, default=str)

    def get(self, key):
        return self[key]

    def __setitem__(self, key, value):
        self.vars[key] = Variable(deleted=False, value=value)

    def __delitem__(self, key):
        self.vars[key] = Variable(deleted=True, value=self.vars[key].value)

    def __del__(self):
        self.vars = {}

    def copy(self):
        return copy.deepcopy(self)


def _exception_validation(ctx: Context, *, pcode, icode, detail=True, msg=None):
    """
    Exception of validator execution

    :param ctx: context's execution of runtime
    :param pcode: default public code for response (HTTP response status code)
    :param icode: default private code for response (internal code)
    :param detail: is need returns message in exception
    :param msg: message for response
    :return:
    """
    with ctx:
        ctx['internal_code'] = icode
        ctx['public_status_code'] = pcode
        ctx['detail'] = msg
        ctx_str = str(ctx)
        logger.info(ctx_str)
        msg = f'Code: {icode}.' \
            f' {msg}'
        if not detail:
            msg = f'Code: {icode}'
        raise HTTPException(pcode, detail=msg)


def info(ctx: Context):
    """
    :param ctx: context's execution of runtime
    :return:
    """
    logger.info(ctx)


class AssertorValidation:
    def __init__(self, pcode, icode, msg=None, detail=True):
        """
        ServiceAssertor checks any conditions with context

        :param pcode: default public code for response (HTTP response status code)
        :param icode: default private code for response (internal code, internal system errors)
        :param msg: default message for response
        :param detail: show detail in HTTPException
        """
        self.name = type(self).__name__
        self.msg = msg
        self.pcode = pcode
        self.icode = icode
        self.detail = detail

    @staticmethod
    def __add_variables(ctx, kwargs):
        if ctx['variables'] is None:
            ctx['variables'] = {'_': kwargs}
            return
        ctx['variables']['_'] = kwargs

    def __call__(self, ctx: Context, **kwargs):
        """
        :param ctx: dict with some fields. You can see these fields into `def exception(ctx, status_code, msg=None)`
        :param kwargs: params for validate
        :return:
        """
        if self._validate(ctx, **kwargs):
            with ctx:
                self.__add_variables(ctx, kwargs)
                ctx['error_name'] = self.name
                _exception_validation(ctx=ctx, msg=self.msg, detail=self.detail, pcode=self.pcode, icode=self.icode)

    def _validate(self, ctx: Context, **kwargs: typing.Dict):
        raise NotImplementedError()


class AssertorOK(AssertorValidation):
    """
    Check ok
    """
    def _validate(self, ctx: Context, **kwargs: typing.Dict):
        return not kwargs['ok']


class AssertorFail(AssertorValidation):
    """
    Check ok
    """
    def _validate(self, ctx: Context, **kwargs: typing.Dict):
        return True


class AssertorListNotEmpty(AssertorValidation):
    """
    Check ok
    """
    def _validate(self, ctx: Context, **kwargs: typing.Dict):
        return not (len(kwargs['list_']) > 0)


class AssertorListEmpty(AssertorValidation):
    """
    Check ok
    """
    def _validate(self, ctx: Context, **kwargs: typing.Dict):
        return not (len(kwargs['list_']) == 0)


class AssertorListOnly(AssertorValidation):
    """
    Check ok
    """
    def _validate(self, ctx: Context, **kwargs: typing.Dict):
        return not (len(kwargs['list_']) <= 1)


class AssertorListDuplicate(AssertorValidation):
    """
    Check ok
    """
    def _validate(self, ctx: Context, **kwargs: typing.Dict):
        return not (len(kwargs['list_']) > 1)


class AssertorListSingle(AssertorValidation):
    """
    Check ok
    """
    def _validate(self, ctx: Context, **kwargs: typing.Dict):
        return not (len(kwargs['list_']) == 1)


class AssertorNotNone(AssertorValidation):
    """
    Check ok
    """
    def _validate(self, ctx: Context, **kwargs: typing.Dict):
        return not (kwargs['ok'] is not None)


class AssertorNone(AssertorValidation):
    """
    Check ok
    """
    def _validate(self, ctx: Context, **kwargs: typing.Dict):
        return not (kwargs['ok'] is None)


class AssertorAEqB(AssertorValidation):
    """
    Check a more b, where a is variables into context
    """
    def _validate(self, ctx: Context, **kwargs: typing.Dict):
        """
        :param ctx: context for validate
        :return:
        """
        return not (kwargs['a'] == kwargs['b'])


class AssertorALessB(AssertorValidation):
    """
    Check a more b, where a is variables into context
    """
    def _validate(self, ctx: Context, **kwargs: typing.Dict):
        """
        :param ctx: context for validate
        :return:
        """
        return not (kwargs['a'] < kwargs['b'])


class AssertorALessEqB(AssertorValidation):
    """
    Check a more b, where a is variables into context
    """
    def _validate(self, ctx: Context, **kwargs: typing.Dict):
        """
        :param ctx: context for validate
        :return:
        """
        return not (kwargs['a'] <= kwargs['b'])


class AssertorAMoreB(AssertorValidation):
    """
    Check a less b, where a is variables into context
    """
    def _validate(self, ctx: Context, **kwargs: typing.Dict):
        """
        :param ctx: context for validate
        :return:
        """
        return not (kwargs['a'] > kwargs['b'])


class AssertorAInB(AssertorValidation):
    """
    Check a less b, where a is variables into context
    """
    def _validate(self, ctx: Context, **kwargs: typing.Dict):
        """
        :param ctx: context for validate
        :return:
        """
        return not (kwargs['a'] in kwargs['b'])


class AssertorANotInB(AssertorValidation):
    """
    Check a less b, where a is variables into context
    """
    def _validate(self, ctx: Context, **kwargs: typing.Dict):
        """
        :param ctx: context for validate
        :return:
        """
        return not (kwargs['a'] not in kwargs['b'])


class AssertorAMoreEqB(AssertorValidation):
    """
    Check a less b, where a is variables into context
    """
    def _validate(self, ctx: Context, **kwargs: typing.Dict):
        """
        :param ctx: context for validate
        :return:
        """
        return not (kwargs['a'] >= kwargs['b'])


def _exception_service(ctx: Context, *, pcode, icode, detail=True, msg=None):
    """
    Exception of validator execution

    :param ctx: context's execution of runtime
    :param pcode: default public code for response (HTTP response status code)
    :param icode: default private code for response (internal code)
    :param detail: is need returns message in exception
    :param msg: message for response
    :return:
    """
    with ctx:
        ctx['internal_code'] = icode
        ctx['public_status_code'] = pcode
        ctx['detail'] = msg
        ctx_str = str(ctx)
        logger.info(ctx_str)
        msg = f'Code: {icode}. {msg}'
        if not detail:
            msg = f'Code: {icode}'
        raise HTTPException(pcode, detail=msg)


class AssertorCode:
    def __init__(self, *, icode, pcode=520, msg=None, detail=True, wcode=None):
        """
        ServiceAssertor checks any conditions with context

        :param pcode: default public code for response (HTTP response status code). Most probably, these codes are 5**
        :param icode: default private code for response (internal code, internal system errors)
        :param msg: default message for response
        :param detail: show detail in HTTPException
        :param wcode: wanted code from service. if wcode is not set, then pcode := wcode
        """
        self.name = type(self).__name__
        self.msg = msg
        self.pcode = pcode
        self.icode = icode
        self.detail = detail
        self.wcode = wcode
        if self.wcode is None:
            self.wcode = pcode

    def __call__(self, ctx: Context, *, req, resp, code):
        """
        :param ctx: dict with some fields. You can see these fields into `def exception(ctx, status_code, msg=None)`
        :param req: params for validate
        :param resp: params for validate
        :return:
        """
        if self._validate(ctx, req=req, resp=resp, code=code, wcode=self.wcode):
            with ctx:
                ctx['error_name'] = self.name
                ctx['service_request'] = req
                ctx['service_response'] = resp
                ctx['wanted_code'] = self.wcode
                ctx['service_code'] = code
                _exception_service(ctx=ctx, msg=self.msg, detail=self.detail, pcode=self.pcode, icode=self.icode)

    def _validate(self, ctx: Context, req, resp, code, wcode):
        """
        :param ctx: context for validate
        :param req: request of service
        :param resp: response of service
        :param wcode: wanted code of service
        :param code: got code of service
        """
        raise NotImplementedError()


class AssertorEqCode(AssertorCode):
    """
    Check a more b, where a is variables into context
    """
    def _validate(self, ctx: Context, req, resp, code, wcode):
        """
        :param ctx: context for validate
        :param req: request of service
        :param resp: response of service
        :param wcode: wanted code of service
        :param code: got code of service
        :return:
        """
        return not (wcode == code)


class AssertorNeqCode(AssertorCode):
    """
    Check a more b, where a is variables into context
    """
    def _validate(self, ctx: Context, req, resp, code, wcode):
        """
        :param ctx: context for validate
        :param req:
        :param resp:
        :param wcode: int
        :param code: int
        :return:
        """
        return not (wcode != code)


Expected200 = AssertorEqCode(msg='Unexpected code 200', wcode=200, icode=-1, detail=False)
Expected201 = AssertorEqCode(msg='Unexpected code 201', wcode=201, icode=-2, detail=False)
Expected202 = AssertorEqCode(msg='Unexpected code 202', wcode=202, icode=-3, detail=False)
Expected204 = AssertorEqCode(msg='Unexpected code 204', wcode=204, icode=-4, detail=False)
