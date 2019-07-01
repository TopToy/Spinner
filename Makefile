build:
	./make_scripts/build.sh

docker_build:
	docker build -t spinner:0.1 .

install:
	./make_scripts/install.sh

run:
	./make_scripts/run.sh



