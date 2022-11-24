#!/usr/bin/env python
"""
Flask app for answering question with OpenAI API.
"""

import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    """Index function for Flask web app"""
    if request.method == "POST":
        question = request.form["question"]
        # response1 = openai.Completion.create(
        #     model="text-davinci-002",
        #     prompt=generate_name_animal_prompt(question),
        #     temperature=0.6,
        # )
        response2 = openai.Completion.create(
        model="text-davinci-002",
        prompt=generate_qna_prompt(question),
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
        )
        print(response2)
        print(response2.choices[0].text)
        return redirect(url_for("index", result=response2.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_name_animal_prompt(animal):
    """Add two numbers"""
    return """Suggest three names for an animal that is a superhero.
    
    Animal: Cat
    Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
    Animal: Dog
    Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
    Animal:""" + animal.capitalize() + "Names:"

def generate_qna_prompt(question):
    """Generate q & a prompt for OpenAI"""
    return "I am a highly intelligent question answering bot. \
        If you ask me a question that is rooted in truth, I will give you the answer. \
        If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ: What is human life expectancy in the United States?\nA: Human life expectancy in the United States is 78 years.\n\n\
        Q: Who was president of the United States in 1955?\nA: Dwight D. Eisenhower was president of the United States in 1955.\n\nQ: Which party did he belong to?\nA: He belonged to the Republican Party.\n\n\
        Q: What is the square root of banana?\nA: Unknown\n\nQ: How does a telescope work?\nA: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\n\
        Q: Where were the 1992 Olympics held?\nA: The 1992 Olympics were held in Barcelona, Spain.\n\n\
        Q: How many squigs are in a bonk?\nA: Unknown\n\nQ:" + question + "\nA:"

if __name__ == '__main__':
    app.run()
