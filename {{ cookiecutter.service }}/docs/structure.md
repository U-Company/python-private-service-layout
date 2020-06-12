## [Project structure]({{ cookiecutter.service }}/docs/structure.md)

### [data/]({{ cookiecutter.service }}/data)

This folder must consists the data of service. We think to a large data file must dumps to any storage (
databases, file storage, git LFS, docs and other). Most part of data here is test's data.

### data/tests/

Files for tests

### data/docs/

Design and user documents.

### [deployments/]({{ cookiecutter.service }}/deployments)

IaaS, PaaS, system and container orchestration deployment configurations and templates (docker-compose, kubernetes/helm,
mesos, terraform, bosh).

You can deploy applications with different docker-compose files and different environment files. Our docker files are built by a make file, which uses as API interface for commutication building of any programm.

Type of docker files:

* **docker-compose.env.yml** -- environment for your application. For example, you have some databases and some servicese, but you want to run your application from source (for debugging, for instance). Then, you can runnig only this file.
* **docker-compose.full.yml** -- full application with environment

We have environment file into `./.envs` directory.

**Notice**: we configure compose with `network_mode: host` (in) therefore, our image links with localhost (no mapping ports, for example)

You can read about publishing packages [here]({{ cookiecutter.service }}/deployments).

### data/logs/

Folder for logs files 

### {{ cookiecutter.service }}/ 

Library code that's ok to use by external applications (e.g., /service_name/mypubliclib). Other projects will
import these libraries expecting them to work, so think twice before you put something here :-) Note that catalogs with prefix `__` is a better way to ensure your private packages. In python this fact denotes private structures. The 
/service_name directory is still a good way to explicitly communicate that the code in that directory is safe 
for use by others.

This package's name has the same name as repo name (_ instead of -). This package (folder) publish to pypi-registry.
### [{{ cookiecutter.service }}/__cmd/]({{ cookiecutter.service }}/__cmd/)
 
Main applications for this project.

The directory name for each application should match the name of the executable you want to have (e.g., {{ cookiecutter.service }}/__cmd/cli.py).

For example, you have service (`http_.py`), CLI runner `cli.py`.

Don't put a lot of code in the application directory. If you think the code can be imported and used in other projects, 
then it should live in the `/service_name` directory. If the code is not reusable or if you don't want others 
to reuse it, put that code in the /internal directory. You'll be surprised what others will do, so be explicit about 
your intentions!

It's common to have a small main function that imports and invokes the code from the `/internal` and `/pkg` directories 
and nothing else.

See the `/__cmd` directory for examples.

We save `__cmd` into package therefore `__cmd` must be include into package to cli works. But cmd is not part of library.

### [{{ cookiecutter.service }}/tests]({{ cookiecutter.service }}/tests/)

This repo consists unit tests. Unit tests is used to test functions

### [{{ cookiecutter.service }}/generators]({{ cookiecutter.service }}/generators/)

Each service works with data. Therefore a good practice is build generators for data creation of each method. This generators is part of package for using in tests of other packages.

### [{{ cookiecutter.service }}/methods]({{ cookiecutter.service }}/generators/)

Here we save methods for connect to our service. Example of usage, you can find [here]({{ cookiecutter.service }}/methods.py)

### {{ cookiecutter.service }}/
 
Implementation of service with unit tests for internal functions. We think that service is part of package, 
therefore we include this folder from package. But you must not import this module. We save service and cli here to add 
availability to them from console  

Internal functions, models of REST API, server, data transformers, utils etc.

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
