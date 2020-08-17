.PHONY: help venv test

PROJECT_NAME=pytest_tutorial

.DEFAULT: help
help:
	@echo "make venv"
	@echo "       install virtual environment using pipenv"
	@echo "make test"
	@echo "       run tests"
	@echo "make help"
	@echo "       print this help message"

venv:
ifeq (,$(shell which pipenv))
	pip3 install pipenv
endif
	pipenv install

test:
	pipenv run pytest

