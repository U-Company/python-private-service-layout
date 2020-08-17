# {{ cookiecutter.service }}

{{ cookiecutter.description }}

This service is built with a [python-private-service-layout](https://github.com/U-Company/python-private-service-layout)

## Building from source

Before work with our storage, you need to install:

    sudo apt-get install docker.io make docker-compose
    
Make and docker is not required features. This tools is needed for more useful development. We recommend to use Anaconda
or another environment manager for safety system interpreter. You can download Anaconda 
[here](https://www.anaconda.com/). After installing Anaconda please create new environment:

    conda create --name your-name python=3.7
    conda activate
    
or, you can do this:

    make config
    conda activate
    
After that, you get project name's environment

## Installing 

    PIP_CONFIG_FILE=/path/to/pip.conf pip install {{ cookiecutter.python_package }}
    
More about pip conf, you can read [here](https://github.com/U-Company/notes/tree/master/deployments).

*Notice*. Probably, if you want to install private package not as dependency, your case is not correctly.
    
## Configuration for publishing

If you want to publish images and packages, you need configure docker and PyPi. You can read short instruction below, or full instruction [here](deployments).

### Prepare config for setup.py (Ubuntu)

Before publishing, you need to create file `~/.pypirc`. Copy [this file](deployments/.secrets/.pypirc) to `~/.pypirc`. If you already have such file, you need to mix it like [this](deployments/.secrets/.pypirc_mixed). `.pypirc` is required for publishing python packages.
                   
### Configure docker

You must lay the config file [this](deployments/.secrets/daemon.json) into `/etc/docker/daemon.json`. If you already have 
such file, you need to mix it like [this](deployments/.secrets/daemon.json_mixed).
    
After that, you must restart docker (first time):

    sudo service docker restart

Now, login in docker registry with your login and password (first time):

    docker login {{cookiecutter.docker_registry}} -u="<username>" -p="<password>"
    
If you don't login, while pulling or pushing, make automatically ask you login.
    
## Dependencies

Install all package dependencies. We suppose that you have not more two registry: [public PyPi-registry](https://pypi.org/project/registry/) and maybe your private pypi-registry (it is optional). This command install from both or only public:

    make deps
    
We automatically create file to installing packages from repository (private or public). You can see this file [here](deployments/.secrets/pip_private.conf). If your repo is [common](https://pypi.org/), then set cookiecutter's default settings while init procedure. Othercase set your custom repositroy.
    
## Publishing
    
If you want to publish package into registry, you need to do this:

    make build
    
Copy tag from console:

    VERSION=x.y.z TAG=<tag-from-make-build-log> make publish
    
## Clean

You can clean python package after building and all temporary files:

    make clean

## Starting

Before starting please install all python package dependencies. Don't forget it:

    make deps

We have three mode of starting:

- full subsystem
- development
- make

### Running

We use docker-compose for local development and starting you service and environment. If you want to start full 
subsystem, you need to do this:

    make run-full 
    
After that our service and environment is started. If you want to start our service the first time, docker container with service is built. Other container is pulled.
 
If you want to start service not first time, maybe you need rebuilt service for apply last changes:

    make run-rebuild
    
### development

For development, you can use only environment:

    make run-env
    
After that, it starts all dependencies services. Now, you can run our service in your IDE for development.    

### make 

For fast start our service we use command:

    make run 

## Environment variables

Our service takes all environments variables from config: `deployments/.envs/local.env`. More about it you can read into
this file: `abc_storage/__service/config.py`. You can add new variables there and here: `deployments/.envs/local.env`. If you want to configure testing environment, you need change file `deployments/.envs/test.env`.

We separates variables by namespaces, therefore we set prefix before variable name. You can see in files, which we 
denote above. 

## Testing

We have three mode of testing:

- unit testing
- integration testing
- all: unit and integration testing

**NOTICE**: before start tests, set envs: `VAULT_ENV=LOCAL`, `VAULT_ENV_PATH=deployments/.envs/test.env`. `VAULT_ENV` says to Vault client takes envs from file. `VAULT_ENV_PATH` sets path to this file. If you use make file, you need to use, only `TEST=yes`. Makefile configure test environment automatically

We have three commands:

    make test-integration
 
Before starting integration tests (above) you need to start service with environment:

    TEST=yes make run-full
    
Environment `TEST=yes` change env file to `deployments/tests/test.env`
      
Unit tests:

    make test-unit
      
All tests:

    make test

If you want to configure testing environment, you need change file `deployments/.envs/test.env`.

## Swagger

If you want to use Swagger. You need to go 
    
## Notice

We use makefile as interface for communicate our application with our systems by command line while development and
deployments

## Common errors

If you have some errors, you can read
[Common errors]({{ cookiecutter.python_package }}/docs/errors.md) doc. Or you can communicate with Egor Urvanov by UrvanovCompany@yandex.ru or in telegram (@egor_urvanov)
