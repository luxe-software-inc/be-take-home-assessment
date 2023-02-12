.PHONY : build lint test coverage migrations run
build:
	docker-compose build

lint:
	docker-compose run --rm kimberlite_backend sh -c "flake8"

test:
	docker-compose run --rm kimberlite_backend sh -c "python -m coverage run manage.py test && coverage report -m"

coverage: 
	docker-compose run --rm kimberlite_backend sh -c "python -m coverage run ./manage.py test && coverage report -m"

migrations:
	docker-compose run --rm kimberlite_backend sh -c "python manage.py makemigrations"

runmigrations:
	docker-compose run --rm kimberlite_backend sh -c "python manage.py migrate"

run:
	docker-compose up
