# Template for private python service

This repository is inspired by the repository of [layout-golang](https://github.com/golang-standards/project-layout). 
We build template for services of python. We use [FastAPI](https://github.com/tiangolo/fastapi), 
[uvicorn](https://www.uvicorn.org/), [docker](https://www.docker.com/) and docker-compose. For service creation we use 
[cookiecutter](https://github.com/cookiecutter/cookiecutter). This tool can init your service. After that your service already work

## Service layout

![](docs/structure.png)

Upper you see struct of modules. Red is not public source. Green is public source. Package consists public and not public sources.

You can read about all the principles that underlie this repository [here](%7B%7B%20cookiecutter.service%20%7D%7D/docs/structure.md).

## Service

Our service has:

- [prometheus endpoint](https://github.com/prometheus/client_python)
- [vault-client](https://github.com/U-Company/vault-client)
- healthcheck
- [docker](https://www.docker.com/) and docker-compose for local development and deploying
- isolated docker development
- loguru for logging
- autogeneration of README.md for your service
- swagger from FastAPI /docs
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

Tutorial service creating lays [here](docs/tutorial.md).

Before usage service, you need to install:

    sudo apt-get install make docker.io docker-compose
    
[Here]({{ cookiecutter.service }}/docs/commands.md) you cand find all available commands for communicate with service with a command line.

If you have some errors, you can read [FAQ](%7B%7B%20cookiecutter.service%20%7D%7D/docs/errors.md) doc. Or you can communicate with Egor Urvanov by UrvanovCompany@yandex.ru or in telegram (@egor_urvanov)

## Infrastructure

If you need a bit infrastructure, see our repo with [infrastructure](https://github.com/U-Company/infrastructure). This is very simple. You need to do only:

    docker-compose up
    
That is enough!

