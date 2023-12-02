FROM python:3
WORKDIR /app
COPY . .
# mount the secret in the correct location, then run pip install
RUN --mount=type=secret,id=my_secret,required cat /run/secrets/my_secret > /app/secrets.txt
RUN --mount=type=secret,id=aws_public_key cat /run/secrets/aws_public_key > /app/aws_public_key
RUN --mount=type=secret,id=aws_private_key cat /run/secrets/aws_private_key > /app/aws_private_key
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=mypython.py
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
CMD ["flask", "run"]