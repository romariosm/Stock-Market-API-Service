# Stock-Market-API-Service


## Run project
Install docker and docker-compose. [install docker](https://docs.docker.com/engine/install/ubuntu/)
```
docker build -t stock-api .
docker run -dp 3000:3000 stock-api
```

Once app is running Access to: [127.0.0.1:3000/stock/health](http://127.0.0.1:3000/stock/health) to check the service is running.

Send a post to [127.0.0.1:3000/stock/auth](http://127.0.0.1:3000/stock/auth) with name, lastname and email. Then it will return the auth token to access to other endpoints.
```
curl -X POST -H 'Content-Type: application/json' -d '{"name": "test", "lastname":"test", "email":"test@gmail.com"}' http://127.0.0.1:3000/stock/auth
```

Use access token for getting stock info.
```
curl --location 'http://127.0.0.1:3000/stock/stock_info?symbol=AMZN' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4MzQ5OTAxNywianRpIjoiN2YxOTdkOGUtODkxMy00MTNjLWEwZjMtMTMxNzkxMzhlNDIxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InJvbWFAZ21haWwuY29tIiwibmJmIjoxNjgzNDk5MDE3LCJleHAiOjE2ODM0OTk5MTd9.p1GepfFfJv23t38fGnKjMKGVMSOOMzev4pLDgrRg8kE'
```

## CI Pipeline
App is deplyed using Github Actions and AWS sailight. The app is already released [here](aws-lightsail-stock-api.1a1fq64424o82.us-east-2.cs.amazonlightsail.com/stock/health)

## Environment
Change environment modifying from .env file when it is run locally