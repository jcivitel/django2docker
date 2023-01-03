FROM --platform=$BUILDPLATFORM python:3 AS builder
EXPOSE 8000
WORKDIR /app
COPY git_clone/* /app/
RUN pip3 install -r requirements.txt --no-cache-dir
COPY start.sh /root/ 
RUN chmod +x /root/start.sh
CMD ["/bin/sh", "/root/start.sh"]