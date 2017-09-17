#
# See ./CONTRIBUTING.rst
#

TAG=""
END=""

clean: ## clean Files compiled
	@echo "$(TAG)"Cleaning up"$(END)"
	rm -rf .tox *.egg dist build .coverage
	find . -name '__pycache__' -delete -print -o -name '*.pyc' -delete -print -o -name '*.tmp' -delete -print
	@echo