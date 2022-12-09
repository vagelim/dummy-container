FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && apt-get install -y python3 python3-pip dnsutils
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY app.py /app
ENTRYPOINT ["python3"]
CMD ["app.py"]