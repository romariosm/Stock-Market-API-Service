FROM python:3.11


WORKDIR /app

RUN pip install pipenv

COPY . /app
RUN pipenv install

CMD ["pipenv", "run", "python", "app.py"]