# bull base image
FROM python:3.9.10-slim-buster

RUN python -m venv /opt/venv

RUN pip install --upgrade pip

# Copy project
COPY . /app
# Set work directory
WORKDIR /app

RUN /opt/venv/bin/pip install -r requirements.txt && \
    chmod +x entrypoint.sh && \
    chmod +x collectstatic.sh

CMD ["/app/entrypoint.sh"]
CMD ["/app/collectstatic.sh"]





