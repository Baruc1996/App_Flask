from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import text

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.sqlite3'
app.config['SQLALCHEMY_BINDS'] = {
    'notas':'sqlite:///notas.sqlite3',
    'conteudos':'sqlite:///conteudos.sqlite3'
}

db.init_app(app)
# Caso queira escluir uma tabela no banco de dados
# with app.app_context():
#     db.session.execute(text('DROP TABLE IF EXISTS conteudo'))
# print(' Tabela excluida')

from projeto import routs