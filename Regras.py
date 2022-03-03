import jogador

'''
Jogadores só podem comprar propriedades caso ela não tenha dono e o jogador tenha o dinheiro da venda.
Ao comprar uma propriedade, o jogador perde o dinheiro e ganha a posse da propriedade
'''
def verificaCompra(propriedade,jogador):
    print(propriedade.get_propriedade(),jogador.get_person())
    if (jogador.getSaldo() >= propriedade.valor):
        print()
       #jogador compra com a sua especificadade de comportamento
        jogador.comportamento(propriedade,jogador)

'''
Um jogador que fica com saldo negativo perde o jogo, e não joga mais. Perde suas propriedades e portanto
podem ser compradas por qualquer outro jogador.
'''
def verificaJogador(jogador: jogador):
    if (jogador.valido == False):
        return False
    else:
        return True

'''
Um jogador que fica com saldo negativo perde o jogo, e não joga mais. Perde suas propriedades e portanto
podem ser compradas por qualquer outro jogador.

'''
def verificaPerdedor(aluguel,jogador):
    if (jogador.getSaldo() < aluguel or jogador.getSaldo() ==0):
        jogador.invalida_jogador()
        return True
    else:
        return  False

'''
Caso o jogo demore muito, como é de costume em jogos dessa natureza, o jogo termina na milésima rodada
com a vitória do jogador com mais saldo. O critério de desempate é a ordem de turno dos jogadores nesta
partida.
'''
'''
Termina quando restar somente um jogador com saldo positivo, a qualquer momento da partida. Esse jogador
é declarado o vencedor.
'''

#todo
def verificaTerminoPorNPartidas(rodada,jogadores):
    volta_termino = 1000
    return  (rodada <= volta_termino)

'''
Ao cair em uma propriedade que tem proprietário, ele deve pagar ao proprietário o valor do aluguel da
propriedade.
'''
def descontaAluguel(aluguel,jogador):
    if(verificaPerdedor(aluguel, jogador)):
        if (jogador.getSaldo() == 0):
            jogador.invalida_jogador()
        return  {'Desconto': False, 'saldo': jogador.getSaldo()}
    else:
        jogador.descontaAluguel(aluguel)
        return {'Desconto': True , 'saldo': jogador.getSaldo() }

'''
Verifica se não tem proprietario e logo está disponivel para venda ou se o jogador deve pagar aluguel
'''
def verificaPropriedade(casa,jogador):
    print(casa.get_propriedade,jogador.get_person())
    if (casa.getTemProprietario()):
        descontaAluguel(casa.get_aluguel(), jogador)
    else:
        verificaCompra(casa, jogador)

    if (jogador.getSaldo() == 0):
        jogador.invalida_jogador()


'''
declara vencedor
'''
def declaraVencedor(jogador):
    print(type(jogador))
    print('Vencedor{}'.format(jogador.get_person()))

def find(arr , id):
    for x in arr:
        if x.id == id:
            xID = arr.index(x)
            arr[xID].remove_proprietario()

def devolverPropriedades(propriedades,casas):
    for propriedade in propriedades:
       id = propriedade.get_id()
       find(casas, id)





