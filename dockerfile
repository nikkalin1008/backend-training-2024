FROM python:3.10
WORKDIR /tmp

COPY ./app/requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

WORKDIR /mnt/app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]