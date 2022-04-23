FROM python:3.9
LABEL maintainer="mikhail_rozov@vk.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 8080
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
