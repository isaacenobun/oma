FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN apk add --no-cache bash curl busybox-extras
RUN python3 manage.py crontab add

CMD ["sh", "-c", "crond -f & python3 manage.py runserver 0.0.0.0:8000"]