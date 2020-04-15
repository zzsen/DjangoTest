FROM python:3.8-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
EXPOSE 8081