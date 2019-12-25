FROM python:3.6

# 创建工作目录
RUN mkdir /demo_django

#设置工作目录
WORKDIR /demo_django

#将当前目录加入到工作目录中
ADD . /demo_django

RUN pip3 install -r requirements.txt

#对外暴露端口
EXPOSE 80 8080 8000 5000

#设置环境变量
ENV SPIDER=/demo_django