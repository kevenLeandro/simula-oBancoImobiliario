# nome , valor, aluguel, dono
'''Cada propriedade tem um custo de
venda, um valor de aluguel, um proprietário caso já estejam compradas, e seguem uma determinada ordem no
tabuleiro'''
import jogador


class propriedade(object):

    def __init__(self, id,nome, valor, aluguel, proprietario=None):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.aluguel = aluguel
        self.proprietario = proprietario

    def get_valor(self):
        self.valor

    def remove_proprietario(self):
        self.proprietario = None

    def get_id(self):
        return self.id

    def set_Proprietario(self,proprietario):
        self.proprietario = proprietario

    def get_aluguel(self):
         return  self.aluguel

    def get_propriedade(self):
        return ' {} {} {} {} '.format(self.nome,self.valor, self.aluguel,self.proprietario)

    def getTemProprietario(self):
        return  (not self.proprietario is None)


