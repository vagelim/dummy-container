FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
COPY . /app
RUN apt-get update -y && apt-get install -y python3 python3-pip dnsutils
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]