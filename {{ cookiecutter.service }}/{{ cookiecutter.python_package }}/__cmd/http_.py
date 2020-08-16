import uvicorn
from loguru import logger

from {{ cookiecutter.python_package }}.__service import server, config
import info

from prometheus_client import start_http_server



app = server.build_app(config.allow_origins)


path = '/health'
desc = 'Health checks health of service'
code = 204
@app.get(path, status_code=code, description=desc)
async def health():
    # TODO: is need to check auth?
    return


@app.get('/info')
async def info_method():
    # TODO: is need to check auth?
    return {"version": info.version, "name": info.name}


if __name__ == "__main__":
    start_http_server(config.prometheus_port)
    logger.info(f'App: {info.name}; Version: {info.version}')
    logger.info(f'Environment: {info.VAULT_ENV}')
    logger.info(f'prometheus port: {config.prometheus_port}')
    uvicorn.run(app.app, host='0.0.0.0', port=config.{{ cookiecutter.python_package }}_port)
