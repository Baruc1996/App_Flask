from projeto import app, db
from flask import render_template, request, redirect, url_for
from projeto.lista_filmes import resultados_filmes
from projeto.livro import livro
from projeto.nota import Nota
from projeto.conteudo import Conteudo

# Localhost:5000/
@app.route('/', methods=['GET', 'POST'])
def principal():
    page = request.args.get('page', 1, type=int)
    per_page = 5

    if request.method == 'POST':
        if request.form.get('conteudo') and request.form.get('descricao'):
            conteudo = request.form.get('conteudo')
            descricao = request.form.get('descricao')

            novo_conteudo = Conteudo(conteudo, descricao)
            novo_conteudo.save()

    conteudos = Conteudo.query.paginate(
        page=page,
        per_page=per_page
    )
    return render_template(
        'index.html',
        conteudos=conteudos
    )

@app.route('/add_conteudo', methods=['GET', 'POST'])
def add_conteudo():
    if request.method == 'POST':
        conteudo = request.form.get('conteudo')
        descricao = request.form.get('descricao')

        novo_conteudo = Conteudo(conteudo, descricao)
        novo_conteudo.save()

    return redirect(url_for('principal'))

@app.route('/edit_conteudo/<int:id>', methods=['GET', 'POST'])
def edit_conteudo(id):
    conteudo = Conteudo.query.get(id)

    if request.method == 'POST':
        nova_descricao = request.form.get('descricao')
        conteudo.descricao = nova_descricao

        db.session.commit()
        return redirect(url_for('principal'))

    return render_template('editar_conteudos.html', descricao=conteudo)

@app.route('/remove_conteudo/<int:id>')
def remove_conteudo(id):
    conteudo = Conteudo.query.get(id)
    db.session.delete(conteudo)
    db.session.commit()
    
    return redirect(url_for('principal'))

# Localhost:5000/sobre
@app.route('/diario', methods=['GET', 'POST'])
def diario():
    page = request.args.get('page', 1, type=int)
    per_page = 5

    if request.method == 'POST':
        if request.form.get('aluno') and request.form.get('nota'):
            aluno = request.form.get('aluno')
            nota = float(request.form.get('nota'))

            nova_nota = Nota(aluno, nota)
            nova_nota.save()

    registros = Nota.query.paginate(
        page=page,
        per_page=per_page
    )

    return render_template(
        'sobre.html',
        registros=registros
    )

@app.route('/add_nota', methods=['POST'])
def add_nota():
    if request.method == 'POST':
        aluno = request.form.get('aluno')
        nota = float(request.form.get('nota'))

        nova_nota = Nota(aluno, nota)
        nova_nota.save()

    return redirect(url_for('diario'))

@app.route('/edit_nota/<int:id>', methods=['GET', 'POST'])
def edit_nota(id):
    nota = Nota.query.get(id)

    if request.method == 'POST':
        aluno = request.form.get('aluno')
        nova_nota = float(request.form.get('nota'))

        nota.aluno = aluno
        nota.nota = nova_nota

        db.session.commit()
        return redirect(url_for('diario'))

    return render_template('editar_notas.html', nota=nota)

@app.route('/remove_nota/<int:id>')
def remove_nota(id):
    nota = Nota.query.get(id)
    db.session.delete(nota)
    db.session.commit()
    
    return redirect(url_for('diario'))

@app.route('/filmes/<propriedade>')
def lista_filmes(propriedade):
    return render_template(
        'filmes.html',
        filmes=resultados_filmes(propriedade)
    )

@app.route('/livros')
def lista_livros():
    page = request.args.get('page', 1, type=int)
    per_page = 5
    todos_livros = livro.query.paginate(
        page=page,
        per_page=per_page
        )
    return render_template(
        'livros.html',
        livros=todos_livros
    )

@app.route('/add_livro', methods=(['GET', 'POST']))
def adiciona_livro():
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    valor = request.form.get('valor')

    if request.method == 'POST':
        livro_add = livro(
            nome,
            descricao,
            valor
        )
        db.session.add(livro_add)
        db.session.commit()
        return redirect(url_for('lista_livros'))
    return render_template('novo_livro.html')

@app.route('/<int:id>/atualiza_livro', methods=(['GET', 'POST']))
def atualiza_livro(id):
    # select * from livro where id = 2
    livro_bd = livro.query.filter_by(id=id).first()
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        valor = request.form['valor']

        livro.query.filter_by(id=id).update({
            'nome': nome,
            'descricao': descricao,
            'valor': valor
        })
        db.session.commit()
        return redirect(url_for('lista_livros'))

    return render_template(
        'atualiza_livro.html',
        livro=livro_bd
    )

@app.route('/<int:id>/remove_livro')
def remove_livro(id):
    livro_bd = livro.query.filter_by(id=id).first()
    db.session.delete(livro_bd)
    db.session.commit()
    return redirect(url_for('lista_livros'))
