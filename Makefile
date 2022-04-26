
setup:
	poetry install
	poetry run pre-commit autoupdate
	poetry run pre-commit install

run:
	SBF_ENVIRONMENT=development poetry run python main.py

test:
	poetry run pytest --cov -vvvvv

docker-run:
	docker-compose up api

docker-test:
	docker-compose run api bash -c "pytest --cov=src --color=yes -vvvv"
