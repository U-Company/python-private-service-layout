# {{ cookiecutter.service }}

## Installing

Before work with our storage, you need to install:

    sudo apt-get install docker.io make docker-compose
    
Make and docker is not required features. This tools is needed for more useful development. We recommend to use Anaconda
or another environment manager for safety system interpreter. You can download Anaconda 
[here](https://www.anaconda.com/). After installing Anaconda please create new environment:

    conda create --name abc-storage python=3.7
    conda activate
    
or, you can do this:

    make config
    conda activate
    
After that, you get project name's environment
    
## Configuration

If you want to configuration, you need configure docker and PyPi. More detail [here](https://github.com/U-Company/notes/tree/master/deployments)

### Prepare config for pip (Ubuntu)

Before publishing, you need to create file `~/.pypirc` like [this](deployments/.secrets/.pypirc). If you already have 
such file, you need to mix it like [this](deployments/.secrets/.pypirc_mixed).
    
### Installing package from private pypi repository

You must lay the config file [this](deployments/.secrets/pip.conf) into `~/.pip/`. If you already have 
such file, you need to mix it like [this](deployments/.secrets/pip.conf_mixed).
                   
### Configure docker

You must lay the config file [this](deployments/.secrets/daemon.json) into `~/.pip/`. If you already have 
such file, you need to mix it like [this](deployments/.secrets/daemon.json_mixed).
    
After that, you must restart docker (first time):

    sudo service docker restart

Now, login in docker registry with your login and password (first time):

    docker login http://{{ cookiecutter.docker_host }}:{{ cookiecutter.docker_port }} -u="<username>" -p="<password>"
    
## Publishing
    
If you want to publish package into registry, you need to do this:

    make build
    
Copy tag from console:

    VERSION=x.y.z TAG=<tag-from-make-build-log> make publish
    
## Clean

You can clean python package after building:

    make clean

## Starting 

Before starting please install all python package dependencies:

    make deps

We have three mode of starting:

- full subsystem
- development
- make

### docker-compose full

We use docker-compose for local development and starting you service and environment. If you want to start full 
subsystem, you need to do this:

    make run-full 
    
After that our service and environment is started. If you want to start our service the first time, docker container 
with service is built. Other container is pulled.
 
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

We have three commands:

    make test-integration
 
Before starting integration tests (above) you need to start environment:

    TEST=yes make run-env
    
Environment `TEST=yes` change env file to `deployments/tests/test.env`
      
Unit tests:

    make test-unit
      
All tests:

    make test

If you want to configure testing environment, you need change file `deployments/.envs/test.env`.
    
## Notice

We use makefile as interface for communicate our application with our systems by command line while development and
deployments
    
