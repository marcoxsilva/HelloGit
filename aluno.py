class Aluno():
    nome = 'Marcos Antonio'
    _idade = 23
    end = 'Teresina/PI'

    def set_aluno(self, idade):
        if idade > 0:
            self._idade = idade