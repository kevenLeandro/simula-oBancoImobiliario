'''
Ao cair em uma propriedade sem proprietário, o jogador pode escolher entre comprar ou não a
propriedade. Esse é a única forma pela qual uma propriedade pode ser comprada.
Ao cair em uma propriedade que tem proprietário, ele deve pagar ao proprietário o valor do aluguel da
propriedade.
Ao completar uma volta no tabuleiro, o jogador ganha 100 de saldo.
'''

from  propriedade import  propriedade as prop
import json

class tabuleiro(object):

    def carrega(self):
        listaDePropriedades = []
        with open("propriedades.json", encoding='utf-8') as meu_json:
            dados = json.load(meu_json)
        # para cada item do arquivo json
        for i in dados:
            id = i['id']
            nome =i['nome']
            valor = i['valor']
            aluguel = i['aluguel']
            p = prop(id,nome, valor, aluguel)
            print(p.get_propriedade())
            listaDePropriedades.append(p)
        return listaDePropriedades

    def __init__(self):
        self.casas = self.carrega()

    def get_tabuleiro(self):
        return "<Tabuleiro(%s)>" % (self.casas)


#t = tabuleiro()

#t.carrega()