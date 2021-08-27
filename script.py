from flask import Flask, render_template
# render template access an html file stored somewhere in our python app that dispolays html
# of the requested URL

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
