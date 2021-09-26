# Nuxt Django Rest Docker

Universal applicartion supporting SSR and PWA build with Nuxt, Django and Docker

Deployement on AWS

For more info, see tutorial https://blog.florianbgt.com/Nuxt_Django_from_dev_to_AWS_Part1

## Setup
Modify the following code with your email provider info if you want email sent to user (defaut is logged in the console)

## Usage

1) Clone this repository

2) Run `docker-compose run api migrate` to migrate the database

3) Run `docker-compose run api createsuperuser` to create a super user and have access to Django admin page

4) Run `docker-compose up` to spin up the containers

Nuxt app will be serve at http://localhost:3000

Django API will be serve at http://localhost:8000