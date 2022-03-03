'''
Jogadores só podem comprar propriedades caso ela não tenha dono e o jogador tenha o dinheiro da venda.
Ao comprar uma propriedade, o jogador perde o dinheiro e ganha a posse da propriedade.
Cada um dos jogadores tem uma implementação de comportamento diferente, que dita as ações que eles
vão tomar ao longo do jogo. Mais detalhes sobre o comportamento serão explicados mais à frente.
Um jogador que fica com saldo negativo perde o jogo, e não joga mais. Perde suas propriedades e portanto
podem ser compradas por qualquer outro jogador.
Termina quando restar somente um jogador com saldo positivo, a qualquer momento da partida. Esse jogador
é declarado o vencedor.
'''

class jogador(object):

    def __init__(self,posicao,volta,saldo):
        self.posicao = posicao
        self.volta = volta
        self.saldo = saldo
        self.propriedades = []
        self.valido = True

    def get_propriedades(self):
        return self.propriedades

    def invalida_jogador(self):
        self.valido = False

    def set_Volta(self):
        self.volta  +=1

    def add_propriedade(self,propriedade):
        self.propriedades.append(propriedade)

    def comprarPripriedade(self,propriedade):
        self.propriedades.append(propriedade)

    def getSaldo(self):
        return self.saldo

    def setSaldo(self,valor):
        self.saldo += valor

    def descontaAluguel(self,valor):
        self.saldo -= valor

    def setPosicao(self,passos,qtd_casas_tabuleiro):
        print(self.getPosicao() +passos)
        if ((self.getPosicao() +passos )< qtd_casas_tabuleiro):
            self.posicao += passos
        else:
            self.posicao = (self.getPosicao() + passos) - 19  # logica para posicao ser circular
            self.setSaldo(100) #Ao completar uma volta no tabuleiro, o jogador ganha 100 de saldo.
            self.set_Volta()

    def getPosicao(self):
        return self.posicao

    def get_person(self):
        return "<Person(%s,%s,%s,%s)>" % (self.posicao,self.volta,self.saldo ,self.propriedades.__str__() )


