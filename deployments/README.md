# /deployments

You can deploy applications with different docker-compose files and different environment files. Our docker files are built by a make file, which uses as API interface for commutication building of any programm.

Type of docker files:

* **docker-compose.env.yml** -- environment for your application. For example, you have some databases and some services, but you want to run your application from source (for debugging, for instance). Then, you can runnig only this file.
* **docker-compose.full.yml** -- full application with environment

For each docker-compose we have environment file into `./.envs` directory.

**Notice**: we configure compose with `network_mode: host` (in) therefore, our image links with localhost (no mapping ports, for example)
