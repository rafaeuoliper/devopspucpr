FROM python:3.9-slim

WORKDIR /app

COPY conversor.py .

RUN pip install -r requirements.txt  

CMD ["python", "conversor.py"]
