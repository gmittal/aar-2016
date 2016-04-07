from flask import Flask, render_template
# import illustrate
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home_main():
    return render_template('index.html')

# The magic endpoint
@app.route("/illustrate", methods=["POST"])
def illustrate():
    return "hello"

if __name__ == "__main__":
    app.run()
