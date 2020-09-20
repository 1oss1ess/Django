# API-Bulgarian-Prime-Minister
Apply Scrapy to collect information from prime ministers and Django REST to return prime minister.


&nbsp;
&nbsp;


## To Run
>- In directory myparliament/
>- python manage.py migrate
>- python manage.py makemigrations
>- python manage.py createsuperuser --username test --email test@test.com
>- python manage.py drf_create_token test
>- In directory myparliament/crawling/
>- scrapy crawl parliament
>- In directory myparliament/
>- python manage.py runserver

***Warning***: Few python packages required: 
- pip install requirements.txt


&nbsp;
&nbsp;


## Crawling
#### 1. items.py
- Define model for scraped items. Python objects that define key-value pairs
#### 2. parliament.py
- Extract data from web site
- In method parse we collecting MPs links and parsing the latter with the parse_item method
- In method pars_item we collecting data (key-value) for each minister
#### 3. pipelines.py
- After an item has been scraped by a spider, it is sent to the Item Pipeline
- We define several method to process raw data (item)
- After item has been formatted we save the data in our model


&nbsp;
&nbsp;


## API
#### 1. serializers.py
- we need to specify how our data well be serialized
#### 2. views.py 
- in our view we use ParliamentListView(generics.ListAPIView) to list all MPs
- ParliamentDetailView(generics.RetrieveAPIView) this view return one MP
- we have ParliamentSearchListView(generics.ListAPIView) that allows you to search MPs by name
#### 3. urls.py
- in http://127.0.0.1:8000/list/ we return all MPs
- in http://127.0.0.1:8000/list?&pp=ПТС we list all MPs how is in that party
- in http://127.0.0.1:8000/list?&dob=19761212 return all MPs how was born on that date
- in http://127.0.0.1:8000/mp/1/ return MP with id=1 if in tha DB
- in http://127.0.0.1:8000/search?q=/Гого Светкавица Виелицата this will return that MP if in the DB
