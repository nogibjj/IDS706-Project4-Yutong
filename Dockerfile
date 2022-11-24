FROM python:3.10-bullseye

# ENV FLASK_APP=app
# ENV FLASK_ENV=development
ENV OPENAI_API_KEY=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

RUN mkdir -p /app
COPY ./openai-app /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8080
CMD [ "app.py" ]
ENTRYPOINT [ "python" ]