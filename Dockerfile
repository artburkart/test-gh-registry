FROM python:3.8.15-alpine3.16

COPY server.py /server.py
EXPOSE 8080/tcp

CMD ["python3", "/server.py"]
