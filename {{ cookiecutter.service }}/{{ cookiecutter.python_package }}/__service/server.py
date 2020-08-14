import threading

import fastapi
from starlette.middleware import cors

import info


class ThreadMutex:
    def __init__(self, message):
        """
        This is server mutex for handlers. This object can block event loop from another requests. Careful about 
        synchronization, if you use nginx

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


def build_app(allow_origins):
    app = fastapi.FastAPI(version=info.version, title=' '.join(info.name.split('_')))
    app.add_middleware(
        cors.CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
