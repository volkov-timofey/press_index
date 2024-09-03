#Makefile

install:
	poetry install
	
lint: # run_linter
	poetry run flake8 connect, db, engine, hubs
	
build:
	./build.sh

makemigrations:
    poetry run press_index_admin/manage.py makemigrations

migrate:
    poetry run press_index_admin/manage.py migrate

createsuperuser:
    poetry run press_index_admin/manage.py createsuperuser

run_admin:
	poetry run python press_index_admin/manage.py runserver

django: makemigrations migrate createsuperuser

start:
    poetry run python engine/start.py