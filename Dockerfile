FROM python:3.12

WORKDIR /app

COPY test_app.py .

CMD ["python", "test_app.py"]
