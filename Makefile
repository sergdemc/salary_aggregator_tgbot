
start-mongo:
	docker-compose up -d --build --remove-orphans

stop-mongo:
	docker-compose stop

down-mongo:
	docker-compose down --volumes --remove-orphans

requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes --with dev

install:
	pip install -r requirements.txt

isort:
	isort salary_aggregator bot.py data_loader.py

selfcheck:
	poetry check
