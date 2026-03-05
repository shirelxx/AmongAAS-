FROM python:3.10

RUN apt-get update

COPY . /postgres_python

WORKDIR /postgres_python

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "db/__init__.py"]