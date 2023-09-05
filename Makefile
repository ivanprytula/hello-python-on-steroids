# CREDITS:
# Code/logic for having colorful output was taken & modified from (c) https://gist.github.com/rsperl/d2dfe88a520968fbc1f49db0a29345b9

SHELL=/bin/bash

# --------------------------------------------------------------------------------------
# CONFIG
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
	@echo "${WHITE}WHITE${RESET}"

job1:  ## help for job 1
	@echo "job 1 started"
	@echo "run stuff for target1"
	@echo "job 1 finished"

job%:  ## help for job with wildcard
	@echo "job $@"

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
# CONFIG
# --------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------
# Project's commands
# --------------------------------------------------------------------------------------

# Dependencies management

install-deps-dev:
	pip install -r requirements/dev_lock.txt

lock-deps-dev:
	pip-compile --upgrade --generate-hashes --strip-extras --verbose --output-file requirements/dev_lock.txt requirements/dev.in

lock-deps-prod:
	pip-compile --upgrade --generate-hashes --strip-extras --output-file requirements/prod_lock.txt requirements/prod.in

audit-deps-dev:
	pip-audit --requirement requirements/dev.in

pcau:
	pre-commit autoupdate

# manage.py commands and extras from django_extensions
mm:
	python manage.py makemigrations

mig:
	python manage.py migrate

runs:
	python manage.py runserver

run-plus:
	python manage.py runserver_plus

pre-commit-all:
	pre-commit run --all-files

docs-serve:
	mkdocs serve --dev-addr 127.0.0.1:8002


# Frontend
