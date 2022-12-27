FROM python:3.10

WORKDIR /exchange

COPY ./requirements.txt /exchange/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /exchange/requirements.txt

COPY ./app /exchange/app

COPY ./utils /exchange/utils

COPY ./run.py /exchange/run.py

CMD ["python", "-u", "run.py"]
