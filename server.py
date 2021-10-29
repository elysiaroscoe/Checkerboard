from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<int:num>')
def version2(num):
    return render_template("index.html", num = num)


if __name__=="__main__":
    app.run(debug=True)