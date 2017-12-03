from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from illustrate import *
import os

os.system('python -m textblob.download_corpora')

@app.route("/", methods=["GET"])
def home_main():
    return render_template('index.html')

@app.route("/tellMeAStory", methods=["GET"])
def storyTime():
    return render_template('example_story.txt')

# The magic endpoint
@app.route("/illustrate", methods=["GET", "POST"])
def illustrate():
    result = genTextMetrics(str(request.form["text_body"]))
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=4007)
