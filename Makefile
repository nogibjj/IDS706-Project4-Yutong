install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	echo "Not implemented yet"
	#python -m pytest -vv test_*.py

format:	
	black *.py src/*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py src/*.py

refactor: format lint

push:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 148653226728.dkr.ecr.us-east-1.amazonaws.com
	docker build -t ids706-proj4 .
	docker tag ids706-proj4:latest 148653226728.dkr.ecr.us-east-1.amazonaws.com/ids706-proj4:latest
	docker push 148653226728.dkr.ecr.us-east-1.amazonaws.com/ids706-proj4:latest

all: install lint test