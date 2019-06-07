from flask import Flask
import sqlite3
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ("Olá Mundo! Estou aprendendo Flask", 200)

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
def getEscola():
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

    for linha in cursor.fetchall():
        print(linha)

    conn.close()
    return("Listado com sucesso", 200)


@app.route("/alunos/<int:id>", methods=['GET'])
def getAluno():
    conn = sqlite3.connect('ifpb.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM tb_aluno
        WHERE id_aluno = ?;
    """, id)

    for linha in cursor.fetchall():
        print(linha)

    conn.close()
    return("Listado com sucesso", 200)

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
def getCurso():
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
def getTurma():
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

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
