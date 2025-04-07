from flask import Flask, request, render_template
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        gender = request.form.get("gender")
        hair_style = request.form.get("hair_style")
        hair_color = request.form.get("hair_color")
        expression = request.form.get("expression")
        emotion = request.form.get("emotion")
        era = request.form.get("era")

        prompt = (
            f"A portrait of {gender} with {hair_style}, {hair_color} hair, "
            f"{expression} expression, looking {emotion}, in {era} style."
        )

        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            n=1
        )

        image_url = response.data[0].url
        print("Üretilen görsel:", image_url)
        return render_template("index.html", image_url=image_url)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)