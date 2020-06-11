## Commands

Create conda environment

    make config
    
Build python docker container. Package is built while publishing

    make build-image

Publish docker image. You can get docker container tag from console, after running `make build-image`

    VERSION=a.b.c TAG=<docker-container-tag> make publish-image

Publish python package

    make publish-package
    
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
