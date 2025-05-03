from flask import Flask, render_template, redirect, request, flash
import json

app = Flask(__name__)
app.config['SECRET_KEY'] =  'Tevez123'

@app.route('/')
def home():
    #Definindo a tela default
    return render_template('login.html')

@app.route('/cadastro')
def cadastrar():
    #Definindo a tela de cadastro
    return render_template('cadastro.html')
   
@app.route('/login', methods=['POST'])
def login():
    #Pegando requisições do html
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    #Abrindo o arquivo json no python
    with open('usuarios.json') as usuariosTemp:
        usuarios = json.load(usuariosTemp)
        #Verificação se a senha corresponde com o usuario
        cont = 0
        for usuario in usuarios:
            cont = cont + 1
            if usuario['nome'] == nome and usuario['senha'] == senha:
                return render_template('usuario.html')
            if cont >= len(usuarios):
                flash('Usuario Invalido')
                return redirect('/')
                
@app.route('/cadastrarUsuario', methods=['POST'])
def cadastro():
    user = []
    #Pegando requisições do html
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    user = [{
        'nome': nome,
        'senha': senha
    }]

    #Abrindo o arquivo json no python  
    with open('usuarios.json') as usuariosTemp:
        usuarios = json.load(usuariosTemp)

    #Concatenando para adição do usuario novo já com o usuario existente
    usuarioNovo = usuarios +  user

    with open('usuarios.json', 'w') as gravarTemp:
        #Adicionando o novo usuario no arquivo json
        json.dump(usuarioNovo, gravarTemp, indent=4)
    return redirect('/cadastrar')
    
if __name__ == '__main__':
    app.run(debug=True)