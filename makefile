PYTHONPATH=.
SCRIPTS=scripts/
TESTS_UNIT=tamplar/tests/
TESTS_INTEGRATION=tests/

ifndef PYTHON
	PYTHON=python
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

ENVS=PYTHONPATH=${PYTHONPATH} ENV_FILE=${ENV_FILE}

run:
	$(info storage starting...)
	$(info $(ENVS))
	$(info ${STORAGE_ENV_FILE})
	$(ENVS) $(PYTHON) service/internal/server.py

test-integration:
	$(info waiting server...)
	$(ENVS) $(PYTHON) ${SCRIPTS}waiting.py
	$(info integration tests running...)
	$(info $(ENVS))
	$(info ${TESTS}${TEST_SUBFOLDER})
	$(ENVS) $(PYTEST) -v -l --disable-warnings ${TESTS_INTEGRATION}${TEST_SUBFOLDER}

test-unit:
	$(info waiting server...)
	$(ENVS) $(PYTHON) ${SCRIPTS}waiting.py
	$(info integration tests running...)
	$(info $(ENVS))
	$(info ${TESTS}${TEST_SUBFOLDER})
	$(ENVS) $(PYTEST) -v -l --disable-warnings ${TESTS_UNIT}${TEST_SUBFOLDER}

deps:
	$(info dependencies installing...)
	$(info $(ENVS))
	$(PIP) install -r requirements

