import os

from clients import http
from vault_client.client import VaultClient

import info


VAULT_ENV = os.environ.get('VAULT_ENV', 'LOCAL')
VAULT_ENV_FILE = os.environ.get('VAULT_ENV_FILE', 'deployments/.envs/test.env')
client = VaultClient(environ=VAULT_ENV, env_file=VAULT_ENV_FILE)

assert client.is_authenticated, 'Vault client not authenticated'
assert client.is_initialized, 'Vault client not initialized'
assert not client.is_sealed, 'Vault client sealed'

namespace = info.name.upper()
{{ cookiecutter.python_package }}_host = client.get(namespace, 'HOST')
{{ cookiecutter.python_package }}_port = client.get(namespace, 'PORT')
{{ cookiecutter.python_package }}_schema = client.get(namespace, 'SCHEMA')
{{ cookiecutter.python_package }}_token = client.get(namespace, 'BASE64_TOKEN')

{{ cookiecutter.python_package }}_backend_url = {{ cookiecutter.python_package }}_schema + '://' + {{ cookiecutter.python_package }}_host + ':' + {{ cookiecutter.python_package }}_port


def set_auth(m):
    if m.headers is None:
        m.headers = {}
    m.headers['Authorization'] = f'Basic '+{{ cookiecutter.python_package }}_token
    return m


def client():
    """
    client_storage creates individual client for each test. This is very famous for aiohttp event loop in tests
    :return:
    """
    return http.AsyncClient({{ cookiecutter.python_package }}_backend_url, mdws_nc=[set_auth])
