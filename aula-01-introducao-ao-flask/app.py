from flask import Flask, render_template

app = Flask(__name__, template_folder='views')

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/games')

def games():
    return render_template('games.html')

@app.route('/consoles')

def consoles():
    return render_template('consoles.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
