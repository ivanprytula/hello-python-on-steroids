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

## Setup

### Django "classic" set of commands

```shell
django-admin startproject <django_project> .
python manage.py startapp <app_name>
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

pip-compile --upgrade --generate-hashes --output-file requirements/dev_lock.txt requirements/dev.in
pip-compile --upgrade --generate-hashes --output-file requirements/prod_lock.txt requirements/prod.in

```

## Used resources

### Tutorials

- <https://djangoforbeginners.com/initial-setup/>
- ...

### Documentation, cheatsheet

- <https://ccbv.co.uk/>
- ...

### People to read

- [jacobian, co-creator of Django](<https://jacobian.org/>)
- ...
