FROM python:3.9-slim

#ENV FLASK_APP=$FLASK_APP
#ENV FLASK_ENV=$FLASK_ENV
#ENV APP_SETTINGS=$APP_SETTINGS
#ENV DDB_RCU=$DDB_RCU
#ENV DDB_WCU=$DDB_WCU
#ENV S3_PHOTO_BUCKET=$S3_PHOTO_BUCKET
#ENV COGNITO_POOL_ID=$COGNITO_POOL_ID
#ENV COGNITO_CLIENT_ID=$COGNITO_CLIENT_ID
#ENV COGNITO_CLIENT_SECRET=$COGNITO_CLIENT_SECRET

# Download latest listing of available packages:
RUN apt-get -y update
# Upgrade already installed packages:
RUN apt-get -y upgrade
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
RUN pip3 install -r requirements.txt
ADD . /app
EXPOSE 80
RUN chmod +x ./entrypoint.sh
#CMD python3 -m http.server 8000
#ENTRYPOINT ["sh", "entrypoint.sh"]
CMD ["sh", "entrypoint.sh"]