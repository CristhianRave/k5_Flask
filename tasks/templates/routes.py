from tasks import app

@app.route('/')
def index():
    return'Aqui ira mi aplicacion'