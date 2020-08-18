import enum

from clients import http


api_key_name = 'access_token'


class Field(enum.Enum):
    Cookie = 'cookie'
    Header = 'header'
    QueryParam = 'query_param'


class CookieNotImplemented(Exception):
    pass


class APIKey(http.Method):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    def __init__(self, *, api_key: str, field: Field = Field.Header):
        http.Method.__init__(self)
        if field == Field.Cookie:
            raise CookieNotImplemented('cookie not implemented')
        elif field == Field.Header:
            self.headers[api_key_name] = api_key
        elif field == Field.QueryParam:
            self.params[api_key_name] = api_key


class Health(APIKey):
    url_ = "/health"
    m_type = "GET"
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
