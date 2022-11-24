FROM python:3.10-bullseye

ENV FLASK_APP=app
# ENV FLASK_ENV=development
ENV OPENAI_API_KEY=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

RUN mkdir -p /app
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8080
CMD [ "test.py" ]
ENTRYPOINT [ "python" ]
# CMD ["python", "/app/test.py"]