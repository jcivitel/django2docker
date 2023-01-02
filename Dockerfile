FROM --platform=$BUILDPLATFORM python:3 AS builder
EXPOSE 8000
WORKDIR /app 
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app 
RUN chmod +x /app/start.sh
CMD ["/bin/sh", "/app/start.sh"]