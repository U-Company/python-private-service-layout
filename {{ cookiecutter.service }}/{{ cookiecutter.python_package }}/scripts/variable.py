import os
import sys

from vault_client.client import VaultClient


variable = sys.argv[1]

VAULT_ENV = os.environ.get('VAULT_ENV', 'LOCAL')
VAULT_ENV_FILE = os.environ.get('VAULT_ENV_FILE', 'deployments/.envs/local.env')
vault_client = VaultClient(environ=VAULT_ENV, env_file=VAULT_ENV_FILE)

assert vault_client.is_authenticated, 'Vault client not authenticated'
assert vault_client.is_initialized, 'Vault client not initialized'
assert not vault_client.is_sealed, 'Vault client sealed'

namespace = {{ cookiecutter.python_package.upper() }}
print(vault_client.get(namespace, variable.upper()))
