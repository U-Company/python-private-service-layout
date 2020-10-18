import fastapi
import uvicorn
from loguru import logger
from fastapi.openapi import docs
from fastapi.openapi.models import APIKey
from fastapi.openapi.utils import get_openapi
from starlette.responses import JSONResponse
from prometheus_client import start_http_server

from server.router import service, auth
from server import server, config
import info


app = server.build_app(config.allow_origins)
app.include_router(service.router)


tag = 'documentation'

desc = 'This method returns openAPI json with service configuration'
handler = '/openapi.json'
summary = 'Open API'
@app.get(handler, summary=summary, description=desc, tags=[tag])
async def open_api_endpoint(api_key: APIKey = fastapi.Depends(auth.get_api_key)):
    open_api = get_openapi(title=server.service_name(), version=info.version, routes=app.routes)
    return JSONResponse(open_api)

desc = 'This method returns info about service. Version, service name and environment'
handler = '/docs'
summary = 'Service documentation'
@app.get(handler, summary=summary, description=desc, tags=[tag])
async def documentation(api_key: APIKey = fastapi.Depends(auth.get_api_key)):
    response = docs.get_swagger_ui_html(openapi_url='/openapi.json', title='docs')
    return response


logger.info('{"app": "%s", "version": "%s"}' % (info.name, info.version))
logger.info('{"environment": "%s"}' % (config.VAULT_ENV,))
swagger_endpoint = f'{config.grader_v2_student_back_schema}://{config.grader_v2_student_back_host}:' \
    f'{config.grader_v2_student_back_port}/api-key?{config.api_key_name}={config.grader_v2_student_back_api_key}'
if __name__ == "__main__":
    start_http_server(config.prometheus_port)
    logger.info('{"prometheus port": "%s"}' % config.prometheus_port)
    uvicorn.run(app, host=config.{{ cookiecutter.python_package }}_host, port=config.{{ cookiecutter.python_package }}_port)
