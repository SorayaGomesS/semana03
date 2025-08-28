from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

# Rota - Página Inicial
@app.route("/")
def home():
    return render_template('index.html', current_time=datetime.utcnow())

# Rota - Hello user
@app.route('/user/<username>')
def user_profile(username):
    return render_template('user.html', name=username)

# Rota de erro
@app.route('/rotainexistente')
def not_found_route():
    return render_template('404.html'), 404

# Não encontrada
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
