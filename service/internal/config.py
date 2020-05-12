import os
import sys

from loguru import logger
from vault_client.client import VaultClient

import info

VAULT_ENV = 'LOCAL'
environ = os.environ.get('VAULT_ENV', VAULT_ENV)
vault_client = VaultClient(environ=environ, env_file='deployments/.envs/local.env')

assert vault_client.is_authenticated, 'Vault client not authenticated'
assert vault_client.is_initialized, 'Vault client not initialized'
assert not vault_client.is_sealed, 'Vault client sealed'

namespace = info.name.upper()
app_port = int(vault_client.get(namespace, 'PORT'))
prometheus_port = int(vault_client.get(namespace, 'PROMETHEUS_PORT'))
allow_origins = vault_client.get(namespace, 'ALLOW_ORIGINS')
if VAULT_ENV == 'LOCAL' and allow_origins is None:
    allow_origins = ['*']


backtrace = False if VAULT_ENV == 'PROD' else True
diagnose = False if VAULT_ENV == 'PROD' else True
logger.add(sys.stdout, backtrace=backtrace, diagnose=diagnose)
