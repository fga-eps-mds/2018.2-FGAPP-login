default:
	docker build . -t docker-django
	docker run --rm -p 8000:8000 -p 587:587 -v `pwd`:"/app" -w "/app" --name login-microservice -it docker-django bash

run:
	docker build . -t docker-django
	docker run --rm -p 8000:8000 -v `pwd`:"/app" -w "/app" --net=backend --name login-microservice -d docker-django bash -c "sh run-django.sh"

production:
	make build-production
	make run-production

build-production:
	docker build -t login-microservice/production -f production.Dockerfile .
	
run-production:
	docker run -p 8000:8000 --name login-microservice-production login-microservice/production