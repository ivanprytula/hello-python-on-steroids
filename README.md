# Hello Python on steroids

Yet (my) another mega project about Python and Django DX.

  > Software development is more than just writing code (c)

---

  > Use the `--help` option, programmer (c)

---

TOC

- [Hello Python on steroids](#hello-python-on-steroids)
  - [Features overview](#features-overview)
  - [Setup](#setup)
    - [Django "classic" set of commands](#django-classic-set-of-commands)
  - [Used resources](#used-resources)
    - [Tutorials](#tutorials)
    - [Documentation/cheatsheet](#documentation-cheatsheet)
    - [People to read](#people-to-read)

## Features overview

### Best Practices

- [Environs](https://github.com/sloria/environs) - Used for managing environment variables
- [Docker](https://www.docker.com/) - Docker Compose for development and a multi-stage Dockerfile for production ready Docker image
- [Pip Tools](https://github.com/jazzband/pip-tools/) - Used to maintain python requirements
- [Just](https://github.com/casey/just) - Popular tool for running common commands in containers (`make` equivalent)
- `make` - with 'classic' Makefile for commands within virtualenv

### Popular Python and Django Packages

- [Django 4.2](https://www.djangoproject.com/) - Latest version of Django
- [Celery](http://docs.celeryproject.org/) - Most popular task runner for running asynchronous tasks in the background
- [Custom User Model][custom_user_model] - Custom user model so that the user model can be easily extended
- [Django Allauth](http://www.intenct.nl/projects/django-allauth/) - The most popular package for adding authentication
  workflows to a Django project

### Python Testing Tools

- [Pytest](https://docs.pytest.org/) - The most popular Python test runner in the Python community
- [Pytest Django](https://pytest-django.readthedocs.io/en/latest/index.html) - A Django plugin for Pytest
- [Pytest-cov](https://pytest-cov.readthedocs.io) - Adds code coverage to tests
- [pre-commit](https://pre-commit.com/) - A framework for managing and maintaining multi-language pre-commit hooks

### Code Quality, Formatting, and Linting Tools

- [Black](https://black.readthedocs.io/en/stable/) - Automatic Python code formatting
- [Ruff](https://github.com/charliermarsh/ruff) - Extra Python linting and lighting fast because it's written in Rust!
- [Mypy](http://mypy-lang.org/) - Python Type checking
- [typeguard](https://pypi.org/project/typeguard/) - Run-time type checker for Python
- [dj Lint](https://djlint.com/) - Automatic Django HTML template formatting and linting
- [Django Debug Toolbar](https://github.com/jazzband/django-debug-toolbar) - A toolbar for debugging and
  optimizing Django queries
- django-silk
- [Bandit](https://bandit.readthedocs.io/) - Automatic security checking
- [pip-audit](https://pypi.org/project/pip-audit/) - tool for scanning Python environments for known vulnerabilities
- [Stylelint](https://stylelint.io/) - Automatic Sass formatting and linting
- [Eslint](https://eslint.org/) - Automatic Javascript formatting and linting

## Setup

### Django "classic" set of commands

```shell
django-admin startproject <django_project> .
python manage.py startapp <app_name>

export SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
cat > .env <<EOF
DEBUG=on
SECRET_KEY='$SECRET_KEY'
DATABASE_URL=postgres://postgres:@db:5432/postgres
INTERNAL_IPS=127.0.0.1,0.0.0.0
EOF


python manage.py migrate
python manage.py runserver
python manage.py makemigrations
```

```shell
tree -a -L 2 -I .venv
npm run build
npm run dev
```

## Used resources

### Tutorials

- <https://djangoforbeginners.com/initial-setup/>
- <https://www3.nd.edu/~zxu2/acms60212-40212/Makefile.pdf>
- <https://cheat.readthedocs.io/en/latest/index.html>
- <https://fabien.herfray.org/posts/mastering-postgres-indexes-in-10-minutes/>
- ...

### Documentation, cheatsheet

- <https://ccbv.co.uk/>
- ...

### People to read

- [jacobian, co-creator of Django](<https://jacobian.org/>)
- ...
