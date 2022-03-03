import jogador
import comportamento

class jogadorExigente(jogador.jogador):

    def __init__(self, posicao, volta, saldo):
        super().__init__(posicao, volta, saldo)

    def comportamento(self, propriedade,jogador):
        comportamento.exigente(propriedade, jogador)

    def get_definition(self):
        return "O jogador exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50."


