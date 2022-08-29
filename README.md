# test-webstie
a simple test website with django

# parameters that you need to change at test-webstie/mywebsite/mywebsite/settings.py 
```python3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_db', # change
        'USER': 'root', # change
        'PASSWORD': 'password', # change
        'HOST': '172.0.0.1', # change
        'PORT': '3306' # change
        #'OPTIONS':{
        #    'init_command': "SET sql_mode='STRICT_TRANS_TABELS'"
        #}
    }
}
```

# drop-in copy-paste prep for debian 11
```shell
sudo apt update
sudo apt install libmariadb-dev
pip3 install django
pip3 install mysqlclient
pip3 install -U pip
```
# drop in copy-paste run on project direcotry
```shell
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
