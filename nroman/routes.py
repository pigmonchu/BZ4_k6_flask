from nroman import app
from utils.romannumber import RomanNumber

@app.route("/")
def index():
    return "Funcionando..."

@app.route('/toroman/<valor>')
def to_roman(valor):
    try:
        valor = int(valor)
    except:
        return 'Valor incorrecto'

    nr = RomanNumber(valor)
    return str(nr)