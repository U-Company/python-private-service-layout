## [Project structure]({{ cookiecutter.python_package }}/docs/structure.md)

### [data/]({{ cookiecutter.python_package }}/data)

This folder must consists the data of service. We think to a large data file must dumps to any storage (
databases, file storage, git LFS, docs and other). Most part of data here is test's data.

### data/tests/

Files for tests

### data/docs/

Design and user documents.

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

### data/logs/

Folder for logs files 

### {{ cookiecutter.python_package }}/ 

Library code that's ok to use by external applications (e.g., /service_name/mypubliclib). Other projects will
import these libraries expecting them to work, so think twice before you put something here :-) Note that catalogs with prefix `__` is a better way to ensure your private packages. In python this fact denotes private structures. The 
/service_name directory is still a good way to explicitly communicate that the code in that directory is safe 
for use by others.

This package's name has the same name as repo name (_ instead of -). This package (folder) publish to pypi-registry.

### [{{ cookiecutter.python_package }}/tests]({{ cookiecutter.python_package }}/tests/)

This repo consists unit tests. Unit tests is used to test functions

### [{{ cookiecutter.python_package }}/generators]({{ cookiecutter.python_package }}/generators/)

Each service works with data. Therefore a good practice is build generators for data creation of each method. This generators is part of package for using in tests of other packages.

### [{{ cookiecutter.python_package }}/methods]({{ cookiecutter.python_package }}/generators/)

Here we save methods for connect to our service. Example of usage, you can find [here]({{ cookiecutter.python_package }}/methods.py)

### {{ cookiecutter.python_package }}/
 
Implementation of service with unit tests for internal functions. We think that service is part of package, 
therefore we include this folder from package. But you must not import this module

Internal functions, models of REST API, server, data transformers, utils etc.

### [scripts/](scripts)

Service scripts are stored here. Default scripts:

- Getting variables from Vault or file (variable.py). This script it need for `make run` command

### [tests/](tests)

This directory consists only integration tests. In this directory cannot import files from another directories except 
package directory (python_service_layout). We tests our service as block box method. Therefore we cannot use common 
functions or scripts with tested sources.

### makefile

Makefile is given interface for control of application: dependencies, run, test, deploying.
  
### setup

This is template for configuration of package of setuptools package
  
### info

This file consists version and package's name.
