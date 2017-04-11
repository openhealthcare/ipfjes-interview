This is IPFJES interview - the 

To get started

Prerequisites:

* Installed Postgres (server and header packages)
* Virtualenvwrapper

```
git clone git@github.com:drcjar/ipfjes-interview
cd ipfjes-interview
mkvirtualenv -a $PWD ipfjes-interview
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
