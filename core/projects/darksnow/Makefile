say_hello:
	echo "Hello"

APP_NAME = 'default'


build-darksnow:
	cd ${CURDIR}/build/application && \
	cp -r ${CURDIR}/core/app ${CURDIR}/build/application && \
    cp ${CURDIR}/core/prestart.sh ${CURDIR}/build/application/prestart.sh && \
	docker-compose build
	rm -rf ${CURDIR}/build/application/app && \
	rm -rf ${CURDIR}/build/application/prestart.sh

run: build-darksnow
	cd ${CURDIR}/build && \
	docker-compose up

down:
	cd ${CURDIR}/build && \
	rm -rf ${CURDIR}/build/application/main.py && \
	docker-compose down

deploy:
	cd ${CURDIR}/build && \
	cp ${CURDIR}/core/main.py ${CURDIR}/build/application/main.py && \
	docker-compose build release
	docker push 691016621062.dkr.ecr.us-east-1.amazonaws.com/myapp

clean:
	cd ${CURDIR}/build && \
	rm -rf ${CURDIR}/build/application/app
	echo $APP_NAME
	docker stop $(APP_NAME)
	docker rm $(APP_NAME)
	#docker image rm 691016621062.dkr.ecr.us-east-1.amazonaws.com/myapp
	docker rmi -f $(APP_NAME)


login:
	cd ${CURDIR}/ && \
	echo ${PWD} && \
	$$(aws ecr get-login --no-include-email)

logout: 
	docker logout https://691016621062.dkr.ecr.us-east-1.amazonaws.com

remove_all_images:
				docker rmi $(docker images -a -q)
