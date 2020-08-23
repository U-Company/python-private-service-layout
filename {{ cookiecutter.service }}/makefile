PYTHONPATH=.
SCRIPTS=scripts/
TESTS_UNIT={{ cookiecutter.python_package }}/tests/
TESTS_INTEGRATION=tests/
REQ=requirements
REQ_PRIVATE=requirements.private
PIP_CONFIG_FILE=deployments/.secrets/pip_private.conf
DOCKER_COMPOSE_FULL=deployments/docker-compose.full.yml
DOCKER_COMPOSE_ENV=deployments/docker-compose.env.yml
VAULT_ENV_FILE_TEST=deployments/.envs/test.env
VAULT_ENV_FILE=deployments/.envs/local.env
CONDA=conda
UVICORN=uvicorn

ifndef PYTHON
	PYTHON=python
endif
ifndef DOCKER_COMPOSE
	DOCKER_COMPOSE=docker-compose
endif
ifndef DOCKER
	DOCKER=docker
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


WORKERS=$(shell $(ENVS) $(PYTHON) scripts/variable.py WORKERS)
PORT=$(shell $(ENVS) $(PYTHON) scripts/variable.py PORT)


config:
	$(ENVS) $(CONDA) create --name {{ cookiecutter.service }} python=3.7

build-image:
	$(ENVS) $(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FULL) build

publish-image:
	$(ENVS) $(DOCKER) tag $(TAG) {{ cookiecutter.docker_image }}:$(VERSION)
	$(ENVS) $(DOCKER) push {{ cookiecutter.docker_image }}:$(VERSION)

publish-package:
	$(ENVS) $(PYTHON) setup.py bdist_wheel upload -r {{ cookiecutter.pypi_alias }}

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf {{ cookiecutter.python_package }}.egg-info
	rm -rf data/test/temp/

deps:
	$(ENVS) $(PIP) install -r $(REQ) --use-feature=2020-resolver
	$(ENVS) PIP_CONFIG_FILE=${PIP_CONFIG_FILE} $(PIP) install -r $(REQ_PRIVATE) --use-feature=2020-resolver

run:
	$(ENVS) $(UVICORN) server.cmd.http_:app --workers=$(WORKERS) --port=$(PORT) --host=0.0.0.0

run-full:
	$(ENVS) $(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FULL) up

run-env:
	$(ENVS) $(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_ENV) up

run-rebuild:
	$(ENVS) $(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FULL) up --build

test-integration:
	$(ENVS_TEST) $(PYTEST) -v -l --disable-warnings ${TESTS_INTEGRATION}${TEST_SUBFOLDER}

test-unit:
	$(ENVS_TEST) $(PYTEST) -v -l --disable-warnings ${TESTS_UNIT}${TEST_SUBFOLDER}

test: test-unit test-integration
