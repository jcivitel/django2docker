FROM --platform=$BUILDPLATFORM python:3 AS builder
EXPOSE 8000
WORKDIR /app
COPY git_clone /app
COPY .env /app/
RUN pip3 install -r requirements.txt
COPY start.sh /root/ 
RUN chmod +x /root/start.sh
CMD ["/bin/sh", "/root/start.sh"]