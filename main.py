from flask import Flask, render_template, jsonify
import requests
import os

app = Flask(__name__)


@app.route("/")
def index():
    #  Get a random quote from the Quotable REST API
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        quote_data = response.json()
        quote = quote_data["content"]
        author = quote_data["author"]
    else:
        quote = "Error fetching quote"
        author = "Unknown"

    return render_template("index.html", quote=quote, author=author)


@app.route("/new_quote")
def new_quote():
    #  Get a new random quote from the Quotable REST API
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        quote_data = response.json()
        quote = quote_data["content"]
        author = quote_data["author"]
    else:
        quote = "Error fetching quote"
        author = "Unknown"

    #  Return the new quote as JSON
    return jsonify({"quote": quote, "author": author})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
