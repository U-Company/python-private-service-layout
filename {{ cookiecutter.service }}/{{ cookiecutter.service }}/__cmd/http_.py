import uvicorn
from loguru import logger

from {{ cookiecutter.service }}.__service import server, config

from prometheus_client import start_http_server


app = server.App(env=config.VAULT_ENV, allow_origins=config.allow_origins)


@app.app.get('/health', status_code=204)
async def health():
    # TODO: is need to check auth?
    return


if __name__ == "__main__":
    start_http_server(config.prometheus_port)
    logger.info(f'prometheus port: {config.prometheus_port}')
    uvicorn.run(app.app, host='0.0.0.0', port=config.{{ cookiecutter.service }}_port)
