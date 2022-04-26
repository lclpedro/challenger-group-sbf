
setup:
	poetry install
	poetry run pre-commit autoupdate
	poetry run pre-commit install

run:
	SBF_ENVIRONMENT=development poetry run python main.py

test:
	poetry run pytest --cov -vvvvv

run-docker:
	docker-compose up api
