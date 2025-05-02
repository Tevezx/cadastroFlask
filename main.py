from flask import Flask, render_template, redirect, request, flash
import json

app = Flask(__name__)
app.config['SECRET_KEY'] =  'Tevez123'

@app.route('/')
def home():
    #Definindo a tela default
    return render_template('login.html')
   
@app.route('/login', methods=['Post'])
def login():
    #Pegando requisições do html
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    #Abrindo o arquivo json no python
    with open('./usuarios.json') as usuariosTemp:
        usuarios = json.load(usuariosTemp)
        #Verificação se a senha corresponde com o usuario
        cont = 0
        #Administradores
        if nome == 'adm' and senha == '000':
            return render_template('administrador.html')
        for usuario in usuarios:
            cont = cont + 1
            if usuario['nome'] == nome and usuario['senha'] == senha:
                return render_template('usuario.html')
            if cont >= len(usuarios):
                flash('Usuario Invalido')
                return redirect('/')

if __name__ in '__main__':
    app.run(debug=True)