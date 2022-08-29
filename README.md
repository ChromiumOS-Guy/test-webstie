# test-webstie
a simple test website with django

# drop-in copy-paste prep for debian
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
