from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, Krzysztof Sikora!"

@app.route('/name/', deafults={'name': None})
@app.route('/name/<name>')
def name(name):
    return f"Hello, {name}!"