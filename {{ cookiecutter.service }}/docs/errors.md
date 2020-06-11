# Not secured connection

Probably you don't set `TAG` or `VERSION` before `make publish-image`. Please, add `daemon.json` to `/etc/docker/daemon.json`. You can read more [here](https://github.com/U-Company/python-private-service-layout/tree/master/%7B%7B%20cookiecutter.service%20%7D%7D) or [here](https://github.com/U-Company/notes/tree/master/deployments)

    The push refers to repository [84.201.149.110:443/l]
    Get https://84.201.149.110:443/v2/: http: server gave HTTP response to HTTPS client
    
 # Anaconda not found
 
You can [install](https://www.anaconda.com/products/individual) anaconda You can read this answer https://stackoverflow.com/questions/35246386/conda-command-not-found/44319368 

    Conda command not found
    
    
# Some command not found

Please see [this](https://github.com/U-Company/python-private-service-layout#usage) page
    
# Tag or version not set

Probably you don't set `TAG` or `VERSION` before `make publish-image`. You can see some info [here](https://github.com/U-Company/python-private-service-layout#usage) or [here](https://github.com/U-Company/python-private-service-layout/blob/master/%7B%7B%20cookiecutter.service%20%7D%7D/docs/commands.md)

    docker tag  192.168.0.1/<image-name>:
    "docker tag" requires exactly 2 arguments.
    See 'docker tag --help'.

    Usage:  docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]

    Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
    makefile:53: recipe for target 'publish-image' failed
    make: *** [publish-image] Error 1

# .pypirc file configuration

Probably you run the `make publish-package`

Cases:

1. You forget to copy or change the file `./deployments/.secrets/.pypirc` to `~/`.
2. You forget to add alias to `[distutils]` section into `.pypirc` file after change him.
3. You forget to add section with alias to `.pypirc` file after change him.

You can find more info [here](https://github.com/U-Company/python-private-service-layout/tree/master/%7B%7B%20cookiecutter.service%20%7D%7D#prepare-config-for-pip-ubuntu) or [here](https://github.com/U-Company/notes/tree/master/deployments).

Error:

    Traceback (most recent call last):
      File "setup.py", line 38, in <module>
        '<project-name>_http=<project-name>.__cmd.http_:main',
      File "/home/username/anaconda3/envs/l/lib/python3.7/site-packages/setuptools/__init__.py", line 161, in setup
        return distutils.core.setup(**attrs)
      File "/home/username/anaconda3/envs/l/lib/python3.7/distutils/core.py", line 148, in setup
        dist.run_commands()
      File "/home/username/anaconda3/envs/l/lib/python3.7/distutils/dist.py", line 966, in run_commands
        self.run_command(cmd)
      File "/home/username/anaconda3/envs/l/lib/python3.7/distutils/dist.py", line 985, in run_command
        cmd_obj.run()
      File "/home/username/anaconda3/envs/l/lib/python3.7/distutils/command/upload.py", line 64, in run
        self.upload_file(command, pyversion, filename)
      File "/home/username/anaconda3/envs/l/lib/python3.7/distutils/command/upload.py", line 74, in upload_file
        raise AssertionError("unsupported schema " + schema)
    AssertionError: unsupported schema 
    makefile:58: recipe for target 'publish-package' failed
    make: *** [publish-package] Error 1
    
# Duplicate package

Probably you run the `make publish-package` and get this error:

    Upload failed (409): Conflict
    error: Upload failed (409): Conflict
    makefile:58: recipe for target 'publish-package' failed
    make: *** [publish-package] Error 1

It means that, this package already exists. Please change version or remove old version. You can remove by [this](https://github.com/U-Company/notes/tree/master/deployments#publish-image-into-docker-registry-for-local-development-and-testing) way.
