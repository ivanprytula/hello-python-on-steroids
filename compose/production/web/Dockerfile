# 0. define an alias for the specific python version used in this file.
FROM python:3.11.5-slim-bullseye as python-base
LABEL maintainer="Ivan Prytula <ivanprytula87@gmail.com>"

# 1.0 Python build stage
FROM python-base as python-build-stage

ARG BUILD_ENVIRONMENT=production

# 1.1 Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg dependencies
  libpq5

# 1.2 Requirements are installed here to ensure they will be cached.
COPY ./requirements .

# 1.3 Create Python Dependency and Sub-Dependency Wheels.
# NB: check this: https://pythonwheels.com/
RUN pip wheel --wheel-dir /usr/src/app/wheels  \
  -r ${BUILD_ENVIRONMENT}.txt


# 2.0 Python 'run' stage
FROM python-base as python-run-stage

ARG BUILD_ENVIRONMENT=production
ARG APP_HOME=/app

# 2.1 Set environment variables
# disables an automatic check for pip updates each time
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

# ensures our console output is not buffered by Docker
ENV PYTHONUNBUFFERED 1
# Python won't try to write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

# 2.1.1 Create non-root user to own/run app
RUN addgroup --system django \
    && adduser --system --ingroup django django


# 2.2 Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  # psycopg2 dependencies
  libpq5 \
  # Translations dependencies
#   gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# 2.3 All absolute dir copies ignore workdir instruction. All relative dir copies are wrt to the workdir instruction
# copy python dependency wheels from python-build-stage
COPY --from=python-build-stage /usr/src/app/wheels  /wheels/

# 2.4 use wheels to install python dependencies
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
  && rm -rf /wheels/

# 2.5 Copy files to be run on containers start up
COPY --chown=django:django ./compose/production/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY --chown=django:django ./compose/production/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker


COPY --chown=django:django ./compose/production/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat


COPY ./compose/production/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower


# 2.6 copy application code to WORKDIR
COPY --from=client-builder --chown=django:django ${APP_HOME} ${APP_HOME}

# 2.7 make django owner of the WORKDIR directory as well.
RUN chown django:django ${APP_HOME}

# 2.8 Switch to the new user
USER django
