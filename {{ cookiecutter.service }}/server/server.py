import fastapi
from starlette.middleware import cors

import info


def make_logger():
    logger.remove()
    pid = os.getpid()
    dt = datetime.datetime.now()
    logger.add(
        f'data/logs/fastapi-{dt}-{pid}.log',
        rotation='100 MB',
        enqueue=True,
        backtrace=True,
        level='INFO',
        format="{time} %s {level} {message}" % pid,
    )
    return logger.bind()


uvicorn_config.LOGGING_CONFIG['handlers'] = {
    'default': {
        'formatter': 'default',
        'class': 'logging.FileHandler',
        'filename': f'data/logs/urvicorn-error-{datetime.datetime.utcnow()}.log',
    },
    'access': {
        'formatter': 'access',
        'class': 'logging.FileHandler',
        'filename': f'data/logs/uvicorn-requests-{datetime.datetime.utcnow()}.log',
    },
}


def service_name():
    return ' '.join(info.name.split('_'))


def build_app(allow_origins):
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
    return app
