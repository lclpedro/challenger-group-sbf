# SBF Group API

## Required Apps
Operational System: Linux or MacOS
Python version: 3.9+
Poetry

Or

Docker Service

## Execution Service Local - To development
1. Execute setup (is required poetry)
```shell
> make setup
```
2. Execute application
```shell
> make run
```
3. For execute tests with covage code.
```shell
> make test
```
## Execution service with docker.

```shell
> make run-docker
```

## Docker application to production service.
The image Dockerfile in project, is to use of the application in production.
For test image local, must run the commands

```shell
docker build . -t group_sbf:latest
docker run -p 8080:8080 --name group_sbf_api group_sbf
```

## Application service API
To access documentation API. Access with running application:

http://localhost:8080/docs

## Design Archtecture API Service
![Design architecture application service](https://user-images.githubusercontent.com/19912630/165411553-49c92f33-f974-4ccc-b724-b3982a491d45.png)

Features:
    - ProductMock: Today is product mock. But, you can connect your database, plugged in repository class with mantainer contracts..
    - ExternalAPIQuotes: Using for test: https://docs.awesomeapi.com.br/api-de-moedas
