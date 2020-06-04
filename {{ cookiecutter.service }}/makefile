PYTHONPATH=.
SCRIPTS=scripts/
TESTS_UNIT={{ cookiecutter.service }}/tests/
TESTS_INTEGRATION=tests/
REQUIREMENTS=requirements
DOCKER_COMPOSE_FULL=deployments/docker-compose.full.yml
DOCKER_COMPOSE_ENV=deployments/docker-compose.env.yml

ifndef PYTHON
	PYTHON=python
endif
ifndef DOCKER_COMPOSE
	DOCKER_COMPOSE=docker-comp#ose
endif
ifndef DOCKER
	DOCKER=DOCKER
endif
ifndef PYTEST
	PYTEST=pytest
endif
ifndef PIP
	PIP=pip
endif
ifndef TEST_SUBFOLDER
	TEST_SUBFOLDER=./
endif
ifndef VAULT_ENV
	VAULT_ENV=LOCAL
endif

ENVS=PYTHONPATH=${PYTHONPATH}

.PHONY: config build publish clean deps run run-env run-full run-rebuild test-integration test-unit test



config:
	conda create --name {{ cookiecutter.service }} python=3.7

build:
	$(PYTHON) setup.py bdist_wheel
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FULL) build

publish:
	$(PYTHON) setup.py bdist_wheel upload -r {{ cookiecutter.pypi_alias }}
	$(DOCKER) login {{ cookiecutter.docker_host }}:{{ cookiecutter.docker_port }}
	$(DOCKER) tag $(TAG) {{ cookiecutter.docker_host }}:{{ cookiecutter.docker_port }}/{{ cookiecutter.service }}:$(VERSION)
	$(DOCKER) push {{ cookiecutter.docker_host }}:{{ cookiecutter.docker_port }}/{{ cookiecutter.service }}:$(VERSION)

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf {{ cookiecutter.service }}.egg-info

deps:
	$(PIP) install -r $(REQUIREMENTS)

run:
	$(PYTHON) {{ cookiecutter.service }}/__cmd/http_.py

run-full:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FULL) -p local_{{ cookiecutter.service }} up

run-env:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_ENV) -p local_{{ cookiecutter.service }} up

run-rebuild:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FULL) -p local_{{ cookiecutter.service }} up --build

test-integration:
	$(info ${TESTS}${TEST_SUBFOLDER})
	$(PYTEST) -v -l --disable-warnings ${TESTS_INTEGRATION}${TEST_SUBFOLDER}

test-unit:
	$(info ${TESTS}${TEST_SUBFOLDER})
	$(PYTEST) -v -l --disable-warnings ${TESTS_UNIT}${TEST_SUBFOLDER}

test: test-unit test-integration
