FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /sen
ADD . .
RUN pip install -r /sen/requirements.txt
RUN python3 manage.py makemigrations 
RUN python manage.py migrate
