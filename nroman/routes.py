from nroman import app
from utils.romannumber import RomanNumber
from flask import jsonify

@app.route("/")
def index():
    return "Funcionando..."

@app.route('/toroman/<valor>')
def to_roman(valor):
    resp = {'correct': False}

    try:
        valor = int(valor)
    except: 
        resp['message']='Valor incorrecto'
        return jsonify(resp)

    nr = RomanNumber(valor)
    resp['correct'] = True
    resp['result'] = {'arabigo': valor, 'romano': str(nr)}
    return jsonify(resp)
