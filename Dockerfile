# syntax=docker/dockerfile:1

FROM python:3.10

# create a directory for the app
RUN mkdir /app

# copy all the files to the container
COPY ./app /app
COPY pyproject.toml /app

WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
ENV MONGO_URI="mongodb+srv://userReadOnly:7ZT817O8ejDfhnBM@minichallenge.q4nve1r.mongodb.net/minichallenge"

EXPOSE 8080

# Install poetry
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# run the command
ENTRYPOINT ["poetry", "run"]
CMD ["python", "main.py"]


