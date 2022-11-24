# Q&A Web App with OpenAI API

This is a web app that can answer questions driven by OpenAI API. The code is adpoted from [OpenAI quickstart repo](https://github.com/openai/openai-quickstart-python) and [OpenAI quickstart tutorial](https://beta.openai.com/docs/quickstart). It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework.

Follow the instructions below to set up and run the web app.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd openai-app
   ```

4. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

6. Create an environment variables file `.env` with following content

   ```env
   FLASK_APP=app
   FLASK_ENV=development
   OPENAI_API_KEY=
   ```

7. Add your [OpenAI API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

8. Run the app

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).
