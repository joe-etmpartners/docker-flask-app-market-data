FROM python:3
WORKDIR /app
COPY . .
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=mypython.py
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
ENV [variable-name]=[default-value]
ENV AWS_DEFAULT_REGION: "us-east-2b"
ENV AWS_ACCESS_KEY_ID: "AKIARD3WOPAPDTY4N6F7"
ENV AWS_SECRET_ACCESS_KEY: "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"
EXPOSE 5000
CMD ["flask", "run"]