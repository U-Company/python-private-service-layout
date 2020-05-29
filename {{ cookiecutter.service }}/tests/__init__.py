import os

from clients import http
from vault_client.client import VaultClient


environ = os.environ.get('VAULT_ENV', 'LOCAL')
client = VaultClient(environ=environ, env_file='deployments/.envs/local.env')

assert client.is_authenticated, 'Vault client not authenticated'
assert client.is_initialized, 'Vault client not initialized'
assert not client.is_sealed, 'Vault client sealed'

namespace = '{{ cookiecutter.service }}'
{{ cookiecutter.service }}_host = client.get(namespace, 'HOST')
{{ cookiecutter.service }}_port = client.get(namespace, 'PORT')
{{ cookiecutter.service }}_schema = client.get(namespace, 'SCHEMA')
{{ cookiecutter.service }}_token = client.get(namespace, 'BASE64_TOKEN')

{{ cookiecutter.service }}_backend_url = {{ cookiecutter.service }}_schema + '://' + {{ cookiecutter.service }}_host + ':' + {{ cookiecutter.service }}_port


def set_auth(m):
    if m.headers is None:
        m.headers = {}
    m.headers['Authorization'] = f'Basic '+{{ cookiecutter.service }}_backend_url+'_token'
    return m


def client():
    """
    client_storage creates individual client for each test. This is very famous for aiohttp event loop in tests
    :return:
    """
    return http.AsyncClient({{ cookiecutter.service }}_backend_url, mdws_nc=[set_auth])