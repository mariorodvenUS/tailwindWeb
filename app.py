from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')  # Crea un login.html si es necesario

@app.route('/sign_in')
def signin():
    return render_template('sign_in.html')  # Crea un login.html si es necesario

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

@app.route('/programacion')
def programacion():
    return render_template('programacion.html')

@app.route('/3d')
def diseño():
    return render_template('diseño.html')

if __name__ == '__main__':
    app.run(debug=True)
