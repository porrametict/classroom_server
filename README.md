# The Air Class Project : Server

## Project setup
```
virtualenv env
.\env\Scripts\activate  (for window os)
source venv/bin/activate (for max && linux os)
pip install -r requirement.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createadminuser

```

[comment]: <> (test comment)
<!---

### CollectStatic (for production)
```
python production.py makemigrations
python production.py migrate
python production.py collectstatic
```

-->
### Run Server
```
python manage.py runserver

```
[comment]: <> (python manage.py runsslserver 0.0.0.0:8000)

## login SuperUser
SuperUser was created in createadminuser process.
```
username  : admin
password : password
``` 


 
### Documents
[Django](https://docs.djangoproject.com/en/3.0/).  
[Django rest-framework](https://www.django-rest-framework.org/).
