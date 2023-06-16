requirements:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt



migrate:
	python manage.py migrate

run:
	python manage.py runserver



clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf media/*

reset:
	rm -rf db.sqlite3
	make clean
	make migrate
