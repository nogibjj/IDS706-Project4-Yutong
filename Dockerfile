FROM python:3.10

WORKDIR /app

EXPOSE 5000
ENV FLASK_APP=app.py

COPY ./openai-app /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "flask" ]
CMD [ "run", "--host", "0.0.0.0" ]

# FROM python:3.10

# WORKDIR /app

# EXPOSE 5000
# ENV FLASK_APP=app.py

# COPY requirements.txt ./
# COPY app.py ./

# RUN pip install -r requirements.txt

# ENTRYPOINT [ "flask"]
# CMD [ "run", "--host", "0.0.0.0" ]
