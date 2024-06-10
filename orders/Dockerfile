FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app

RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

#COPY orders/orders /app

#CMD ["python3", "orders/manage.py", "runserver", "0.0.0.0:8000"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "orders.wsgi:application"]