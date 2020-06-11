# Not secured connection

Probably you don't set `TAG` or `VERSION` before make. Please, add `daemon.json` to `/etc/docker/daemon.json`. You can read more [here](https://github.com/U-Company/python-private-service-layout/tree/master/%7B%7B%20cookiecutter.service%20%7D%7D) or [here](https://github.com/U-Company/notes/tree/master/deployments)

    The push refers to repository [84.201.149.110:443/l]
    Get https://84.201.149.110:443/v2/: http: server gave HTTP response to HTTPS client
    
 # Anaconda not found
 
You can [install](https://www.anaconda.com/products/individual) anaconda You can read this answer https://stackoverflow.com/questions/35246386/conda-command-not-found/44319368 

    Conda command not found
    
    
# Some command not found

Please see [this](https://github.com/U-Company/python-private-service-layout#usage) page.
    
# Tag or version not set

Probably you don't set `TAG` or `VERSION` before `make publish-image`. You can see some info [here](https://github.com/U-Company/python-private-service-layout#usage) or [here](https://github.com/U-Company/python-private-service-layout/blob/master/%7B%7B%20cookiecutter.service%20%7D%7D/docs/commands.md).

    docker tag  192.168.0.1/<image-name>:
    "docker tag" requires exactly 2 arguments.
    See 'docker tag --help'.

    Usage:  docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]

    Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
    makefile:53: recipe for target 'publish-image' failed
    make: *** [publish-image] Error 1
