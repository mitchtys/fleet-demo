FROM python:alpine3.8
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt

EXPOSE 80

CMD python3 app.py
