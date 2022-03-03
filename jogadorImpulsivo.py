
import jogador
import comportamento

class jogadorImpulsivo(jogador.jogador):

    def __init__(self,posicao,volta,saldo):
        super().__init__(posicao,volta,saldo)

    def comportamento(self,propriedade,jogador):
        comportamento.impulsivo(propriedade,jogador)


    def get_definition(self):
       return "O jogador impulsivo compra qualquer propriedade sobre a qual ele parar."



