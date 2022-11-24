FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip3 install poetry
RUN poetry config virtualenvs.create false && \
  poetry install --no-interaction --no-root --no-dev && \
  rm -rf ~/.cache/pypoetry && \
  rm -rf ~/.config/pypoetr

COPY . .

RUN poetry run python manage.py makemigrations && \
    poetry run python manage.py migrate && \
    poetry run python manage.py collectstatic --no-input


CMD poetry run daphne -b 0.0.0.0 -p 8080 turbiditech.asgi:application