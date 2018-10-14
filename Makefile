default:
	docker-compose up

run:
	echo NEED_UPDATE

tests:
	docker-compose exec web bash -c "sh run-tests.sh"

enter:
	docker-compose exec web bash

production:
	docker-compose -f docker-compose-production.yml up