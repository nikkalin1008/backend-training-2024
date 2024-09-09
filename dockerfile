FROM python:3.10
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /app/backend-training/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]