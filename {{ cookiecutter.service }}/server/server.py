import fastapi
from starlette.middleware import cors


from datetime import datetime

import info


def build_logger(rotation_size, level):
    logger.remove()
    logger.add(
        f'data/logs/{{ cookiecutter.python_service }}_service_{datetime.utcnow()}.log',
        rotation=rotation_size,
        enqueue=True,
        backtrace=True,
        level=level,
        format="{level}\t-\t{time}\t-\t{message}",
    )
    return logger.bind()


def service_name():
    return ' '.join(info.name.split('_'))


def build_app(allow_origins, rotation_size, level):
    app = fastapi.FastAPI(
        version=info.version, title=service_name(), docs_url=None, redoc_url=None, openapi_url=None,
    )
    app.add_middleware(
        cors.CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    build_logger(rotation_size, level)
    Instrumentator().instrument(app).expose(app)
    return app
