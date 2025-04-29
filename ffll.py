from flask import Flask, request

app = Flask(__name__)

@app.route('/calc')
def calc():
    operator = request.args.get('op')
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)

    if operator == 'add':
        result = a+b
    elif operator == 'diff':
        result = a - b
    elif operator == 'mult':
        result = a * b
    elif operator == 'sub':
        result = a / b
    else:
        return 'Введите доступную операцию'

    return str(result)

if __name__ == '__main__':
    app.run(debug=True)