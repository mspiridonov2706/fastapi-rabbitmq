.PHONY: up
up:
	@poetry export -f requirements.txt --output requirements.txt --without-hashes --only main 
	@docker-compose -f docker-compose.yaml up --build
