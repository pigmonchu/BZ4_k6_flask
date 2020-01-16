from nroman import app

@app.route("/")
def index():
    return "Funcionando..."