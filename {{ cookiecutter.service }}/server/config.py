import os
import datetime

from fastapi import security
from vault_client.client import VaultClient
from uvicorn import config as uvicorn_config


VAULT_ENV = os.environ.get('VAULT_ENV', 'LOCAL')
VAULT_ENV_FILE = os.environ.get('VAULT_ENV_FILE', 'deployments/.envs/local.env')
vault_client = VaultClient(environ=VAULT_ENV, env_file=VAULT_ENV_FILE)

assert vault_client.is_authenticated, 'Vault client not authenticated'
assert vault_client.is_initialized, 'Vault client not initialized'
assert not vault_client.is_sealed, 'Vault client sealed'

api_key_name = 'access_token'

namespace = info.name.upper()
{{ cookiecutter.python_package }}_schema = vault_client.get(namespace, 'SCHEMA')
{{ cookiecutter.python_package }}_host = vault_client.get(namespace, 'HOST')
{{ cookiecutter.python_package }}_port = int(vault_client.get(namespace, 'PORT'))
{{ cookiecutter.python_package }}_api_key = vault_client.get(namespace, 'API_KEY')
{{ cookiecutter.python_package }}_log_rotation_size = vault_client.get(namespace, 'LOG_ROTATION_SIZE')
{{ cookiecutter.python_package }}_log_level = vault_client.get(namespace, 'LOG_LEVEL')
prometheus_port = int(vault_client.get(namespace, 'PROMETHEUS_PORT'))
allow_origins = vault_client.get(namespace, 'ALLOW_ORIGINS')
if VAULT_ENV == 'LOCAL' and allow_origins is None:
    allow_origins = ['*']


api_key_query = security.APIKeyQuery(name=api_key_name, auto_error=False)
api_key_header = security.APIKeyHeader(name=api_key_name, auto_error=False)
api_key_cookie = security.APIKeyCookie(name=api_key_name, auto_error=False)
