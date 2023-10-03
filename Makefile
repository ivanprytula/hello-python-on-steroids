# CREDITS:
# Code/logic for having colorful output was taken & modified from (c) https://gist.github.com/rsperl/d2dfe88a520968fbc1f49db0a29345b9

SHELL=/bin/bash

# --------------------------------------------------------------------------------------
# GENERAL CONFIG
# --------------------------------------------------------------------------------------


# to see all colors, run
# bash -c 'for c in {0..255}; do tput setaf $c; tput setaf $c | cat -v; echo =$c; done'
# the first 15 entries are the 8-bit colors

# define standard colors
ifneq (,$(findstring xterm,${TERM}))
	BLACK        := $(shell tput -Txterm setaf 0)
	RED          := $(shell tput -Txterm setaf 1)
	GREEN        := $(shell tput -Txterm setaf 2)
	YELLOW       := $(shell tput -Txterm setaf 3)
	LIGHTPURPLE  := $(shell tput -Txterm setaf 4)
	PURPLE       := $(shell tput -Txterm setaf 5)
	BLUE         := $(shell tput -Txterm setaf 6)
	WHITE        := $(shell tput -Txterm setaf 7)
	RESET := $(shell tput -Txterm sgr0)
else
	BLACK        := ""
	RED          := ""
	GREEN        := ""
	YELLOW       := ""
	LIGHTPURPLE  := ""
	PURPLE       := ""
	BLUE         := ""
	WHITE        := ""
	RESET        := ""
endif

# set target color
TARGET_COLOR := $(BLUE)

POUND = \#

.PHONY: no_targets__ info help build deploy doc
	no_targets__:

.DEFAULT_GOAL := help

# NB: @ prefix in line suppress echoing of the line

colors: ## show all the colors
	@echo "${BLACK}BLACK${RESET}"
	@echo "${RED}RED${RESET}"
	@echo "${GREEN}GREEN${RESET}"
	@echo "${YELLOW}YELLOW${RESET}"
	@echo "${LIGHTPURPLE}LIGHTPURPLE${RESET}"
	@echo "${PURPLE}PURPLE${RESET}"
	@echo "${BLUE}BLUE${RESET}"
	@echo "${WHITE}WHITE${RESET}"$(var)

help:
	@echo ""
	@echo "    ${BLACK}:: ${RED}Self-documenting Makefile${RESET} ${BLACK}::${RESET}"
	@echo ""
	@echo "Document targets by adding '$(POUND)$(POUND) comment' after the target"
	@echo ""
	@echo "Example:"
	@echo "  | job1:  $(POUND)$(POUND) help for job 1"
	@echo "  | 	@echo \"run stuff for target1\""
	@echo ""
	@echo "${BLACK}-----------------------------------------------------------------${RESET}"
	@grep -E '^[a-zA-Z_0-9%-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "${TARGET_COLOR}%-30s${RESET} %s\n", $$1, $$2}'
# --------------------------------------------------------------------------------------
# GENERAL CONFIG
# --------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------
# Project's commands (local setup)
# --------------------------------------------------------------------------------------

# Dependencies management

lock-deps-dev:
	pip-compile --upgrade --generate-hashes --strip-extras --verbose --output-file requirements/local.txt requirements/local.in

lock-deps-prod:
	pip-compile --upgrade --generate-hashes --strip-extras --output-file requirements/production.txt requirements/production.in

audit-deps-local:
	pip-audit --requirement requirements/local.in

audit-deps-prod:
	pip-audit --requirement requirements/production.in

install-deps-local:
	pip install --require-hashes --no-deps -r requirements/local.txt

install-deps-prod:
	pip install -r requirements/production.txt

pcau:
	pre-commit autoupdate

# manage.py commands + extras from django_extensions
mm:
	python manage.py makemigrations

mig:
	python manage.py migrate

colstat:
	python manage.py collectstatic --no-input

runs:  ## standard HTTP + option: whitenoise (if enabled, run collectstatic first)
	python manage.py runserver

runs-plus:  ## ... + using the Werkzeug debugger + faster reload on files changes with watchdog
	python manage.py runserver_plus

runs-ssl: ## HTTPS with the help of Werkzeug and mkcert
	python manage.py runserver_plus --cert-file cert.pem --key-file key.pem

run-gu-ssl:  ## HTTPS. Strongly recommended using Gunicorn behind a proxy server
	gunicorn --timeout 1000 --workers 2 --bind 127.0.0.1:8000 --log-level debug --certfile cert.pem  --keyfile key.pem django_project.wsgi

show-urls:
	python manage.py show_urls --format=table

pre-commit-all:
	pre-commit run --all-files

docs-serve:
	mkdocs serve --dev-addr 127.0.0.1:8002


# Frontend


# --------------------------------------------------------------------------------------
# Project's commands (containerized setup)
# --------------------------------------------------------------------------------------

dconf:  ## Parse, resolve and render Compose file in canonical format
	docker compose config

build: ## Build or rebuild Compose services
	docker compose -f docker-compose.yml -f docker-compose.dev.yml build

up: ## Create and start containers
	docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d

stop:  ## Stop Compose services (running containers)
	docker compose -f docker-compose.yml -f docker-compose.dev.yml stop

start:  ## Start Compose services
	docker compose -f docker-compose.yml -f docker-compose.dev.yml start

down:  ## Stop and remove containers, networks
	docker compose -f docker-compose.yml -f docker-compose.dev.yml down

.PHONY: clean
clean: ## Clean project containers and volumes with compose
	docker compose down -v --remove-orphans | true
	docker compose rm -f | true

# Testing, auto formatting, type checks, & Lint checks

pytest: ## Run project tests
	docker exec -it ${PROJECT_IMAGE_PREFIX}_${ENVIRONMENT}_web pytest -p no:warnings -v

format: ## Format project code.
	docker exec ${PROJECT_IMAGE_PREFIX}_${ENVIRONMENT}_web python -m black --config pyproject.toml .

isort: ## Sort project imports.
	docker exec ${PROJECT_IMAGE_PREFIX}_${ENVIRONMENT}_web isort .

type:  ## Static typing check
	docker exec ${PROJECT_IMAGE_PREFIX}_${ENVIRONMENT}_web mypy --ignore-missing-imports price_navigator/

lint:  ## Lint project code.
	docker exec ${PROJECT_IMAGE_PREFIX}_${ENVIRONMENT}_web flake8

ci: isort format type lint pytest

# Local dev

sh-web:
	docker exec -ti ${PROJECT_IMAGE_PREFIX}_${ENVIRONMENT}_web bash

sh-db:
	docker exec -ti ${PROJECT_IMAGE_PREFIX}_${ENVIRONMENT}_db bash

verify-db-health:
	docker exec -ti ${PROJECT_IMAGE_PREFIX}_${ENVIRONMENT}_db psql -U postgres -c 'SELECT 1;'

psql-db:
	docker exec -ti ${PROJECT_IMAGE_PREFIX}_${ENVIRONMENT}_db psql -U postgres

check-migrations-state:
	docker compose  -f docker-compose.yml -f docker-compose.dev.yml exec web python manage.py showmigrations -l --verbosity 2

createsuperuser:
	docker compose  -f docker-compose.yml -f docker-compose.dev.yml exec web python manage.py createsuperuser
