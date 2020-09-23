FROM python:latest

WORKDIR /demo

COPY demo.py /demo/demo.py

CMD [ "python", "demo.py" ]