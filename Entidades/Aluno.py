class Aluno():
    """docstring for Aluno."""
    def __init__(self, id_aluno, nome, endereco, matricula, cpf, nasc):
        super(Aluno, self).__init__()
        self.id_aluno = id_aluno
        self.nome = nome
        self.endereco = endereco
        self.matricula = matricula
        self.cpf = cpf
        self.nascimento = nasc
