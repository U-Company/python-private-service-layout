# /deployments

You can deploy applications with different docker-compose files and different environment files. Our docker files are built by a make file, which uses as API interface for commutication building of any programm.

Type of docker files:

* **docker-compose.env.yml** -- environment for your application. For example, you have some databases and some services, but you want to run your application from source (for debugging, for instance). Then, you can runnig only this file.
* **docker-compose.full.yml** -- full application with environment

For each docker-compose we have environment file into `./.envs` directory.

**Notice**: we configure compose with `network_mode: host` (in) therefore, our image links with localhost (no mapping ports, for example)


# Prepare config for pip (Ubuntu)

Before publishing, you need to create file `~/.pypirc` like this:

    [distutils]
    index-servers=
        pypi
        private_pypi
    
    [pypi]
    repository: https://upload.pypi.org/legacy/ 
    username: <username_pypi>
    password: <password_pypi>
    
    [private_pypi]
    repository: <private-pypi-registry>
    username: <username_private_pipy_registry>
    password: <password_private_pipy_registry>
    
You must to set this file into home directory. 

# Publish package to private_pypi pypi server

Before publish, set differences into CHANGELOG.md, setup.py version. After that, you need to create new release into master branch on 
github. Now, you need update package:

    python setup.py bdist_wheel upload -r private_pypi
    
This command push your image to pypi-package-registry

# Installing package from private pypi repository

You must lay the config file `pip.conf` into `~/.pip/`:

    [global]
    index-url = http://<login>:<password>@<your-host>:<your-port>
    trusted-host = pypi.python.org
                   pypi.org
                   <your-host>

# Publish image into docker registry (for local development and testing)

Before build, you need add `pip.conf` into `.secrets`. You can see template [here](https://github.com/Hedgehogues/docker-compose-deploy/blob/master/.deploy/.secrets/pip.conf)

From the root directory build the image

    docker-compose -f .deploy/docker-compose.full.yml build
    
After that, you must find the line with next text (last lines):

    Successfully built <image-id>
    Successfully tagged <image-name>:latest
    
Now, you must set tag for image:

    docker tag <image-id> <private-docker-registry>/<project>-<version>-<service-name>:<the-same-version-setup.py>
    
Please, add insecure-registry parameters to `/etc/docker/daemon.json` (first time):

    {
        "insecure-registries" : [ "<private-docker-registry>" ]
    }
    
And restart docker (first time):

    sudo service docker restart

Now, login in docker registry with your login and password (first time):

    docker login <private-docker-registry> -u="<username>" -p="<password>"
    
Push the image:

    docker push <private-docker-registry>/<project>-<version>-<service-name>:<the-same-version-setup.py>
    
After that, you need remove image:

    docker rmi <image-id> --force

You can see images:

    http://<private-docker-registry>/v2/_catalog
    
You can see all versions for image:

    http://<private-docker-registry>/v2/<image-name>/tags/list
 
Or concrete versions:

    http://<private-docker-registry>/v2/<image-name>/tags/list
    
If you want remove specific version from pypi-registry, you can do this:

    curl --form ":action=remove_pkg" --form "name=pkg" --form "version=0.0.0" 0.0.0.0:1234 -H "Authorization: Basic <base64-string>"

    
**Notice**: while docker image building, we fix all environment variables includes ports and endpoints. After that, you cannot to change them. We will fix it in the future
