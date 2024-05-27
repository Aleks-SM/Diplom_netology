FROM python:3.10

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /usr/src/app
RUN pip install --upgrade pip stuptools
RUN pip install -r requirements.txt

COPY . /usr/src/app

CMD ["python3", "manage.py", "reunserver", "0.0.0.0:800"]