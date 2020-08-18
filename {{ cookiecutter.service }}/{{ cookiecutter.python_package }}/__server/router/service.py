import fastapi
from fastapi import APIRouter
from fastapi.security import api_key
from starlette.responses import RedirectResponse

from {{ cookiecutter.python_package }}.__server import config
from {{ cookiecutter.python_package }}.__server.router import auth

router = APIRouter()

tag = 'service'

desc = 'This method set API key to cookie. We use get method for simple browser supporting'
handler = '/api-key'
summary = 'Create API token'
@router.get(handler, summary=summary, description=desc, tags=[tag])
async def create_token(api_key: api_key.APIKey = fastapi.Depends(auth.get_api_key)):
    response = RedirectResponse(url="/docs")
    response.set_cookie(
        config.api_key_name,
        value=api_key,
        domain=config.{{ cookiecutter.python_package }}_host,
        httponly=True,
        max_age=1800,
        expires=1800,
    )
    return response


desc = 'This method delete API key from cookie'
handler = '/api-key'
summary = 'Delete API token'
@router.delete(handler, summary=summary, description=desc, tags=[tag])
async def delete_token():
    response = RedirectResponse(url="/")
    response.delete_cookie(config.api_key_name, domain=config.{{ cookiecutter.python_package }}_host)
    return response


desc = 'This method check health of service'
handler = '/health'
summary = 'Health of service'
@router.get(handler, summary=summary, description=desc, status_code=204, tags=[tag])
async def health(api_key: api_key.APIKey = fastapi.Depends(auth.get_api_key)):
    return


desc = 'This method returns info about service. Version, service name and environment'
handler = '/info'
summary = 'Information about service'
@router.get(handler, summary=summary, description=desc, status_code=204, tags=[tag])
async def info(api_key: api_key.APIKey = fastapi.Depends(auth.get_api_key)):
    return {'version': info.version, 'name': info.name, 'environment': config.VAULT_ENV}
