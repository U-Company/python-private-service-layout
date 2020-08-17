import fastapi
from starlette.status import HTTP_403_FORBIDDEN

from {{ cookiecutter.python_package }}.__server import config


async def get_api_key(
    api_key_query: str = fastapi.Security(config.api_key_query),
    api_key_header: str = fastapi.Security(config.api_key_header),
    api_key_cookie: str = fastapi.Security(config.api_key_cookie),
):
    """
    get_api_key is middleware for check authorization of methods
    :param api_key_query: query param authorization
    :param api_key_header: header authorization
    :param api_key_cookie: cookie authorization
    :return:
    """
    if api_key_query == config.API_KEY:
        return api_key_query
    elif api_key_header == config.API_KEY:
        return api_key_header
    elif api_key_cookie == config.API_KEY:
        return api_key_cookie
    else:
        # TODO: здесь нужно добавить стандартный assertor с контекстами
        raise fastapi.HTTPException(status_code=HTTP_403_FORBIDDEN, detail='Could not validate credentials')
