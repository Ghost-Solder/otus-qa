FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN apk add --no-cache chromium chromium-chromedriver
RUN pip install -U pip
RUN pip install -r requirements.txt

ENV PATH="/usr/lib/chromium-browser:${PATH}"
ENV CHROME_BIN="/usr/lib/chromium/chrome"

COPY . .

ENTRYPOINT ["pytest"]
