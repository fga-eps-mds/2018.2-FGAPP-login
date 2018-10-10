default:
	docker-compose up

run:
	echo NEED_UPDATE

production:
	docker-compose -f docker-compose-production.yml up