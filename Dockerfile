# bull base image
FROM python:3.9.10-slim-buster

RUN pip install --upgrade pip

RUN python3 -m venv /opt/venv

# Copy project
COPY . /app
# Set work directory
WORKDIR /app

RUN /opt/venv/bin/pip install -r requirements.txt && \
    chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]





