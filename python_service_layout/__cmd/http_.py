import random

import uvicorn
from loguru import logger

from service.internal import server, config

from prometheus_client import start_http_server, Summary
import time


app = server.App(env=config.VAULT_ENV, allow_origins=config.allow_origins)

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)


@app.app.get('/health', status_code=204)
async def health():
    return


if __name__ == "__main__":
    start_http_server(config.prometheus_port)
    logger.info(f'prometheus port: {config.prometheus_port}')
    uvicorn.run(app.app, host='0.0.0.0', port=config.app_port)
