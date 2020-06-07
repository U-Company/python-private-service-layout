PYTHONPATH=.
SCRIPTS=scripts/
TESTS_UNIT={{ cookiecutter.service }}/tests/
TESTS_INTEGRATION=tests/
REQ=requirements
REQ_PRIVATE=requirements.private
SECRETS_PRIVATE=deployments/.secrets/pip_private.conf
DOCKER_COMPOSE_FULL=deployments/docker-compose.full.yml
DOCKER_COMPOSE_ENV=deployments/docker-compose.env.yml
VAULT_ENV_FILE_TEST=deployments/.envs/test.env
VAULT_ENV_FILE=deployments/.envs/local.env
CONDA=conda

ifndef PYTHON
	PYTHON=python
endif
ifndef DOCKER_COMPOSE
	DOCKER_COMPOSE=docker-compose
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
ifeq ($(TEST),yes)
	VAULT_ENV_FILE=${VAULT_ENV_FILE_TEST}
endif


.PHONY: config build publish clean deps run run-env run-full run-rebuild test-integration test-unit test

ENVS=PYTHONPATH=${PYTHONPATH} VAULT_ENV_FILE=${VAULT_ENV_FILE} VAULT_ENV=${VAULT_ENV}
ENVS_TEST=PYTHONPATH=${PYTHONPATH} VAULT_ENV_FILE=${VAULT_ENV_FILE_TEST} VAULT_ENV=${VAULT_ENV}


config:
	$(ENVS) $(CONDA) create --name {{ cookiecutter.service }} python=3.7

build:
	$(ENVS) $(PYTHON) setup.py bdist_wheel
	$(ENVS) $(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FULL) build

publish:
	$(ENVS) $(PYTHON) setup.py bdist_wheel upload -r {{ cookiecutter.pypi_alias }}
	$(ENVS) $(DOCKER) login {{ cookiecutter.docker_host }}:{{ cookiecutter.docker_port }}
	$(ENVS) $(DOCKER) tag $(TAG) {{ cookiecutter.docker_host }}:{{ cookiecutter.docker_port }}/{{ cookiecutter.service }}:$(VERSION)
	$(ENVS) $(DOCKER) push {{ cookiecutter.docker_host }}:{{ cookiecutter.docker_port }}/{{ cookiecutter.service }}:$(VERSION)

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf {{ cookiecutter.service }}.egg-info
	rm -rf data/test/temp/

deps:
	$(ENVS) $(PIP) install -r $(REQUIREMENTS)

run:
	$(ENVS) $(PYTHON) {{ cookiecutter.service }}/__cmd/http_.py

run-full:
	$(ENVS) $(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FULL) -p local_{{ cookiecutter.service }} up

run-env:
	$(ENVS) $(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_ENV) -p local_{{ cookiecutter.service }} up

run-rebuild:
	$(ENVS) $(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FULL) -p local_{{ cookiecutter.service }} up --build

test-integration:
	$(ENVS_TEST) $(PYTEST) -v -l --disable-warnings ${TESTS_INTEGRATION}${TEST_SUBFOLDER}

test-unit:
	$(ENVS_TEST) $(PYTEST) -v -l --disable-warnings ${TESTS_UNIT}${TEST_SUBFOLDER}

test: test-unit test-integration
