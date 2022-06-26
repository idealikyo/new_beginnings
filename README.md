# New Beginnings
---
# Overview

A participant registry microservice using Django REST framework that supports adding, updating, removing and retrieving personal information about participants in New Beginnings.

# Requirements

* Python 
* Django 
* djangorestframework
* django-phonenumber-field
* django-phonenumbers

# Setup

Make directory

    mkdir new_beginnings
    
Enter folder

    cd new_beginnings

Clone git repository

    git clone https://github.com/idealikyo/new_beginnings.git

Install using `pip`...

    pip install  -r requirements.txt

Execute migrate

    ./manage.py migrate
    
Create superuser

    ./manage.py createsuperuser
    
Run server

    ./manage.py runserver
    
    
# Test API

## Create test data in admin site

Open and log in the Admin site in the browser at `http://127.0.0.1:8000/admin` as the superuser created above. Create or edit Participants for the test.

![image](https://user-images.githubusercontent.com/29779370/175809357-ce4d237b-e2b0-407b-a90c-beb70196488b.png)

## Test API in the browser

### Get all participants and create a new one

Open `http://127.0.0.1:8000/participant/` in the browser. All participants in New Beginnings are shown in JSON format. Click GET button to refresh. 

Write participant information (name, date_of_birth, phone_number, address) in JSON format in Content field and click PUT button to add a new participant.

![image](https://user-images.githubusercontent.com/29779370/175809766-ce1e4f53-5c7b-4368-8365-5ff02ba622b0.png)

### Get a participant by reference_number, update and remove the participant information

Open `http://127.0.0.1:8000/participant/<str:reference_number>` in the browser. The found participant information is shown in JSON format if exists. Click GET button to refresh.

Write participant information (name, date_of_birth, phone_number, or address) in JSON format in Content field and click POST button to update the found participant information.

Click DELETE button to remove the found participant.

![image](https://user-images.githubusercontent.com/29779370/175810766-f2c27214-1fe9-45a3-9f04-d54b27308293.png)


## Test API using command line tools such as [`curl`](https://curl.haxx.se/)

### Get all participants information in New Beginnings

    $ curl -i -X GET http://127.0.0.1:8000/participant/
    [{"name":"Xiang Li1","date_of_birth":"2022-01-05","phone_number":"+12125552368","address":"Address2","reference_number":"XL-001"},{"name":"TEST22","date_of_birth":"2022-01-05","phone_number":"+12125552368","address":"Address1","reference_number":"TES-003"},{"name":"TEST3","date_of_birth":"2022-01-05","phone_number":"+12125552368","address":"Address1","reference_number":"TEST3-8"}]
    
### Add a new participant information

    $ curl -i -X PUT -H 'Content-Type: application/json' -d '{"name":"TEST","date_of_birth":"2022-01-05","phone_number":"+12125552368","address":"Address1"}' http://127.0.0.1:8000/participant/
    
    
### Get a participant information by reference number

    $ curl -i -X GET http://127.0.0.1:8000/participant/TEST3-8/
    {"name":"TEST3","date_of_birth":"2022-01-05","phone_number":"+12125552368","address":"Address1","reference_number":"TEST3-8"}
    
### Update a participant information by reference number

    $ curl -i -X POST -H 'Content-Type: application/json' -d '{"name":"TEST","phone_number":"+12125552369","address":"Address3"}' http://localhost:8000/participant/TEST3-8/
    
### Remove a participant information by reference number

    $ curl -i -X DELETE http://127.0.0.1:8000/participant/TEST3-8/
    
# Note

Django REST framework is based on Django's class-based views. If you are a Django developer and familiar with views, forms, validator, QuerySet and urls, Django REST framework is an excellent choice. It also provides a Web browsable API for developers and an Authentication solution.

In this project, I keep the functions as simple as possible. When add or update participants, it has only basic validations based on the definition of field. It could be improved in `ParticipantSerializer` by adding particular field validations based on the client's requirements. I also assume reference number is combined by participant name and id, not using extra API to generate.

For Django REST framework, it is easy to add authentication in `settings.py`. For example, anonymous request is readonly. To edit participants, the proper account info should be contained in the request.

Considering New Beginning hopes to enrol 100,000 participants over five years, it is better to add filters and search function for the API, not only by reference number. And you can also set the pagination style in `settings.py` to control the response size.

