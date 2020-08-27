.PHONY: help venv test lint reformat

PROJECT_NAME=project_folder

.DEFAULT: help
help:
	@echo "make test"
	@echo "       run tests"
	@echo "make checks"
	@echo "       run reformatting and linting"
	@echo "make help"
	@echo "       print this help message"

test:
	pipenv run pytest --cov

check:
	pipenv run isort -v $(PROJECT_NAME) tests
	pipenv run black $(PROJECT_NAME) tests
	pipenv run flake8 $(PROJECT_NAME) tests
	pipenv run mypy
	# pipenv run pylint $(PROJECT_NAME) tests