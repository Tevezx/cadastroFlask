from flask import Flask, render_template, redirect, request, flash
import json
import re
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] =  'Tevez123'

email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

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

    #Conexão com o banco de dados
    connect_BD = mysql.connector.connect(host='localhost', database='banco_cadastro', user='root', password='Tevez1910#')
    cont = 0
    if connect_BD.is_connected():
        print('Conectado ao banco de dados')
        cursor = connect_BD.cursor()
        cursor.execute('select * from usuario;')
        usuariosBD = cursor.fetchall()

        #Verificação se a senha corresponde com o usuario      
        for usuario in usuariosBD:
            cont = cont + 1
            usuarioNome = str(usuario[1])
            usuarioSenha = str(usuario[3])
            
            if usuarioNome == nome and usuarioSenha == senha:
                return render_template('usuario.html')
            if cont >= len(usuariosBD):
                flash('Usuario ou senha incorretos')
                return redirect('/')
        else:
            flash('Usuario ou senha incorretos')
            return redirect('/')
                
@app.route('/cadastrarUsuario', methods=['POST'])
def cadastro():
    user = []
    #Pegando requisições do html
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    user = [{
        'nome': nome,
        'senha': senha
    }]

    if len(nome) < 3:
        flash('Nome deve conter 3 caracteres')
        return redirect('/cadastro')  
    
    if not re.match(email_regex, email):
        flash('Email inválido')

    if len(senha) < 8:
        flash('A senha deve conter no minimo 8 caracteres')
        return redirect('/cadastro')

    #Abrindo o arquivo json no python  
    with open('usuarios.json') as usuariosTemp:
        usuarios = json.load(usuariosTemp)

    #Concatenando para adição do usuario novo já com o usuario existente
    usuarioNovo = usuarios +  user

    with open('usuarios.json', 'w') as gravarTemp:
        #Adicionando o novo usuario no arquivo json
        json.dump(usuarioNovo, gravarTemp, indent=4)
        flash('Cadastro realizado com sucesso!')
    return redirect('/cadastro')
    
if __name__ == '__main__':
    app.run(debug=True)