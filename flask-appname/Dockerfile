FROM python:latest
MAINTAINER Farkhod Sadykov

## Copy everything to image folder app
WORKDIR /app
COPY . /app

## Expose the port 5000
EXPOSE 5000

## Install all requirements to the docker image
RUN python -m pip install -r /app/requirements.txt
ENTRYPOINT ["python", "/app/app.py"]
