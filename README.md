# IDS706-Project4-Yutong
This is the repo for IDS706 course project 4.

OpenAI
https://beta.openai.com/playground/p/default-qa?model=text-davinci-002

### Usage

Build docker image `docker build -t ids706-proj4 .`

Run in docker locally `docker run -p 5000:5000 -t -i ids706-proj4`

Project #4: Continuous Delivery of Flask/FastAPI Data Engineering API on AWS

- Create a Microservice that returns a JSON payload and performs a Data Engineering related task
- Push tested source code to Github and perform Continuous Integration with Github Actions (or similar SaaS Build service)
- Configure Build Server to Deploy Changes on build (Continuous Delivery)
- Create realistic API (reference here: Data Engineering: Chapter 5 aws chapter for pragmatic ai.)
