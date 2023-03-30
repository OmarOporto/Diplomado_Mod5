FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /code/
WORKDIR /code
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

EXPOSE 8000
COPY . /code/
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
