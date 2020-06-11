# Template for python service

This repository is inspired by the repository of [layout-golang](https://github.com/golang-standards/project-layout). 
We build template for services of python. We use [FastAPI](https://github.com/tiangolo/fastapi), 
[uvicorn](https://www.uvicorn.org/), [docker](https://www.docker.com/) and docker-compose. For service creation we use 
[cookiecutter](https://github.com/cookiecutter/cookiecutter). This tool can init the service  

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
- completely to publishing package (custom or common pypi-registry)
- completely to publishing dockerfile (custom or common docker-registry/docker-hub)

## Usage

If you want to use our layout, you must use [cookiecutter](https://github.com/cookiecutter/cookiecutter). This is a very simple:

    pip install cookiecutter
    cookiecutter https://github.com/U-Company/python-service-layout.git
    
While installing, cookiecutter ask you with default some values: `-`. It means to ignore this parameter.
    
More about our approaches, you can read [here](https://github.com/U-Company/notes).

## Usability

Before usage, you need to install:

    sudo apt-get install make docker.io docker-compose

Create conda environment

    make config
    
Build python package and docker container

    make build

Publish python package and docker container

    VERSION=a.b.c TAG=<docker-container-tag> make publish
    
Clean source of python package after building and all temporary files

    make clean
    
Install all packages dependencies. We suppose that you have not more two registry: [public PyPi-registry](https://pypi.org/project/registry/) and maybe your private pypi-registry (optional). This command install from both or only public

    make deps
    
Run service in operation system
    
    make run

Run service in docker with environment services

    make run-full
    
Run service in docker with environment services

    make run-env

Rebuild docker container

    make run-rebuild

Run integration tests (you must run service and environments before running tests: `TEST=yes make run-full`):

    make test-integration
    
Run unit tests

    make test-unit
    
Run all tests

    make test

## [Project structure](https://github.com/U-Company/python-service-layout/tree/master/%7B%7B%20cookiecutter.service%20%7D%7D)

### [data/](https://github.com/U-Company/python-service-layout/tree/master/%7B%7B%20cookiecutter.service%20%7D%7D/data)

This folder must consists the data of service. We think to a large data file must dumps to any storage (
databases, file storage, git LFS, docs and other). Most part of data here is test's data.

### data/tests/

Files for tests

### data/docs/

Design and user documents.

### [deployments/](https://github.com/U-Company/python-service-layout/tree/master/%7B%7B%20cookiecutter.service%20%7D%7D/deployments)

IaaS, PaaS, system and container orchestration deployment configurations and templates (docker-compose, kubernetes/helm,
mesos, terraform, bosh).

You can deploy applications with different docker-compose files and different environment files. Our docker files are built by a make file, which uses as API interface for commutication building of any programm.

Type of docker files:

* **docker-compose.env.yml** -- environment for your application. For example, you have some databases and some servicese, but you want to run your application from source (for debugging, for instance). Then, you can runnig only this file.
* **docker-compose.full.yml** -- full application with environment

We have environment file into `./.envs` directory.

**Notice**: we configure compose with `network_mode: host` (in) therefore, our image links with localhost (no mapping ports, for example)

You can read about publishing packages [here](%7B%7B%20cookiecutter.service%20%7D%7D/deployments).

### data/logs/

Folder for logs files 

### service_name/ 

Library code that's ok to use by external applications (e.g., /service_name/mypubliclib). Other projects will
import these libraries expecting them to work, so think twice before you put something here :-) Note that catalogs with prefix `__` is a better way to ensure your private packages. In python this fact denotes private structures. The 
/service_name directory is still a good way to explicitly communicate that the code in that directory is safe 
for use by others.

This package's name has the same name as repo name (_ instead of -). This package (folder) publish to pypi-registry.
### [service_name/__cmd/](%7B%7B%20cookiecutter.service%20%7D%7D/__cmd/)
 
Main applications for this project.

The directory name for each application should match the name of the executable you want to have (e.g., /__cmd/cli.py).

For example, you have service (`http_.py`), CLI runner `cli.py`.

Don't put a lot of code in the application directory. If you think the code can be imported and used in other projects, 
then it should live in the `/service_name` directory. If the code is not reusable or if you don't want others 
to reuse it, put that code in the /internal directory. You'll be surprised what others will do, so be explicit about 
your intentions!

It's common to have a small main function that imports and invokes the code from the `/internal` and `/pkg` directories 
and nothing else.

See the `/__cmd` directory for examples.

We save `__cmd` into package therefore `__cmd` must be include into package to cli works. But cmd is not part of library.

### [service_name/tests/](%7B%7B%20cookiecutter.service%20%7D%7D/tests/)

This repo consists unit tests. Unit tests is used to test functions

### [service_name/generators/](%7B%7B%20cookiecutter.service%20%7D%7D/generators/)

Each service works with data. Therefore a good practice is build generators for data creation of each method. This generators is part of package for using in tests of other packages.

### [service_name/methods](%7B%7B%20cookiecutter.service%20%7D%7D/generators/)

Here we save methods for connect to our service. Example of usage, you can find [here](%7B%7B%20cookiecutter.service%20%7D%7D/%7B%7B%20cookiecutter.service%20%7D%7D/methods.py)

### service/
 
Implementation of service with unit tests for internal functions. We think that service is part of package, 
therefore we include this folder from package. But you must not import this module. We save service and cli here to add 
availability to them from console  

Internal functions, models of REST API, server, data transformers, utils etc.

### [tests/](%7B%7B%20cookiecutter.service%20%7D%7D/tests)

This directory consists only integration tests. In this directory cannot import files from another directories except 
package directory (python_service_layout). We tests our service as block box method. Therefore we cannot use common 
functions or scripts with tested sources.

### makefile

Makefile is given interface for control of application: dependencies, run, test, deploying.
  
### setup

This is template for configuration of package of setuptools package
  
### info

This file consists version and package's name.
