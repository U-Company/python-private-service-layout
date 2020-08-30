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
        self.__vars = {
            'handler': Variable(value=handler, deleted=False),
            'request': Variable(
                value={
                    'method': method,
                    'body': body,
                    'query_params': query_params,
                    'headers': headers,
                },
                deleted=False,
            ),
        }
        self.__cache = None

    def __enter__(self):
        self.__cache = copy.deepcopy(self.__vars)

    def __exit__(self, *args, **kwargs):
        self.__vars = self.__cache

    def __getitem__(self, key):
        v = self.__vars.get(key)
        if v is None:
            return None
        if v.deleted:
            return None
        return v.value

    def __setitem__(self, key, value):
        self.__vars[key] = Variable(deleted=False, value=value)

    def __delitem__(self, key):
        self.__vars[key] = Variable(deleted=True, value=self.__vars[key].value)

    def __del__(self):
        self.__vars = {}

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
    log_msg = {
        'handler': ctx['handler'],  # handler of method
        'request': ctx['request'],  # request of method
        'detail': msg,  # default message from class
        'comment': ctx['comment'],  # comment from developer (not message for response)
        'error_name': ctx['error_name'],  # class name of error
        'variables': ctx['variables'],  # state's variables
        'public_status_code': pcode,  # status code of response (HTTP status code)
        'internal_code': icode,  # status code of response (internal code)
    }
    logger.exception(log_msg)
    msg = f'Code: {icode}. {msg}'
    if not detail:
        msg = f'Code: {icode}'
    raise HTTPException(pcode, detail=msg)


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
            ctx_ = copy.deepcopy(ctx)
            self.__add_variables(ctx_, kwargs)
            ctx_['error_name'] = self.name
            _exception_validation(ctx=ctx_, msg=self.msg, detail=self.detail, pcode=self.pcode, icode=self.icode)

    def _validate(self, ctx: Context, **kwargs: typing.Dict):
        raise NotImplementedError()


class AssertorOK(AssertorValidation):
    """
    Check ok
    """
    def _validate(self, ctx: Context, **kwargs: typing.Dict):
        return not kwargs['ok']


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


def _exception_service(ctx: Context, *, pcode, icode, detail=True, msg=None):
    """
    Exception of validator execution

    :param ctx: context's execution of runtime
    :param pcode: default public code for response (HTTP response status code)
    :param icode: default private code for response (internal code)
    :param wcode: wanted code from service
    :param detail: is need returns message in exception
    :param msg: message for response
    :return:
    """
    log_msg = {
        'handler': ctx['handler'],  # handler of method
        'request': ctx['request'],  # request of method
        'service_request': ctx['service_request'],  # request to service
        'service_response': ctx['service_response'],  # response from service
        'service_code': ctx['service_code'],  # code from service
        'detail': msg,  # default message from class
        'comment': ctx['comment'],  # comment from developer (not message for response)
        'error_name': ctx['error_name'],  # class name of error
        'variables': ctx['variables'],  # state's variables
        'public_status_code': pcode,  # status code of response (HTTP status code)
        'wanted_code': ctx['wcode'],  # wanted code from service
        'internal_code': pcode,  # status code of response (internal code)
    }
    logger.exception(log_msg)
    msg = f'Code: {icode}. {msg}'
    if not detail:
        msg = f'Code: {icode}'
    raise HTTPException(pcode, detail=msg)


class AssertorCode:
    def __init__(self, icode, pcode=520, msg=None, detail=True, wcode=None):
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
            ctx_ = copy.deepcopy(ctx)
            ctx_['error_name'] = self.name
            ctx_['service_request'] = req
            ctx_['service_response'] = resp
            ctx_['service_code'] = code
            ctx_['wcode'] = self.wcode
            _exception_service(ctx=ctx_, msg=self.msg, detail=self.detail, pcode=self.pcode, icode=self.icode)

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

ExtraFields = AssertorOK(msg='Consists extra fields', pcode=422, icode=1, detail=True)
NotFoundFields = AssertorOK(msg='Not found some fields', pcode=422, icode=2, detail=True)
