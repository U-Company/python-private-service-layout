import fastapi
from starlette.middleware import cors

import info


def build_logger(rotation_size, level):
    logger.remove()
    pid = os.getpid()
    logger.add(
        f'data/logs/fastapi-{pid}.log',
        rotation=rotation_size,
        enqueue=True,
        backtrace=True,
        level=level,
        format="{level}\t-\t{time}\t-\t%s\t-\t{message}" % pid,
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
    return app
