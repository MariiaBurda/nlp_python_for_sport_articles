# NLP for sport articles
Django project with NLP (Natural Language Processing) in Python for sport articles. 
Used Python 3.7.5, spaCy 2.2.4, Django 3.0.7

### Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Clone

- Clone this repo to your local machine using `https://github.com/MariiaBurda/nlp_python_for_sport_articles/`

### Setup

- If you want to use makefile, skip this step and go to Usage -- Option 2

> create and activate virtual environment first

```shell
$ python3 -m venv venv
$ . venv/bin/activate
```

> install all needed packages

```shell
$ pip install -r requirements.txt
```

### Usage

- Option 1: 

> run django server

```shell
$ python app/football/manage.py runserver
```

- Option 2: use makefile

> run make

```shell
$ make
```
### Test
Use nlp_text.txt as sport article for testing
