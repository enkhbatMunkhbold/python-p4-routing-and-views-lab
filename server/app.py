#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f'{parameter}')
    return f'{parameter}'

@app.route('/count/<int:number>')
def count(number):
    result = ''.join(f'{num}\n' for num in range(number))
    return f'{result}'

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    a = int(num1)
    b = int(num2)
    match operation:
        case '+':
            return f'{a + b}' 
        case '-':
            return f'{a - b}'
        case '*':
            return f'{a * b}'
        case 'div':
            return f'{a / b}'
        case '%':
            return f'{a % b}'
        case _:
            return "Unknown operand!"