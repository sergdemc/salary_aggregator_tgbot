
start-mongo:
	docker-compose up -d --build --remove-orphans

stop-mongo:
	docker-compose stop

down-mongo:
	docker-compose down --volumes --remove-orphans

start-bot:
	python bot.py

stop-bot:
	pkill -f "python bot.py"

start_db_loader:
	python data_loader.py

load-data: start-mongo start_db_loader

test: start-mongo
	pytest -vv

requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes --with dev

install:
	pip install -r requirements.txt

isort:
	isort salary_aggregator bot.py data_loader.py

selfcheck:
	poetry check
