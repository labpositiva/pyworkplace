#
# See ./CONTRIBUTING.rst
#

test.lint: clean
	pre-commit run --all-files --verbose

test: clean
	@echo $(MESSAGE) Running tests on the current Python interpreter with coverage $(END)
	docker-compose -f docker-compose.yml -f docker-compose/test.yml run --rm app \
		py.test --cov pyworkplace --cov tests --doctest-modules --verbose pyworkplace tests
	@echo

test.pytest: clean
	@echo $(MESSAGE) Running tests on the current Python $(END)
	@if [ "${test}" == "" ]; then \
		docker-compose -f docker-compose.yml -f docker-compose/test.yml run --rm app \
			py.test -s pyworkplace tests; \
	else \
		docker-compose -f docker-compose.yml -f docker-compose/test.yml run --rm app \
			py.test tests/"${test}"; \
	fi
