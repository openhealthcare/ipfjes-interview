[![Stories in Ready](https://badge.waffle.io/drcjar/ipfjes-interview.png?label=ready&title=Ready)](https://waffle.io/drcjar/ipfjes-interview)
This is IPFJES interview - the

### Development install

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

Project documentation: https://github.com/drcjar/ipfjes

Bug tracker: https://github.com/drcjar/ipfjes-interview/issues

### Deployment details

Deployment via scripts here: https://github.com/openhealthcare/elcid-deployment/tree/ipfjes

Install as per instructions there, then:

```
fab server_setup
```

Deploytment scripts at `(elcid-setup) drcjar@ipfjes:~/Documents/elcid-deployment$`
Production application code at `(ipfjes-interview) drcjar@ipfjes:~/Documents/src/ipfjes-interview$`
