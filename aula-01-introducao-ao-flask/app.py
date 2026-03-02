from flask import Flask, render_template

app = Flask(__name__, template_folder='views')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/games')
def games():
    titulo = "Team Fortress 2"
    genero = "Team Shooter"
    ano = 2007
    jogadores = ["Pedro", "Luiz", "Tales"]
    return render_template('games.html', titulo = titulo, genero = genero, ano = ano, jogadores = jogadores)

@app.route('/consoles')
def consoles():
    console = {"Nome": "Playstation 2",
               "Fabricante": "Sony",
               "Ano": 2000}
    return render_template('consoles.html', console = console)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
