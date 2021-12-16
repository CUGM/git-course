from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Bye Code!"

@app.route('hello')
def greating():
    return "Helllo World!"

@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int):
        nums_sum = a + b
        return f"La suma es: {str(nums_sum)}"
    
    @app.route('/multiply/<int:a>/<int:b>')
def multiply(a: int, b: int):
        result = float (a * b)
        return f"El resultado de la multiplicacion es: {str(result)}"
