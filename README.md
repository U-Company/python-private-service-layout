# python-service-layout

This repository is inspired by the repository of [layout-golang](https://github.com/golang-standards/project-layout). 
We build template for services of python. We use [FastAPI](https://github.com/tiangolo/fastapi) and 
[uvicorn](https://www.uvicorn.org/) for service creation. For automation we create 
[tamplar](https://github.com/hedgehogues/tamplar). This tool can init repo, control dependencies and publish docker and 
packages.  

![](docs/structure.png)

Red is not public source. Green is public source. Package consists public and not public sources.

## Usage

If you want to use our layout, you can try [tamplar](https://github.com/u-company/tamplar) or you must change some 
files:

- info.py
- setup.py
- makefile
- deployments/.secrets/pip.conf
- deployments/.envs/local.env

tamplar can work with:

- python setup
- pip
- publishing package to pypi registry
- publishing docker to docker registry
- docker-compose for local development

## Service

Our service has:

- [prometheus endpoint](https://github.com/prometheus/client_python)
- [vault-client](https://github.com/Flesspro/vault-client)
- healthcheck
- docker-compose for local development
- loguru for logging
- FastAPI as service

## Project structure:
  
### configs/ 

Configuration file templates or default configs.

### docs/

Design and user documents.

### data/

This folder must consists the data of service and library. We think to a large data file must dumps to any storage (
databases, file storage, git LFS and other). Most part of these data is test's data.

### [deployments/](deployments/)

IaaS, PaaS, system and container orchestration deployment configurations and templates (docker-compose, kubernetes/helm,
mesos, terraform, bosh).

You can deploy applications with different docker-compose files and different environment files. Our docker files are built by a make file, which uses as API interface for commutication building of any programm.

Type of docker files:

* **docker-compose.env.yml** -- environment for your application. For example, you have some databases and some servicese, but you want to run your application from source (for debugging, for instance). Then, you can runnig only this file.
* **docker-compose.full.yml** -- full application with environment

We have environment file into `./.envs` directory.

**Notice**: we configure compose with `network_mode: host` (in) therefore, our image links with localhost (no mapping ports, for example)

You can read about publishing packages [here](deployments).

### logs/

Folder for logs files 

### python_service_layout/ 
 
Library code that's ok to use by external applications (e.g., /python_service_layout/mypubliclib). Other projects will 
import these libraries expecting them to work, so think twice before you put something here :-) Note that the internal
directory is a better way to ensure your private packages are not importable because it's enforced by Go. The 
/python_service_layout directory is still a good way to explicitly communicate that the code in that directory is safe 
for use by others.

This package's name has the same name as repo name (_ instead of -). This package (folder) publish to pypi-registry.

### [python_service_layout/__cmd/](python_service_layout/__cmd/)
 
Main applications for this project.

The directory name for each application should match the name of the executable you want to have (e.g., /__cmd/cli.py).

For example, you have service (`http.py`), CLI runner `cli.py`.

Don't put a lot of code in the application directory. If you think the code can be imported and used in other projects, 
then it should live in the `/python_service_layout` directory. If the code is not reusable or if you don't want others 
to reuse it, put that code in the /internal directory. You'll be surprised what others will do, so be explicit about 
your intentions!

It's common to have a small main function that imports and invokes the code from the `/internal` and `/pkg` directories 
and nothing else.

See the `/__cmd` directory for examples.

We save `__cmd` into package therefore `__cmd` must be include into package to cli works. But cmd is not part of library.

### [python_service_layout/generators/](python_service_layout/generators/)

Each service works with data. Therefore a good practice is build generators for data creation of each method. This generators is part of package for using in tests of other packages.

### service/
 
Implementation of service with unit tests for internal functions. We think that service is not part of package, 
therefore we exclude this folder from package.

### service/internal/

Internal functions and utils (for example, models of REST API), transformers data etc.

### service/tests/

Unit tests of your service's functions.

### [tests/](tests)

This directory consists only integration tests. In this directory cannot import files from another directories except 
package directory (python_service_layout). We tests our service as block box method. Therefore we cannot use common 
functions or scripts with tested sources.

### makefile

Makefile is given interface for control of application: dependencies, run, test.
  
### setup.tmpl

This is template for configuration of package of setuptools package
  
### version.tmpl

This file consists version and package's name.
