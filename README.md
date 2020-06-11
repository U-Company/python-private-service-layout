# Template for private python service

This repository is inspired by the repository of [layout-golang](https://github.com/golang-standards/project-layout). 
We build template for services of python. We use [FastAPI](https://github.com/tiangolo/fastapi), 
[uvicorn](https://www.uvicorn.org/), [docker](https://www.docker.com/) and docker-compose. For service creation we use 
[cookiecutter](https://github.com/cookiecutter/cookiecutter). This tool can init your service. After that your service already work

## Service layout

![](docs/structure.png)

Upper you see struct of modules. Red is not public source. Green is public source. Package consists public and not public sources.

## Service

Our service has:

- [prometheus endpoint](https://github.com/prometheus/client_python)
- [vault-client](https://github.com/U-Company/vault-client)
- healthcheck
- [docker](https://www.docker.com/) and docker-compose for local development and deploying
- loguru for logging
- [FastAPI](https://github.com/tiangolo/fastapi) as service
- [uvicorn](https://www.uvicorn.org/) as asgi server
- console server
- console cli with [Fire](https://github.com/google/python-fire) framework for google
- templates for unit and integration tests
- interface for control your service via makefile
- completely to publishing package (private pypi-registry)
- completely to publishing dockerfile (private docker-registry)

## Usage

If you want to use our layout, you must use [cookiecutter](https://github.com/cookiecutter/cookiecutter). This is a very simple:

    pip install cookiecutter
    cookiecutter https://github.com/U-Company/python-private-service-layout.git
    
More about our approaches, you can read [here](https://github.com/U-Company/notes).

Tutorial service creating lays [here](https://github.com/U-Company/python-service-layout/blob/master/docs/tutorial.md).

Before usage service, you need to install:

    sudo apt-get install make docker.io docker-compose

You can read about all the principles that underlie this repository [here](https://github.com/U-Company/python-service-layout/blob/master/%7B%7B%20cookiecutter.service%20%7D%7D/docs/structure.md).
    
[Here](https://github.com/U-Company/python-service-layout/blob/master/%7B%7B%20cookiecutter.service%20%7D%7D/docs/commands.md) you cand find all available commands for communicate with service with a command line.

