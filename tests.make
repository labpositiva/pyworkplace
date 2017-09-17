#
# See ./CONTRIBUTING.rst
#

lint: ## Make Lint Files
	@make clean
	pre-commit run --all-files --verbose

test: ## make test
	@make clean
	@echo $(MESSAGE) Running tests on the current Python interpreter with coverage $(END)
	py.test --cov pyworkplace --cov tests --doctest-modules --verbose pyworkplace tests
	@echo