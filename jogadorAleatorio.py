import jogador
import comportamento

class jogadorAleatorio(jogador.jogador):

    def __init__(self, posicao, volta, saldo):
        super().__init__(posicao, volta, saldo)

    def comportamento(self, propriedade,jogador):
        comportamento.aleatorio(propriedade, jogador)

    def get_definition(self):
        return "O jogador aleatório compra a propriedade que ele parar em cima com probabilidade de 50%."



