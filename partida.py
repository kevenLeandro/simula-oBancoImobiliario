'''
Saída
Uma execução do programa proposto deve rodar 300 simulações, imprimindo no console os dados referentes
às execuções. Esperamos encontrar nos dados as seguintes informações:
Quantas partidas terminam portime out (1000 rodadas);
Quantos turnos em média demora uma partida;
Qual a porcentagem de vitórias por comportamento dos jogadores;
Qual o comportamento que mais vence
'''

from  tabuleiro import tabuleiro as tab
from jogadorImpulsivo import jogadorImpulsivo as jog_impulsivo
from jogadorCauteloso import jogadorCauteloso as jog_cauteloso
from jogadorAleatorio import jogadorAleatorio as jog_aleatorio
from jogadorExigente import jogadorExigente as jog_Exigente

import dado
import Regras as regras

QUANTIDADE_CASAS_TABULEIRO = 19
t = tab()
casas = t.carrega()
jogadores = []
jogadores_eliminados = []

j1 = jog_impulsivo(1,0, 300)
j2 = jog_cauteloso(2 ,0, 300)
j3= jog_aleatorio(3 ,0, 300)
j4= jog_Exigente(4 ,0, 300)

jogadores.append(j1)
jogadores.append(j2)
jogadores.append(j3)
jogadores.append(j4)

def partida (casas, jogadores):
    rodada = 0
    criterio_termino_por_max_rodada = True
    n= 0

    while(criterio_termino_por_max_rodada):
        criterio_termino_por_max_rodada = regras.verificaTerminoPorNPartidas(rodada,jogadores)
        for jogaforVez in jogadores:
            if (jogaforVez.getSaldo() == 0):
                print()

            print(jogaforVez.get_person())
            passos = dado.RolagemDado()
            print(jogaforVez.getPosicao())
            if (jogaforVez.getPosicao()>19):
                print()
            jogaforVez.setPosicao(passos, QUANTIDADE_CASAS_TABULEIRO)
            # verifica se vai comprar ou se vai pagar aluguel
            regras.verificaPropriedade(casas[jogaforVez.getPosicao()],jogaforVez)

            info_jogadador =  regras.verificaJogador(jogaforVez)
            if (info_jogadador == False or jogaforVez.getSaldo()  ==0):
                print()
                jogadores_eliminados.append(jogaforVez)
                jogadores.remove(jogaforVez)
                regras.devolverPropriedades(jogaforVez.get_propriedades(),casas)
            else:
                print()

        if (jogaforVez.getSaldo()  ==0):
            print()

        n += 1
        print("############# rodada")
        print(n)

        if jogadores.__len__() == 1:
            criterio_termino_por_max_rodada = False
            regras.declaraVencedor(jogaforVez)

partida(casas, jogadores)

print()
