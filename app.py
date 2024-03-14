from flask import request, jsonify, Flask
import random as rk
import csv

dicionario=[*csv.DictReader(open('planilha.csv'),delimiter=';')]

print(dicionario)

app = Flask(__name__)

@app.route("/")

def home():
    html = """
    <p> <a href="/input">Visualizar os dados</a> </p>
    <p> <a href="/output">Receber</a> </p>

"""
    return html

@app.route("/input")

def input():
    return jsonify(dicionario)

@app.route("/output", methods=['GET', 'POST'])

def output():
    return jsonify(dicionario)

if __name__ == '__main__':
    app.run(debug=True)