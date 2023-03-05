
from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request, redirect, jsonify


app = Flask(__name__,template_folder="docs")
bootstrap = Bootstrap5(app)


@app.route("/",methods = ['POST', 'GET'])
def home():

    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)