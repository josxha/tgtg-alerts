FROM python:3

ENV TGTG_EMAIL = ""
ENV TGTG_ACCESS_TOKEN = ""
ENV TGTG_REFRESH_TOKEN = ""
ENV TGTG_USER_ID = ""
ENV TGTG_COOKIE = ""
ENV INTERVAL = "60"

WORKDIR /app
COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "tgtg_alerts.py"]
