from flask import Flask, render_template, redirect, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] =  'Tevez123'

@app.route('/')
def home():
    return render_template('login.html')
@app.route('/login', methods=['Post'])
def login():

    nome = request.form.get('nome')
    senha = request.form.get('senha')

    if nome == 'Carlos' and senha == 'Tevez123':
        return render_template('usuario.html')
    else:        
        flash('Usuario invalido')
        return redirect('/')


if __name__ in '__main__':
    app.run(debug=True)