FROM python:3.12.2-alpine

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY api.py .

CMD [ "python", "api.py" ]