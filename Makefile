.PHONY: help venv test lint reformat

PROJECT_NAME=pytest_tutorial

.DEFAULT: help
help:
	@echo "make venv"
	@echo "       install virtual environment using pipenv"
	@echo "make test"
	@echo "       run tests"
	@echo "make lint"
	@echo "       run flake8 in app folder and mypy"
	@echo "make reformat"
	@echo "       run isort and black in app folder"
	@echo "make help"
	@echo "       print this help message"

venv:
ifeq (,$(shell which pipenv))
	pip3 install pipenv
endif
	pipenv install
	pipenv install --dev

test:
	pipenv run pytest

lint:
	pipenv run flake8 $(PROJECT_NAME) tests
	pipenv run mypy

reformat:
	pipenv run isort -v $(PROJECT_NAME) tests
	pipenv run black $(PROJECT_NAME) tests
