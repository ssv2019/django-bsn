# django-bsn
Django-based web app for billiard social network

## Requirements:
1) Python (see requirements.txt)
2) PostgreSQL >= 9.5
3) NGINX

## To start:
1) Rename `bsn/settings.py.example` to `settings.py` and fill all settings according to your machine config
2) Change NGINX config according to `bsn.nginx.conf.example` and restart NGINX
3) Perform migrations to database - from bsn root directory, run:
	```
	python manage.py migrate
	```
4) From bsn root directory, run:
	```
	gunicorn bsn.wsgi
	```
5) Open `localhost:80/static/html/index.html` - there should be blog main page

## TODO:
- [x] Initial files set for git repo
- [ ] Add collectstatic to precommit hook
- [ ] Add makemigrations for all aps to precommit hook (only if new migration is needed!)
