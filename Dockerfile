# Use an official Python runtime as a parent image
FROM python:3.12-slim

RUN apt-get update && apt-get install -y curl build-essential

WORKDIR /challenge


COPY ./requirements.txt /challenge/tmp/requirements.txt
COPY ./requirements.dev.txt /challenge/tmp/requirements.dev.txt
COPY ./app /challenge/app
COPY ./data /challenge/data


# by default we don't running our dockerfile in development mode
ARG DEV="false"


RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install --no-cache-dir -r /challenge/tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install --no-cache-dir -r /challenge/tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /challenge/tmp


EXPOSE 8080

# Run app.py when the container launches
CMD ["/py/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]