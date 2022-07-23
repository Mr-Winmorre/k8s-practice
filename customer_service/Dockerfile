FROM python:3.10

WORKDIR /customer

COPY ./requirements.txt /customer/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /customer/requirements.txt

COPY ./app /customer/app

CMD ["uvicorn", "app.main:app","--host","0.0.0.0", "--port", "8009"]