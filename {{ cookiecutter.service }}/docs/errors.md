# Not secured connection

Probably you don't set `TAG` or `VERSION` before `make publish-image`. Please, add `daemon.json` to `/etc/docker/daemon.json`. You can read more [here](/{{ cookiecutter.python_package }}) or [here](/{{ cookiecutter.python_package }}/deployments)

    The push refers to repository [{{ cookiecutter.docker_registry }}/{{ cookiecutter.python_package }}]
    Get {{ cookiecutter.docker_registry }}/v2/: http: server gave HTTP response to HTTPS client
 
# Anaconda prefix error
 
    CondaValueError: prefix already exists: /home/username/anaconda3/envs/environment
 
 Probably, you use `make config` twice. The latest version of anaconda try to replace existed environment.
 
 Probably, you use not latest conda version (conda 4.5.* and lower). You need to update anaconda:
 
    conda update conda    
 
# Anaconda not found
 
You can [install](https://www.anaconda.com/products/individual) anaconda You can read this answer https://stackoverflow.com/questions/35246386/conda-command-not-found/44319368 

    Conda command not found
    
You can insert to the file `~/.bashrc` next line:

    export PATH="/path/to/anaconda/bin:$PATH"    
    
Example:

    export PATH="/home/username/anaconda3/bin:$PATH"    
    
# Some command not found

Please see [this](https://github.com/U-Company/python-private-service-layout#usage) page
    
# Tag or version not set

Probably you don't set `TAG` or `VERSION` before `make publish-image`. You can see some info [here](https://github.com/U-Company/python-private-service-layout#usage) or [here](/{{ cookiecutter.python_package }}/docs/commands.md)

    docker tag  {{ cookiecutter.docker_registry }}/{{ cookiecutter.docker_image }}:
    "docker tag" requires exactly 2 arguments.
    See 'docker tag --help'.

    Usage:  docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]

    Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
    makefile:53: recipe for target 'publish-image' failed
    make: *** [publish-image] Error 1

# .pypirc file configuration

Error:

    Traceback (most recent call last):
      File "setup.py", line 38, in <module>
        '{{ cookiecutter.python_package }}_http={{ cookiecutter.python_package }}.__cmd.http_:main',
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


Probably you run the `make publish-package`

Cases:

1. You forget to copy or change the file `./deployments/.secrets/.pypirc` to `~/`.
2. You forget to add alias to `[distutils]` section into `.pypirc` file after change him.
3. You forget to add section with alias to `.pypirc` file after change him.

You can find more info [here](/{{ cookiecutter.python_package }}#prepare-config-for-pip-ubuntu) or [here](/{{ cookiecutter.python_package }}deployments).
    
# Duplicate package

    Upload failed (409): Conflict
    error: Upload failed (409): Conflict
    makefile:58: recipe for target 'publish-package' failed
    make: *** [publish-package] Error 1
    
Probably you run the `make publish-package` and get this error:

It means that, this package already exists. Please change version or remove old version. You can remove by [this](https://github.com/U-Company/notes/tree/master/deployments#publish-image-into-docker-registry-for-local-development-and-testing) way.

# Problem with uninstall

    Cannot uninstall 'certifi'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.

**Best rule**. You can solve this problem with reinitialization anaconda:

    make config
    
Or you can change make file rule `deps`. Add `--ignore-installed` for pip. You can read [some](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-i) [topics](https://stackoverflow.com/questions/51913361/difference-between-pip-install-options-ignore-installed-and-force-reinstall) [about](https://github.com/pypa/pip/issues/5247) [it](https://github.com/galaxyproject/galaxy/issues/7324).

The second way can break down you application.    
    
# Vault client not authenticated

    Traceback (most recent call last):
      File "/home/username/python/version/version/__cmd/http_.py", line 16, in <module>
        from version.__server import config, models
      File "/home/username/python/version/version/__server/config.py", line 13, in <module>
        assert vault_client.is_authenticated, 'Vault client not authenticated'
    AssertionError: Vault client not authenticated
    
If you use NOT `LOCAL` mode of development, check vault credentials. You need to set these environments for [vault-client](https://github.com/U-Company/vault-client):

    VAULT_TOKEN=
    VAULT_PORT=
    VAULT_HOST=
    VAULT_MOUNT_POINT=
    VAULT_ENV=
    
One way do this: set environments into `.env` file into `deployments/.envs/` or pass another way.

If you use `LOCAL` mode of develop and you get such problem, than probably you use a PyCharm or another IDE. In this case, you can forget change a workdir. Please, set them as root directory of project. PyCharm example:

![](/docs/IDE_workdir.png)

# Not set environments

    Traceback (most recent call last):
      File "/home/username/python/version/version/__cmd/http_.py", line 16, in <module>
        from version.__server import config, models
      File "/home/username/python/version/version/__server/config.py", line 11, in <module>
        vault_client = VaultClient(environ=VAULT_ENV, env_file=VAULT_ENV_FILE)
      File "<string>", line 5, in __init__
      File "/home/username/anaconda3/envs/version/lib/python3.7/site-packages/vault_client/client.py", line 22, in __post_init__
        self.environ = self.environ.upper()
    AttributeError: 'NoneType' object has no attribute 'upper'
    
If you start with mode of vault `LOCAL`, probably, you forget set environments: `VAULT_ENV` or `VAULT_ENV_FILE`. Please, check default values by path: ![]({{ cookiecutter.docker_registry }}/__server/config.py):

    VAULT_ENV = os.environ.get('VAULT_ENV')
    VAULT_ENV_FILE = os.environ.get('VAULT_ENV_FILE')
    
Change to 

    VAULT_ENV = os.environ.get('VAULT_ENV', 'LOCAL')
    VAULT_ENV_FILE = os.environ.get('VAULT_ENV_FILE', 'deployments/.envs/local.env')
    
Or set environments by handle.
