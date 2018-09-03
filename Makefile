default:
	docker build . -t docker-django
	docker run --rm -p 8000:8000 -v `pwd`:"/app" -w "/app" -it docker-django bash -c "sh run-django.sh"