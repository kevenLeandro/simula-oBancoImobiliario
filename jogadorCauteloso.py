import jogador
import comportamento

class jogadorCauteloso(jogador.jogador):

    def __init__(self, posicao, volta, saldo):
        super().__init__(posicao, volta, saldo)

    def comportamento(self, propriedade,jogador):
        comportamento.cauteloso(propriedade, jogador)

    def get_definition(self):
        return "O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrandodepois de realizada a compra."



