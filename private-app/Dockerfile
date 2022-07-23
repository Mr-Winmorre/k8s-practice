FROM python:3.10.4

WORKDIR /private

COPY ./requirements.txt /private/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /private/requirements.txt

COPY ./app /private/app

CMD ["uvicorn", "app.main:app","--host","0.0.0.0", "--port", "80"]