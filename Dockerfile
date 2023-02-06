FROM python:3.10-slim-buster

ENV DockerHome=/usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR ${DockerHome}

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt ${DockerHome}
RUN pip install -r requirements.txt

COPY . ${DockerHome}

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:9000"]
