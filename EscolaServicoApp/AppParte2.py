from flask import Flask
import sqlite3
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route("/escolas", methods=['GET'])
def getEscolas():
    conn = sqlite3.connect('ifpb.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM tb_escola;
    """)
    for linha in cursor.fetchall():
        print(linha)


    conn.close()
    return("Listado com sucesso", 200)

@app.route("/escolas/<int:id>", methods=['GET'])
def getEscola(id):
    conn = sqlite3.connect('ifpb.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM tb_escola
        WHERE id_escola = ?;
    """, id)

    for linha in cursor.fetchall():
        print(linha)


    conn.close()
    return("Listado com sucesso", 200)

@app.route("/escola", methods=['POST'])
def setEscola():
    print('Cadastrando a escola')
    nome = request.form["nome"]
    logradouro = request.form["logradouro"]
    cidade = request.form["cidade"]
    print(nome,logradouro, cidade)

    conn = sqlite3.connect('ifpb.db')
    cursor = conn.cursor()
    cursor.execute("""
        insert into tb_escola(nome, logradouro, cidade)
        values(?, ?, ?);
    """, (nome, logradouro, cidade))
    conn.commit()
    conn.close()
    return("Inserido com sucesso", 200)

@app.route("/alunos", methods=['GET'])
def getAlunos():

    conn = sqlite3.connect('ifpb.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM tb_aluno;
    """)
    alunos = []
    for linha in cursor.fetchall():
        aluno = {
            "nome":linha[0],
            "matricula":linha[1],
            "Cpf":linha[2],
            "nascimento":linha[3]
        }
        alunos.append(aluno)


    conn.close()
    return jsonify(alunos)



@app.route("/aluno", methods=['POST'])
def setAluno():
    print('Cadastrando o aluno')
    nome = request.form["nome"]
    print(nome)
    matricula = request.form["matricula"]
    print(matricula)
    cpf = request.form["cpf"]
    print(cpf)
    nascimento = request.form["nascimento"]
    print(nascimento)

    conn = sqlite3.connect('ifpb.db')
    cursor = conn.cursor()
    cursor.execute("""
        insert into tb_aluno(nome, matricula, cpf, nascimento)
        values(?, ?, ?, ?);
    """, (nome, matricula , cpf, nascimento))

    conn.commit()
    conn.close()

    return("Inserido com sucesso", 200)

@app.route("/cursos", methods=['GET'])
def getCursos():
    conn = sqlite3.connect('ifpb.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM tb_curso;
    """)
    for linha in cursor.fetchall():
        print(linha)


    conn.close()
    return("Listado com sucesso", 200)

@app.route("/cursos/<int:id>", methods=['GET'])
def getCurso(id):
    conn = sqlite3.connect('ifpb.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM tb_curso
        WHERE id_curso = ?;
    """, id)
    for linha in cursor.fetchall():
        print(linha)


    conn.close()
    return("Listado com sucesso", 200)

@app.route("/curso", methods=['POST'])
def setCurso():
    print('Cadastrando o curso')
    nome = request.form["nome"]
    print(nome)
    turno = request.form["turno"]
    print(turno)

    conn = sqlite3.connect('ifpb.db')
    cursor = conn.cursor()
    cursor.execute("""
        insert into tb_curso(nome, turno)
        values(?, ?);
        """, (nome, turno))

    conn.commit()
    conn.close()
    return("Inserido com sucesso", 200)

@app.route("/turmas", methods=['GET'])
def getTurmas():
    conn = sqlite3.connect('ifpb.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM tb_turma;
    """)
    for linha in cursor.fetchall():
        print(linha)


    conn.close()
    return("Listado com sucesso", 200)

@app.route("/turmas/<int:id>", methods=['GET'])
def getTurma(id):
    conn = sqlite3.connect('ifpb.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM tb_turma
        WHERE id_turma = ?;
    """, id)
    for linha in cursor.fetchall():
        print(linha)


    conn.close()
    return("Listado com sucesso", 200)

@app.route("/turma", methods=['POST'])
def setTurma():
    print('Cadastrando a Turma')
    nome = request.form["nome"]
    print(nome)
    curso = request.form["curso"]
    print(curso)

    conn = sqlite3.connect('ifpb.db')
    cursor = conn.cursor()
    cursor.execute("""
        insert into tb_turma(nome, fk_id_curso)
        values(?, ?);
        """, (nome, curso))

    conn.commit()
    conn.close()
    return("Inserido com sucesso", 200)

@app.route("/disciplinas", methods=['GET'])
def getDisciplinas():
    conn = sqlite3.connect('ifpb.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM tb_disciplina;
    """)

    for linha in cursor.fetchall():
        print(linha)


    conn.close()
    return("Listado com sucesso", 200)

@app.route("/disciplinas/<int:id>", methods=['GET'])
def getDisciplina(id):
    conn = sqlite3.connect('ifpb.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM tb_disciplina
        WHERE id_disciplina = ?;
    """, id)

    for linha in cursor.fetchall():
        print(linha)


    conn.close()
    return("Listado com sucesso", 200)

@app.route("/disciplina", methods=['POST'])
def setDisciplina():
        print('Cadastrando a Disciplina')
        nome = request.form["nome"]
        print(nome)

        conn = sqlite3.connect('ifpb.db')
        cursor = conn.cursor()
        cursor.execute("""
            insert into tb_disciplina(nome)
            values(?);
        """, (nome, ))

        conn.commit()
        conn.close()
        return("Inserido com sucesso", 200)
@app.route("/escola/<int:id>", methods=['PUT'])
def updateEscola(id):
    print ("-------------- Atualizando Escola --------------")
    escola = request.get_json()
    nome = escola['nome']
    logradouro = escola['logradouro']
    cidade = escola['cidade']
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM tb_escola WHERE id_escola = ?; """, (id,))
    data = cursor.fetchone()
    if (data is not None):
        cursor.execute("""UPDATE tb_escola SET nome=?, logradouro=?, cidade=?""" (nome,logradouro, cidade, id))
        conn.commit()
    else:
        print ("-------------- Cadastrando Escola --------------")
        cursor.execute(""" INSERT INTO tb_escola(nome, logradouro, cidade) VALUES(?,?,?); """, (nome,logradouro, cidade))
        conn.commit()
        id = cursor.lastrowid
        escola["id_escola"] = id
    conn.close()
    return jsonify(escola)
@app.route("/aluno/<int:id>", methods=['PUT'])
def updateAluno(id):
    print ("-------------- Atualizando Aluno --------------")
    aluno = request.get_json()
    nome = aluno['nome']
    matricula = aluno['matricula']
    cpf = aluno['cpf']
    nascimento = aluno['nascimento']
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM tb_aluno WHERE id_aluno = ?; """, (id,))
    data = cursor.fetchone()
    if (data is not None):
        cursor.execute("""UPDATE tb_aluno SET nome=?, matricula=?, cpf=?,nascimento=? WHERE id_aluno = ? """, (nome, matricula, cpf, nascimento,id))
        conn.commit()
    else:
        print ("-------------- Cadastrando Aluno --------------")
        cursor.execute(""" INSERT INTO tb_aluno(nome, matricula, cpf, nascimento) VALUES(?,?,?,?); """, (nome, matricula, cpf, nascimento))
        conn.commit()
        id = cursor.lastrowid
        aluno["id_aluno"] = id
    conn.close()
    return jsonify(aluno)
@app.route("/curso/<int:id>", methods=['PUT'])
def updateCurso(id):
    print ("-------------- Atualizando Curso --------------")
    curso = request.get_json()
    nome = curso['nome']
    turno = curso['turno']
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM tb_curso WHERE id_curso = ?; """, (id,))
    data = cursor.fetchone()
    if (data is not None):
        cursor.execute("""UPDATE tb_curso SET nome=?, turno=? WHERE id_curso = ? """, (nome, turno, id))
        conn.commit()
    else:
        print ("-------------- Cadastrando Curso --------------")
        cursor.execute(""" INSERT INTO tb_curso(nome, turno) VALUES(?,?); """, (nome, turno))
        conn.commit()
        id = cursor.lastrowid
        curso["id_curso"] = id
    conn.close()
    return jsonify(curso)
@app.route("/turma/<int:id>", methods=['PUT'])
def updateTurma(id):
    print ("-------------- Atualizando Turma --------------")
    turma = request.get_json()
    nome = turma['nome']
    curso = turma['curso']
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM tb_turma WHERE id_turma = ?; """, (id,))
    data = cursor.fetchone()
    if (data is not None):
        cursor.execute(""" UPDATE tb_turma SET nome=?, curso=? WHERE id_disciplina = ?""", (nome,curso, id))
        conn.commit()
    else:
        print ("-------------- Cadastrando Turma --------------")
        cursor.execute(""" INSERT INTO tb_turma(nome, curso) VALUES(?,?); """, (nome, curso))
        conn.commit()
        id = cursor.lastrowid
        turma["id_turma"] = id
    conn.close()
    return jsonify(turma)
@app.route("/disciplina/<int:id>", methods=['PUT'])
def updateDisciplina(id):
    print ("-------------- Atualizando Disciplina --------------")
    disciplina = request.get_json()
    nome = disciplina['nome']
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM tb_disciplina WHERE id_disciplina = ?; """, (id,))
    data = cursor.fetchone()
    if (data is not None):
        cursor.execute(""" UPDATE tb_disciplina SET nome=? WHERE id_disciplina = ?""", (nome, id))
        conn.commit()
    else:
        print ("-------------- Cadastrando Disciplina --------------")
        cursor.execute(""" INSERT INTO tb_disciplina(nome) VALUES(?); """, (nome,))
        conn.commit()
        id = cursor.lastrowid
        disciplina["id_disciplina"] = id
    conn.close()
    return jsonify(disciplina)

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
