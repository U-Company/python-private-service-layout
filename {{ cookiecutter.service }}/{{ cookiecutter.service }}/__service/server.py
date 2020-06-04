import threading

import fastapi
from starlette.middleware import cors

import info


class ThreadMutex:
    def __init__(self, message):
        """
        This is server mutex for handlers

        :param message: message of exception
        """
        self.__flag = False
        self.__mutex = threading.Lock()
        self.__message = message

    def check(self):
        if self.__flag:
            raise fastapi.HTTPException(409, detail=self.__message)

    def acquire(self):
        self.__mutex.acquire()
        if self.__flag:
            self.__flag = False
            self.__mutex.release()
            raise fastapi.HTTPException(409, detail=self.__message)
        self.__flag = True

    def release(self):
        self.__flag = False
        self.__mutex.release()


def check_mutex(l):
    """
    :param l: list of mutex for check
    :return:
    """
    for m in l:
        m.check()


class App:
    def __init__(self, env, allow_origins):
        self.app = fastapi.FastAPI(version=info.version, title=' '.join(info.name.split('_')))
        if env not in ['LOCAL', 'STAGE', 'ISOLATED']:
            self.app = fastapi.FastAPI(
                version=info.version,
                title=' '.join(info.name.split('_')),
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
