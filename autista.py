class Autista():
    _nome = ''
    _idade = 0

    def set_nome(self, nome):
        self._nome = nome

    def set_idade(self, idade):
        if idade > 0:
            self._idade = idade


    def valida_idade(self):
        if self._idade >= 18:
            print('Você é autista, pode entrar!')
        else:
            print('Que pena, você não pode entrar!')