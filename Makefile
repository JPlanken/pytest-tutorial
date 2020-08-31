.PHONY: help venv test lint reformat

PROJECT_NAME=project_folder

.DEFAULT: help
help:
	@echo "make test"
	@echo "       run tests"
	@echo "make rl"
	@echo "       run reformatting and linting"
	@echo "make help"
	@echo "       print this help message"

venv:
ifeq (,$(shell which pipenv))
	pip3 install pipenv
endif
	pipenv install
	pipenv install --dev
	
test:
	pipenv run pytest --cov

rl:
	pipenv run isort -v $(PROJECT_NAME) tests
	pipenv run black $(PROJECT_NAME) tests
	pipenv run flake8 $(PROJECT_NAME) tests
	pipenv run mypy

score:
	pipenv run pylint $(PROJECT_NAME) tests