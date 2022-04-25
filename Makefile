
setup:
	poetry install
	poetry run pre-commit autoupdate
	poetry run pre-commit install

run:
	poetry run
