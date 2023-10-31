# SystematicFarming

Web Application for a farmers that display systematic farming instruction & guidelines in our local languages. Feature includes a information about a crop cultivation, disease of a plant, farming instruments and natural fertilizers.

# Steps to run a application :

# Step 1 :

Download & Install a python 3.10 or later versions using a below link and set a environment variables.

https://www.python.org/downloads/

Download a mysql and install it. follow the guidelines in a youtube link

https://youtu.be/eq-e_n7lm2M

# Step 2 :

Go to command prompt and run the following commands one by one.

pip install Django

pip install mysql-connector-python

# Step 3 :

Open a mysql and run the below command for create a database.

create database systematicfarming;

# Step 4:

Go to SystematicFarming folder and open a settings.py file.

Change a user name and password in the database to your username and password of mysql.

DATABASES = {

'default': {

'ENGINE': 'django.db.backends.mysql',

'NAME': 'systematicfarming',

'USER':'root', ----> replace with ur username

'PASSWORD':'root', ----> replace with your password 
} }

# Step 5 :

Open a command prompt and go to manage.py location. run the below commands one by one.

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

copy the url like this shown in ur command prompt & paste in ur browser.

http://127.0.0.1:8000/

Now we successfully run a web application.
