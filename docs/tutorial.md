## Tutorial

After initialization, cookiecutter ask you about clonning the latest version into temporary repo (if you have our already layout). Anothercase, cookiecutter clonning repo into `/home/your-name/.cookiecutters`:

    You've downloaded /home/your-name/.cookiecutters/python-service-layout before. Is it okay to delete and re-download it? [yes]: 
    
If you said `yes`, cookicutter clonning repo with replace. Othercase (`no`), you get another else question:

    Do you want to re-use the existing version? [yes]: 
    
If you said `no`, cookiecutter is finished.

Now, cookiecutter ask you some questions about your environment (`-` donotes not skip variable).

The first block:

1. `author`. Enter your name
2. `email`. Enter your email
3. `description`. Enter description your service's name
4. `service`. Enter your service's name
5. `python_package`. Compiled python package's name

The second block:

6. `pypi_schema`. Enter your pypi registry's schema
7. `pypi_host_and_path`. Enter your pypi registry's host and path (for example `pypi.org/simple` or `192.168.0.1`)
8. `pypi_port`. Enter your pypi registry's port (**not required**)
9. `pypi_registry`. Compiled python registry's name
10. `pypi_alias`: alias to pypi registry
11. `pypi_login`: login to pypi registry (for publishing and installing)
12. `pypi_password`: password to pypi registry (for publishing and installing)

The third block:

13. `docker_schema`. Enter your docker registry's schema (**not required**)
14. `docker_host`. Enter your docker registry's host. For example `192.168.0.1` (**not required**)
16. `docker_port`. Enter your docker registry's port. For example `8000` (**not required**)
17. `docker_username`. Enter docker dockerhub's name. If you use private docker registry, skip this with entring `-`  (**not required**)
18. `docker_registry`. Compiled docker registry's name
19. `docker_image`. Compiled docker image's name

*Notice*. If you don want to use common docker hub registry, please enter `docker_username`. Othercase, enter `docker_schema`, `docker_host` and `docker_port`.
