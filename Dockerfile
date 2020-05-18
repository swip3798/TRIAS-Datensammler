FROM debian:latest

RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-mysqldb
RUN apt-get autoclean
RUN pip3 install --upgrade pip

WORKDIR /TriasMiner

COPY . /TriasMiner

RUN pip3 --no-cache-dir install -r requirements.txt
RUN python3 sensitive.py

EXPOSE 7777

ENTRYPOINT [ "python3" ]
CMD ["main.py"]