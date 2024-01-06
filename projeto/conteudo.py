from projeto import db

class Conteudo(db.Model):
    __bind_key__ = 'conteudos'
    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.String(100))

    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def save(self):
        db.session.add(self)
        db.session.commit()
