import uvicorn

from service.internal import server


env = 'LOCAL'
port = '8080'
app = server.App(env=env, allow_origins=['*'])


@app.app.get('/healthcheck', status_code=204)
async def healthcheck():
    return


if __name__ == "__main__":
    uvicorn.run(app.app, host='0.0.0.0', port=port)
