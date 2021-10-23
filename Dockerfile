FROM python:3.9-alpine
WORKDIR /code

ENV PYTHONUNBUFFERED=1

COPY . .
CMD ["python", "calc.py"]
