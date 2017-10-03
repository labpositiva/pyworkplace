#
# See ./CONTRIBUTING.rst
#

TAG=""
END=""

clean: ## clean Files compiled
	@echo "$(TAG)"Cleaning up"$(END)"
	@rm -rf .tox *.egg dist build .coverage
	@find . -name '__pycache__' -delete -print -o -name '*.pyc' -delete -print -o -name '*.tmp' -delete -print
	@echo

environment: ## Make environment for developer
	@echo $(HOME)
	@if [ -e "$(HOME)/.pyenv" ]; then \
		eval "$(pyenv init -)"; \
		eval "$(pyenv virtualenv-init -)"; \
	fi
	pyenv virtualenv "${PYTHON_VERSION}" "${PYENV_NAME}" >> /dev/null 2>&1 || echo 'Oh Yeah!!'
	pyenv activate "${PYENV_NAME}" >> /dev/null 2>&1 || echo 'Oh Yeah!!'

install: ## Install with var env Dependences
	@make clean
	@echo $(MESSAGE) "Deployment environment: ${env}"
	@if [ "${env}" == "" ]; then \
		pip install -r requirements.txt; \
	elif [ "${env}" == "dev" ]; then \
		pip install -r "${REQUIREMENTS_DIR}/dev.txt"; \
	elif [ "${env}" == "stage" ]; then \
		pip install -r "${REQUIREMENTS_DIR}/stage.txt"; \
	elif [ "${env}" == "test" ]; then \
		pip install -r "${REQUIREMENTS_DIR}/test.txt"; \
	elif [ "${env}" == "prod" ]; then \
		pip install -r requirements.txt; \
	fi

setup: ## Install dependences initial
	@make clean
	pip install -r "${REQUIREMENTS_DIR}/setup.txt"
	pre-commit install