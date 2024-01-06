from projeto import db

class Nota(db.Model):
    __bind_key__ = 'notas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    nota = db.Column(db.Float)

    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def save(self):
        db.session.add(self)
        db.session.commit()