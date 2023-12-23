# python-web-api-fastapi-sqlmodel-mysql-simple

## Description
Creates an api of `dog` for a fastapi project.
Has the ability to query by parameters.

SQLModel only works for fastapi.

## Tech stack
- python
- fastapi
- sqlmodel

## Docker stack
- python:latest
- mariadb:latest

## To run
`sudo ./install.sh -u`
- Get all dogs: http://localhost/dog
  - Schema id, breed, and color

## To stop (optional)
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credit
[SQLModel doc](https://sqlmodel.tiangolo.com/)