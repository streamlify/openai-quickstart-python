import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )


#if __name__ == '__main__':
#    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
