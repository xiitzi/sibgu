from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

def generate_phone_numbers():
    numbers = set()
    while len(numbers) < 1000:
        random_part = ''.join([str(random.randint(0, 9)) for _ in range(7)])
        full_number = f"8913{random_part}"
        numbers.add(full_number)
    return sorted(numbers)

phone_numbers = generate_phone_numbers()

#print('Hellow, world!') hihihih
#print('meowmeowmeow') yes?

@app.route('/')
def index():
    return render_template('index.html', phone_numbers=phone_numbers)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        phone_number = request.form.get('phone_number', '').strip()
        return redirect(url_for('phone_info', number=phone_number))
    return redirect(url_for('index'))

@app.route('/phone/<number>')
def phone_info(number):
    return render_template('phone_info.html', number=number)

if __name__ == '__main__':
    app.run(debug=True)
