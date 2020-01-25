.PHONY: build

APP_NAME='default'

all: build

test-poc :
	cd ${CURDIR}/core/pocs/automatic-item-classification/build && \
	docker-compose -f docker-compose.${ENV}.yaml up

run-darksnow:
ifeq "$(APP_NAME)" "darksnow"
	cd ${CURDIR}/core/projects/darksnow/ && \
	make run
else ifeq "$(APP_NAME)" "others"
	@echo please use others microservices here
else
	@echo please provide app name
endif

build-learning :
ifeq "$(APP_NAME)" "darksnow"
	cd ${CURDIR}/tools/learning/darksnow && \
	make CreateInfra
else ifeq "$(APP_NAME)" "others"
	@echo please use others microservices here
else
	@echo please provide app name
endif

destroy-learning :
ifeq "$(APP_NAME)" "darksnow"
	cd ${CURDIR}/tools/learning/darksnow && \
	make DeleteInfra
else
	@echo please provide app name
endif


run-learning :
ifeq "$(APP_NAME)" "darksnow"
	cd ${CURDIR}/core/learning/darksnow && \
	make deploy
	rm -rf ${CURDIR}/core/learning/darksnow/build/application/main.py
	docker image rm 691016621062.dkr.ecr.us-east-1.amazonaws.com/myapp
else
	@echo please provide app name
endif

login:
	$$(aws ecr get-login --no-include-email)

