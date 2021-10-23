FROM python:3.9-alpine
WORKDIR /code

COPY . .
CMD ["python", "calc.py"]
