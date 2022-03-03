import random
'''
Cada um dos jogadores tem uma implementação de comportamento diferente, que dita as ações que eles
vão tomar ao longo do jogo. Mais detalhes sobre o comportamento serão explicados mais à frente
'''
'''
Desejamos rodar uma simulação para decidir qual a melhor estratégia. Para isso, idealizamos uma partida
com 4 diferentes tipos de possíveis jogadores. Os comportamentos definidos são:
'''

'''
O jogador impulsivo compra qualquer propriedade sobre a qual ele parar.
'''
#O jogador um é impulsivo;
def impulsivo(propriedade,jogador):
    propriedade.set_Proprietario(jogador)
    jogador.add_propriedade(propriedade)
'''
O jogador exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
'''
#O jogador dois é exigente;
def exigente(propriedade,jogador):
   if(propriedade.get_aluguel() >50):
       propriedade.set_Proprietario(jogador)
       jogador.add_propriedade(propriedade)
   else:
       print("Não COmprou")

#O jogador três é cauteloso;
'''
O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando
depois de realizada a compra
'''
def cauteloso(propriedade,jogador):
    reserva = abs(propriedade.get_valor()-(jogador.getSaldo()))
    if (reserva > 80):
        propriedade.set_Proprietario(jogador)
        jogador.add_propriedade(propriedade)
    else:
        print("Não COmprou")


#O jogador quatro é aleatório;
def aleatorio(propriedade,jogador):
    if random.random() <= 0.5:
        propriedade.set_Proprietario(jogador)
        jogador.add_propriedade(propriedade)
    else:
        print("Não COmprou")
