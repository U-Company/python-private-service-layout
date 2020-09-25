## [Project structure]({{ cookiecutter.python_package }}/docs/structure.md)

We provide a very simple interface for running your server (**after installation dependencies**):

    make run
    
Or, if you have some service dependencies, you can do this:

    make run-full

## Installation dependencies

You need to use: 

- docker
- docker-compose
- make
- Anaconda

Before work with service, you need to install:

    sudo apt-get install make docker.io make docker-compose
    
Make and docker is not required features. This tools is needed for more useful development. We recommend to use Anaconda
or another environment manager for safety system interpreter. You can download Anaconda 
[here](https://www.anaconda.com/). After installing Anaconda please create new environment:

    make config
    conda activate {{ cookiecutter.python_package }}
    
Now, you can install all python dependencies
    
## Project structure

### [data/]({{ cookiecutter.python_package }}/data)

This folder must consists the data of service. We think to a large data file must dumps to any storage (
databases, file storage, git LFS, docs and other). Most part of data here is test's data.

### data/tests/

Files for tests

### data/docs/

Design and user documents

### data/logs/

Folder for logs files 

### [deployments/]({{ cookiecutter.python_package }}/deployments)

IaaS, PaaS, system and container orchestration deployment configurations and templates (docker-compose, kubernetes/helm,
mesos, terraform, bosh).

You can deploy applications with different docker-compose files and different environment files. Our docker files are built by a make file, which uses as API interface for commutication building of any programm.

Type of docker files:

* **docker-compose.env.yml** -- environment for your application. For example, you have some databases and some servicese, but you want to run your application from source (for debugging, for instance). Then, you can runnig only this file.
* **docker-compose.full.yml** -- full application with environment

We have environment file into `./.envs` directory.

**Notice**: we configure compose with `network_mode: host` (in) therefore, our image links with localhost (no mapping ports, for example)

You can read about publishing packages [here]({{ cookiecutter.python_package }}/deployments).

### {{ cookiecutter.python_package }}/ 

Library code that's ok to use by external applications (e.g., /{{ cookiecutter.python_package }}/mypubliclib). Other projects will
import these libraries expecting them to work, so think twice before you put something here :-) 

We have only two type modules in python package of service:

- public API methods for service

### [{{ cookiecutter.python_package }}/methods.py]({{ cookiecutter.python_package }}/methods.py)

Here we save methods for connect to our service. Example of usage, you can find [here]({{ cookiecutter.python_package }}/methods.py)

### [server/tests](server/tests/)

This repo consists unit tests. Unit tests is used to test functions, not services

### [scripts/](scripts)

Service scripts are stored here. Default scripts:

- Getting variables from Vault or file (variable.py). This script it need for `make run` command

### [tests/](tests)

This directory consists only integration tests. In this directory cannot import files from another directories except 
package directory. We tests our service as block box method. Therefore we cannot use common 
functions or scripts with tested sources.

More details about testing, you can find [here](tests.md)

### makefile

Makefile is given interface for control of application: dependencies, run, test, deploying.
  
### setup

This is template for configuration of package of setuptools package
  
### info

This file consists version and package's name.
