PYTHONPATH=.
SCRIPTS=scripts/
TESTS=tests/

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
	$(ENVS) $(PYTHON) app.py

test:
	$(info waiting server...)
	$(ENVS) $(PYTHON) ${SCRIPTS}waiting.py
	$(info integration tests running...)
	$(info $(ENVS))
	$(info ${TESTS}${TEST_SUBFOLDER})
	$(ENVS) $(PYTEST) -v -l --disable-warnings ${TESTS}${TEST_SUBFOLDER}

deps:
	$(info dependencies installing...)
	$(info $(ENVS))
	$(PIP) install -r requirements

