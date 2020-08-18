import uvicorn
from loguru import logger

from {{ cookiecutter.python_package }}.__server import server, config
from {{ cookiecutter.python_package }}.__server.router import service
import info

from prometheus_client import start_http_server


app = server.build_app(config.allow_origins)
app.include_router(service.router)


logger.info(f'app: {info.name}; version: {info.version}')
logger.info(f'environment: {config.VAULT_ENV}')
swagger_endpoint = f'{config.{{ cookiecutter.python_package }}_schema}://{config.{{ cookiecutter.python_package }}_host}:{config.{{ cookiecutter.python_package }}_port}/api-key?{config.api_key_name}={config.{{ cookiecutter.python_package }}_api_key}'
logger.info(f'swagger: {swagger_endpoint}')
if __name__ == "__main__":
    start_http_server(config.prometheus_port)
    logger.info(f'prometheus port: {config.prometheus_port}')
    uvicorn.run(app, host=config.{{ cookiecutter.python_package }}_host, port=config.{{ cookiecutter.python_package }}_port)
