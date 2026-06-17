from flask import Flask, render_template, request, redirect
from models.usuario import cadastrar_usuario, login
from models.vaga import cadastrar_vaga, listar_vagas

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    if request.method == 'POST':

        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        cadastrar_usuario(nome, email, senha)

        return redirect('/login')

    return render_template('cadastro.html')


@app.route('/login', methods=['GET', 'POST'])
def tela_login():

    if request.method == 'POST':

        email = request.form['email']
        senha = request.form['senha']

        usuario = login(email, senha)

        if usuario:
            return redirect('/dashboard')

        return "Email ou senha inválidos"

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/cadastrar_vaga', methods=['GET', 'POST'])
def tela_cadastrar_vaga():

    if request.method == 'POST':

        titulo = request.form['titulo']
        empresa = request.form['empresa']
        descricao = request.form['descricao']

        cadastrar_vaga(titulo, empresa, descricao)

        return redirect('/vagas')

    return render_template('cadastrar_vaga.html')


@app.route('/vagas')
def vagas():

    lista_vagas = listar_vagas()

    return render_template(
        'vagas.html',
        vagas=lista_vagas
    )


if __name__ == '__main__':
    app.run(debug=True)