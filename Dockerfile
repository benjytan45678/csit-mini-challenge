# syntax=docker/dockerfile:1

FROM python:3.10

# create a directory for the app
RUN mkdir /app

# copy all the files to the container
COPY ./app /app
COPY pyproject.toml /app

WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

# Install poetry
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

EXPOSE 8080

# run the command
ENTRYPOINT ["poetry", "run"]
CMD ["python", "main.py"]
