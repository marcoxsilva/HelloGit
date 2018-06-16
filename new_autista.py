from autista import Autista

autista = Autista()

nome = input('Qual seu nome?\n')
idade = int(input('Qual sua idade?\n'))

autista.set_nome(nome)
autista.set_idade(idade)

autista.valida_idade()