# Docker
DOCKER_NETWORK = $(PROJECT_NAME)_network

build:  ## Build docker container by env
	@make clean
	@echo $(MESSAGE) "Building environment: ${env}"
	@if [ "${env}" == "" ]; then \
		docker-compose build --no-cache; \
	elif [ "${env}" == "dev" ]; then \
		docker-compose -f docker-compose.yml -f docker-compose/dev.yml -p "${PROJECT_NAME_DEV}" build --no-cache; \
	elif [ "${env}" == "stage" ]; then \
		docker-compose -f docker-compose.yml -f docker-compose/stage.yml -p "${PROJECT_NAME_STAGE}" build --no-cache; \
	elif [ "${env}" == "test" ]; then \
		docker-compose -f docker-compose.yml -f docker-compose/test.yml -p "${PROJECT_NAME_TEST}" build --no-cache; \
	elif [ "${env}" == "prod" ]; then \
		docker-compose -p "${PROJECT_NAME}" build --no-cache; \
	fi

down: ## remove containers docker by env
	make clean
	@echo $(MESSAGE) "Down Services Environment: ${env}"
	@if [ "${env}" == "" ]; then \
		docker-compose -p "${PROJECT_NAME}" down --remove-orphans; \
	elif [ "${env}" == "dev" ]; then \
		docker-compose -f docker-compose.yml -f docker-compose/dev.yml -p "${PROJECT_NAME_DEV}" down --remove-orphans; \
	elif [ "${env}" == "stage" ]; then \
		docker-compose -f docker-compose.yml -f docker-compose/stage.yml -p "${PROJECT_NAME_STAGE}" down --remove-orphans; \
	elif [ "${env}" == "test" ]; then \
		docker-compose -f docker-compose.yml -f docker-compose/test.yml -p "${PROJECT_NAME_TEST}" down --remove-orphans; \
	elif [ "${env}" == "prod" ]; then \
		docker-compose -f docker-compose.yml -f docker-compose/prod.yml -p "${PROJECT_NAME}" down --remove-orphans; \
	fi

ssh: ## Connect to container
	docker exec -it $(CONTAINER) bash

stop: ## stop containers docker by env
	make clean
	@echo $(MESSAGE) "Stop Services: ${env}"
	@if [ "${env}" == "" ]; then \
		docker-compose -p "${PROJECT_NAME}" stop; \
	elif [ "${env}" == "dev" ]; then \
		docker-compose -f docker-compose.yml -f docker-compose/dev.yml -p "${PROJECT_NAME_DEV}" stop; \
	elif [ "${env}" == "stage" ]; then \
		docker-compose -f docker-compose.yml -f docker-compose/stage.yml -p "${PROJECT_NAME_STAGE}" stop; \
	elif [ "${env}" == "test" ]; then \
		docker-compose -f docker-compose.yml -f docker-compose/test.yml -p "${PROJECT_NAME_TEST}" stop; \
	elif [ "${env}" == "prod" ]; then \
		docker-compose -f docker-compose.yml -f docker-compose/prod.yml -p "${PROJECT_NAME}" stop; \
	fi

verify_network: ## Verify network
	@if [ -z $$(docker network ls | grep $(DOCKER_NETWORK) | awk '{print $$2}') ]; then\
		(docker network create $(DOCKER_NETWORK));\
	fi

up: ## Run services docker
	make clean
	@echo $(MESSAGE) "Up Services: ${env}"
	@if [ "${env}" == "" ]; then \
		docker-compose -p "${PROJECT_NAME}" up --remove-orphans; \
	elif [ "${env}" == "dev" ]; then \
		docker-compose -f docker-compose.yml -f docker-compose/dev.yml -p "${PROJECT_NAME_DEV}" up --remove-orphans; \
	elif [ "${env}" == "stage" ]; then \
		docker-compose -f docker-compose.yml -f docker-compose/stage.yml -p "${PROJECT_NAME_STAGE}" up --remove-orphans; \
	elif [ "${env}" == "test" ]; then \
		docker-compose -f docker-compose.yml -f docker-compose/test.yml -p "${PROJECT_NAME_TEST}" up --remove-orphans; \
	elif [ "${env}" == "prod" ]; then \
		docker-compose -f docker-compose.yml -f docker-compose/prod.yml -p "${PROJECT_NAME}" up --remove-orphans; \
	fi

list: ## List of current active services by env
	@make clean
	@echo $(MESSAGE) "List Services: ${env}"
	@if [ "${env}" == "" ]; then \
		docker-compose -p "${PROJECT_NAME_DEV}" ps; \
	elif [ "${env}" == "dev" ]; then \
		docker-compose -f docker-compose.yml -f docker-compose/dev.yml -p "${PROJECT_NAME_DEV}" ps; \
	elif [ "${env}" == "stage" ]; then \
		docker-compose -f docker-compose.yml -f docker-compose/stage.yml -p "${PROJECT_NAME_STAGE}" ps; \
	elif [ "${env}" == "test" ]; then \
		docker-compose -f docker-compose.yml -f docker-compose/test.yml -p "${PROJECT_NAME_TEST}" ps; \
	elif [ "${env}" == "prod" ]; then \
		docker-compose -p "${PROJECT_NAME}" ps; \
	fi