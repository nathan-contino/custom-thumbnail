FROM python:3
RUN apt-get update
RUN pip install Pillow

COPY ./entrypoint.py /entrypoint.py
ENTRYPOINT ["python", "/entrypoint.py"]
