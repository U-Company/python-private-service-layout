from clients import http


class Health(http.Method):
    url_ = "/health"
    m_type = "GET"
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
