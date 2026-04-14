
from flask import Flask, render_template, request, url_for


app = Flask(__name__, template_folder='views')


def init_app(app):

    listaConsoles = ['Playstation 5', 'Xbox One',
            'Super Nintendo', 'Atari 2600', 'Nintendo 3DS']
    listaGames = [{'titulo' : 'CS-GO', 'ano' : 2012, 'genero ' : 'FPS Online', 'plataforma' : 'PC (Windows)'}]
    
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/games')
    def games():
        # Criar informação para a rota de games
        titulo = "Portal 2"
        ano = 2011
        categoria = "Puzzle"
        jogadores = ['Marcos', 'Richard', "Miguel", 'Renato', 'Pedro']
        return render_template('games.html', titulo=titulo, ano=ano, categoria=categoria, jogadores=jogadores)

    @app.route('/consoles', methods=['GET', 'POST'])
    def consoles():
        # criando um objeto
        console = {"Nome:": "Playstation 2 ",
                   "Fabricante: ": "Sony", "Ano: ": 2000}
        print("FUCKING CONSOLES")
        # Recebendo o valor do formulário
        if request.method == 'GET':
            novoConsole = request.args.get('novoConsole')
            if novoConsole != None and novoConsole != '':
                listaConsoles.append(novoConsole)

        return render_template('consoles.html', console=console, listaConsoles=listaConsoles)

    @app.route('/cadastrar', methods=['GET', 'POST'])
    def cadastrar():
        if request.method == 'POST':
            titulo = request.form.get('titulo')
            ano = request.form.get('ano')
            genero = request.form.get('genero')
            plataforma = request.form.get('plataforma')
            listaGames.append({'titulo' : titulo, 'ano' : ano, 'genero' : genero, 'plataforma' : plataforma})
        return render_template('cadastrar.html', listaGames = listaGames)