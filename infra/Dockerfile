FROM python:3.12-alpine as compile-image


RUN apk add --no-cache --update alpine-sdk libffi-dev curl gcc musl-dev openssl-dev cargo

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

FROM python:3.12-alpine as build-image

ENV APP_USER=backend-user \
    HOME=/opt/app \
    PATH="/opt/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR $HOME

RUN adduser -D $APP_USER

USER $APP_USER

COPY --chown=$APP_USER:$APP_USER . .
COPY --from=compile-image --chown=$APP_USER:$APP_USER /opt/venv /opt/venv

