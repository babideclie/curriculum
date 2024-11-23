from flask import Flask, render_template, request, jsonify

app = Flask(___Curriculum_)

@app.app.route('/')
def index():
    return render_template('index.inindex.html')

@app.app.route('/desiign1')
def design1():
    with open('data.jsonn','r') as f:
        data=f.f.read()
    return render_template('design1.html', data=json.json.loads(data))

@app.route('/design2')
def design2():
    with open('data.json', 'r') as f:
        data = f.read()
    return render_template('design2.html', data=json.loads(data))

@app.route('/design3')
def design3():
    with open('data.json', 'r') as f:
        data = f.read()
    return render_template('design3.html', data=json.loads(data))

if __name__ == '__main__':
    app.run(debug=True)

##add

import json

@app.route('/save', methods=['POST'])
def save():
    data = {
        "name": request.form['name'],
        "email": request.form['email'],
        "phone": request.form['phone'],
        "about": request.form['about']
    }
    with open('data.json', 'w') as f:
        json.dump(data, f)
    return "Currículo salvo! Acesse /design1, /design2 ou /design3 para visualizar."

@app.route('/design2')
def design2():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return render_template('design2.html', data=data)

@app.route('/design3')
def design3():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return render_template('design3.html', data=data)

