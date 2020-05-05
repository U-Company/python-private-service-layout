import fastapi
from starlette.middleware import cors

import version


class App:
    def __init__(self, env, allow_origins):
        self.app = fastapi.FastAPI(version=version.app_version, title=' '.join(version.app_name.split('_')))
        if env not in ['LOCAL', 'STAGE', 'ISOLATED']:
            self.app = fastapi.FastAPI(
                version=version.app_version,
                title=' '.join(version.app_name.split('_')),
                openapi_url=None,
                redoc_url=None,
                docs_url=None,
                swagger_ui_oauth2_redirect_url=None,
            )
        self.app.add_middleware(
            cors.CORSMiddleware,
            allow_origins=allow_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )
