.ONESHELL:

all: install run_server
.PHONY: all

install:
	echo "Creating virtualenv, installing packages"
	python3 -m venv venv
	. venv/bin/activate
	pip install -r requirements.txt
	
run_server:
	echo "Running django server"
	. venv/bin/activate
	python app/football/manage.py runserver


