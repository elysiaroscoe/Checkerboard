from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", num=8, numy=8)

@app.route('/<int:num>')
def version2(num):
    return render_template("index.html", num = num, numy=num)

@app.route('/<int:num>/<int:numy>')
def version3(num,numy):
    return render_template("index.html", num = num, numy=numy)


if __name__=="__main__":
    app.run(debug=True)