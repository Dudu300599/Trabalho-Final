import pygame
from datetime import datetime
import numpy as np
import sys
import time
import random
from collections import deque

#MATRIZ DE ADJACÊNCIA
matriz_jogo = np.array([[0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]])

# --- POSIÇÕES MANUAIS DOS 31 VÉRTICES ---
vertex_positions = [
    (440, 50),  (540, 50),  (640, 50),  (740, 50),  (840, 50),
    (440, 150), (540, 150), (640, 150), (740, 150), (840, 150),
    (440, 250), (540, 250), (640, 250), (740, 250), (840, 250),
    (440, 350), (540, 350), (640, 350), (740, 350), (840, 350),
    (440, 450), (540, 450), (640, 450), (740, 450), (840, 450),
    (540, 550), (640, 550), (740, 550), (440, 650), (640, 650), (840, 650)
]

#Vetor com a posição inicial das peças
#Com -1 representando a onça e 1 represetando os cachorros
def inicializacao():
  posicao_inicial_pecas = ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
  posicao_inicial_pecas[12] = -1
  posicao_inicial_pecas[0] = 1
  posicao_inicial_pecas[1] = 1
  posicao_inicial_pecas[2] = 1
  posicao_inicial_pecas[3] = 1
  posicao_inicial_pecas[4] = 1
  posicao_inicial_pecas[5] = 1
  posicao_inicial_pecas[6] = 1
  posicao_inicial_pecas[7] = 1
  posicao_inicial_pecas[8] = 1
  posicao_inicial_pecas[9] = 1
  posicao_inicial_pecas[10] = 1
  posicao_inicial_pecas[11] = 1
  posicao_inicial_pecas[13] = 1
  posicao_inicial_pecas[14] = 1

  return posicao_inicial_pecas

#Mapea os saltos da onça PosiçãoAtual:[(PosiçãoDestino, CasaSaltada)]
saltos_onca = {
    0: [(2, 1), (10, 5), (12, 6)],
    1: [(11, 6), (3, 2)],
    2: [(0, 1), (4, 3), (10, 6), (12, 7), (14, 8)],
    3: [(1, 2), (13, 8)],
    4: [(2, 3), (14, 9), (12, 8)], 
    5: [(7, 6), (15, 10)], 
    6: [(16, 11), (8, 7), (18, 12)], 
    7: [(5, 6), (9, 8), (17, 12)], 
    8: [(6, 7), (18, 13), (16, 12)], 
    9: [(8, 7), (19, 14)], 
    10:[(0, 5), (12, 11), (20, 15), (2, 6), (22, 16)], 
    11:[(1, 6), (21, 16), (13, 12)], 
    12:[(0, 6), (2, 7), (4, 8), (10, 11), (14, 13), (20, 16), (22, 17), (24, 18)],
    13:[(11, 12), (3, 8), (23, 18)], 
    14:[(4, 9), (12, 13), (24, 19), (22,18)], 
    15:[(5, 10), (17, 16)], 
    16:[(6, 11), (8, 12), (18, 17), (27,22)], 
    17:[(15, 16), (7, 12), (19, 18), (26,22)], 
    18:[(8, 13), (6, 12), (16, 17), (25,22)], 
    19:[(17, 18), (9, 14)], 
    20:[(10, 15), (22, 21), (12, 16)], 
    21:[(11, 16), (23, 22)], 
    22:[(10, 16), (12, 17), (14, 18), (20,21), (24,23), (28,25), (29,26), (30,27)], 
    23:[(21, 22), (13, 18)], 
    24:[(14, 19), (12, 18), (22, 23)], 
    25:[(18, 22), (27, 26)], 
    26:[(17, 22)], 
    27:[(16, 22), (25, 26)], 
    28:[(22, 25), (30, 29)], 
    29:[(22, 26)], 
    30:[(22, 27), (28, 29)], 
}


estado_do_jogo = inicializacao() #Inicializa o estado inicial do tabuleiro

BRANCO = (255, 255, 255)
LARANJA = (203, 112, 31)
VERDE_CLARO = (221, 207, 142)
CREME = (252, 217, 191)
PRETO = (0, 0, 0)
CINZA = (200, 200, 200)
VERMELHO = (200, 50, 50)
AZUL = (50, 50, 200)
AMARELO = (230, 230, 0)



pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Jogo da Onça")
clock = pygame.time.Clock()

#IMAGENS
peca_onca = pygame.transform.scale(
    pygame.image.load("imagens/ONÇA.png"), (50,50)
)

peca_cachorro = pygame.transform.scale(
    pygame.image.load("imagens/CACHORRO.png"), (50,50)
)

fundo_jogo = pygame.transform.scale(
    pygame.image.load("imagens/Tabuleiro_Tabuleiro_Frente.png").convert(),
    (1280,720)
)

selected = None
turno = -1  # Onça começa
capturados = 0
fim_de_jogo = False
vencedor = None
nos_visitados = 0
cont_turno = 0



#Função que retorna os movimentos validos da onça, e tem como entrada a posição da onça, o estado atual do tabuleiro e os saltos da onça
def movimentos_validos_onca(posicao_onca, estado_atual, saltos_onca):
    movimentos_possiveis = []

    #Movimentos normais
    for i in range(len(matriz_jogo)):
        if matriz_jogo[posicao_onca][i] == 1 and estado_atual[i] == 0:
            movimentos_possiveis.append(i)

    #Saltos (capturas)
    for destino, meio in saltos_onca.get(posicao_onca, []):
        if estado_atual[meio] == 1 and estado_atual[destino] == 0:
            movimentos_possiveis.append(destino)

    return movimentos_possiveis


#Função que retorna os movimentos validos dos cachorros, e tem como entrada a posição do cachorro e o estado atual do tabuleiro
def movimentos_validos_cachorros(posicao_cachorro, estado_atual):
  movimentos_possiveis = []
  for i in range(len(matriz_jogo)):
    if matriz_jogo[posicao_cachorro][i] == 1: #Verifica se tem aresta entre o vértice atual da peça e outros vértices
        if estado_atual[i] == 0:   #Verifica se a casa adjacente está vazia
          movimentos_possiveis.append(i)    #Adiciona o movimento a lista de movimentos validos
  return movimentos_possiveis


#Função que retorna quem venceu a partida, e tem como entrada posição da onça e o estado atual do tabuleiro
def condicao_vitoria(posicao_onca, estado_atual):
    qnt_cachorros = estado_atual.count(1)
    if qnt_cachorros <= 9: #Verifica se a onça ja capturou 5 cachorros
        return "Vitória da Onça"
    if movimentos_validos_onca(posicao_onca, estado_atual, saltos_onca) == []: #Verifica se a onça nao possui mais movimentos
        return "Vitória dos Cachorros"
    return None


#Função utilidade sugerida pelo artigo
def utilidade_onca_1(estado_atual): 
  qnt_cachorros = estado_atual.count(1)
  capturas = 14 - qnt_cachorros
  return capturas * 200

#Função utilidade criada por nós
def utilidade_onca_2(estado_atual): 
  qnt_cachorros = estado_atual.count(1)
  capturas = 14 - qnt_cachorros
  posicao_onca = estado_atual.index(-1)
  movimentos = movimentos_validos_onca(posicao_onca, estado_atual, saltos_onca)
  qnt_movimentos = len(movimentos)
  return capturas * 200 + qnt_movimentos * 10

#Apesar do nome nao é utilizada pelo minimax, apenas retorna um movimento aleatorio entre os disponiveis
def utilidade_onca_0(estado_atual):
    movimentos = gerar_estados_futuros_onca(estado_atual)
    movimento_aleatorio = random.choice(movimentos)
    return movimento_aleatorio


#Apesar do nome nao é utilizada pelo minimax, apenas retorna um movimento aleatorio entre os disponiveis
def utilidade_cachorros_0(estado_atual):
    movimentos = gerar_estados_futuros_cachorros(estado_atual)
    movimento_aleatorio = random.choice(movimentos)
    return movimento_aleatorio


def utilidade_cachorros_1(estado_atual): #função utilidade sugerida pelo artigo
    t = 0  # Total de cachorros adjacentes à onça
    p = 0  # Total de cachorros que não podem ser capturados
    posicao_onca = estado_atual.index(-1)

    for i in range(len(matriz_jogo)):
        # Verifica se i é adjacente à onça
        if matriz_jogo[posicao_onca][i] == 1:
            # Verifica se tem um cachorro na casa i
            if estado_atual[i] == 1:
                t += 1  # Um cachorro adjacente
                pode_ser_capturado = False

                for destino, meio in saltos_onca.get(posicao_onca, []):
                # se o cachorro está na casa "meio" e o destino está livre, ele pode ser capturado
                    if meio == i and estado_atual[destino] == 0:
                        pode_ser_capturado = True
                        break

                if not pode_ser_capturado:
                    p += 1  # Está protegido

    # Evita divisão por zero
    if t == 0:
        return 0

    return int(1000 * (p / t))

def utilidade_cachorros_2(estado_atual): #função utilidade sugerida pelo artigo - objetivo quantificar a área livre de movimentação da onça
    posicao_onca = estado_atual.index(-1)
    visitado = [False] * len(estado_atual)
    fila = deque()
    fila.append(posicao_onca)
    area = 0
    visitado[posicao_onca] = True

    while fila:
        casa = fila.popleft()
        area += 1

        for vizinha in range(len(matriz_jogo[casa])): #realiza busca em largura a partir da posição da onça e contabiliza quantas casas ela pode atingir a partir da casa em que ela está
            if matriz_jogo[casa][vizinha] == 1:
                if not visitado[vizinha] and estado_atual[vizinha] == 0:
                    fila.append(vizinha)
                    visitado[vizinha] = True

    valor = 1000 - (area * 100)
    return max(-1000, min(1000, valor))


def utilidade_cachorros_3(estado_atual): ## função que junta as duas funções do artigo com utilização de pesos

    #valor das funções de utilidade
    u1 = utilidade_cachorros_1(estado_atual)
    u2 = utilidade_cachorros_2(estado_atual)

    #pesos
    w1 = 0.4 
    w2 = 0.6

    valor = w1 * u1 + w2 * u2
    return int(max(-1000, min(1000, valor)))



#Função que gera os estados os estados futuros da onça, tem como entrada o estado atual do tabuleiro
#Retorna um vetor com todos os movimentos possiveis da onça a partir do estado atual
def gerar_estados_futuros_onca(estado_atual):
    filhos = []
    posicao_onca = estado_atual.index(-1)
    movimentos = movimentos_validos_onca(posicao_onca, estado_atual, saltos_onca)

    for posicao_destino in movimentos:
        nova_estado = estado_atual.copy()

        # Trata captura
        if matriz_jogo[posicao_onca][posicao_destino] == 0: #Verifica se foi um salto
                   for destino, meio in saltos_onca.get(posicao_onca, []): #Encontra Cachorro Saltado
                        if destino == posicao_destino:
                                if nova_estado[meio] == 1:
                                    nova_estado[meio] = 0  #Remove o cachorro capturado
                                    break

        nova_estado[posicao_onca] = 0
        nova_estado[posicao_destino] = -1

        filhos.append(nova_estado)
    #print("Jogadas possíveis da onça:", len(filhos))


    return filhos



#Função que gera os estados os estados futuros dos cachorros, tem como entrada o estado atual do tabuleiro
#Retorna um vetor com todos os movimentos possiveis dos cachrros a partir do estado atual
def gerar_estados_futuros_cachorros(estado_atual):
    filhos = []

    for posicao, peca in enumerate(estado_atual):
        if peca == 1:  # Se encontrar um cachorro
            destinos_validos = movimentos_validos_cachorros(posicao, estado_atual)

            for destino in destinos_validos:
                novo_estado = estado_atual.copy()
                novo_estado[posicao] = 0  # Remove o cachorro da posição atual
                novo_estado[destino] = 1  # Coloca o cachorro na nova posição
                filhos.append(novo_estado)

    return filhos


def falta_de_combatividade(turnos_jogador):
    """
    Detecta empate por falta de combatividade.
    
    :param turnos_jogador: Lista onde cada elemento representa o conjunto de posições 
                           ocupadas pelo jogador em um turno (ex: [{10}, {11}, {10}, ...])
    :return: True se houve falta de combatividade, False caso contrário.
    """
    C = set()
    p = 0

    for movimento in turnos_jogador:
        if movimento in C:
            p += 1  # Movimento exato repetido
        else:
            C.add(movimento)
    return p >= len(C) / 2

#Função minimax retorna a melhor jogada com base na função objetiva
#Tem como entrada o estado atual do jogo, um booleano para identificar qual jogador será maximizado e a profundidade da árvore gerada.
def minimax(estado_atual, maximizador, profundidade, func_utilidade, alpha=float('-inf'), beta=float('inf')):
    global nos_visitados
    nos_visitados += 1

    # Checar condição de parada (profundidade ou vitória)
    if profundidade == 0 or condicao_vitoria(estado_atual.index(-1), estado_atual) in ["Vitória dos Cachorros", "Vitória da Onça"]:
        utilidade = func_utilidade(estado_atual)
        return utilidade, estado_atual

    if maximizador:
        maior_avaliacao = float('-inf')
        melhores_estados = []
        for filho in gerar_estados_futuros_onca(estado_atual):
            avaliacao, _ = minimax(filho, False, profundidade - 1, func_utilidade, alpha, beta)
            if avaliacao > maior_avaliacao:
                maior_avaliacao = avaliacao
                melhores_estados = [filho]
            elif avaliacao == maior_avaliacao:
                melhores_estados.append(filho)
            
            alpha = max(alpha, avaliacao)
            if beta <= alpha:
                break  # poda beta

        melhor_estado = random.choice(melhores_estados)
        #print(f"Valor: {maior_avaliacao}, Melhor Posição: {melhor_estado.index(-1)}, Estado do tabuleiro: {melhor_estado}")
        return maior_avaliacao, melhor_estado

    else:
        menor_avaliacao = float('inf')
        melhores_estados = []
        for filho in gerar_estados_futuros_cachorros(estado_atual):
            avaliacao, _ = minimax(filho, True, profundidade - 1, func_utilidade, alpha, beta)
            if avaliacao < menor_avaliacao:
                menor_avaliacao = avaliacao
                melhores_estados = [filho]
            elif avaliacao == menor_avaliacao:
                melhores_estados.append(filho)
            
            beta = min(beta, avaliacao)
            if beta <= alpha:
                break  # poda alfa

        melhor_estado = random.choice(melhores_estados)
        #print(f"Valor: {menor_avaliacao}, Posição: {melhor_estado.index(-1)}, Estado do tabuleiro: {melhor_estado}")
        return menor_avaliacao, melhor_estado



#Função minimax retorna a melhor jogada com base na função objetiva
#Tem como entrada o estado atual do jogo, um booleano para identificar qual jogador será maximizado e a profundidade da árvore gerada.
def minimax_cachorro(estado_atual, maximizador, profundidade, func_utilidade, alpha=float('-inf'), beta=float('inf')):
    global nos_visitados
    nos_visitados += 1

    # Checar condição de parada (profundidade ou vitória)
    if profundidade == 0 or condicao_vitoria(estado_atual.index(-1), estado_atual) in ["Vitória dos Cachorros", "Vitória da Onça"]:
        utilidade = func_utilidade(estado_atual)
        return utilidade, estado_atual

    if maximizador:
        maior_avaliacao = float('-inf')
        melhores_estados = []
        for filho in gerar_estados_futuros_cachorros(estado_atual):
            avaliacao, _ = minimax_cachorro(filho, False, profundidade - 1, func_utilidade, alpha, beta)
            if avaliacao > maior_avaliacao:
                maior_avaliacao = avaliacao
                melhores_estados = [filho]
            elif avaliacao == maior_avaliacao:
                melhores_estados.append(filho)
            
            alpha = max(alpha, avaliacao)
            if beta <= alpha:
                break  # poda beta

        melhor_estado = random.choice(melhores_estados)
        #print(f"Valor: {maior_avaliacao}, Melhor Posição: {melhor_estado.index(-1)}, Estado do tabuleiro: {melhor_estado}")
        return maior_avaliacao, melhor_estado

    else:
        menor_avaliacao = float('inf')
        melhores_estados = []
        for filho in gerar_estados_futuros_onca(estado_atual):
            avaliacao, _ = minimax_cachorro(filho, True, profundidade - 1, func_utilidade, alpha, beta)
            if avaliacao < menor_avaliacao:
                menor_avaliacao = avaliacao
                melhores_estados = [filho]
            elif avaliacao == menor_avaliacao:
                melhores_estados.append(filho)
            
            beta = min(beta, avaliacao)
            if beta <= alpha:
                break  # poda alfa

        melhor_estado = random.choice(melhores_estados)
        #print(f"Valor: {menor_avaliacao}, Posição: {melhor_estado.index(-1)}, Estado do tabuleiro: {melhor_estado}")
        return menor_avaliacao, melhor_estado

def draw_board():
    screen.blit(fundo_jogo,(0,0))

    # Desenha as Arestas
    for i in range(31):
        for j in range(i+1, 31):
            if matriz_jogo[i][j] == 1:
                pygame.draw.line(screen, BRANCO, vertex_positions[i], vertex_positions[j], 2)

    # Desenha os Vértices e as peças
    for i, pos in enumerate(vertex_positions):
        pygame.draw.circle(screen, CINZA, pos, 20)
        if estado_do_jogo[i] == 1:
            rect = peca_cachorro.get_rect(center=pos)
            screen.blit(peca_cachorro, rect)
        elif estado_do_jogo[i] == -1:
            rect = peca_onca.get_rect(center=pos)
            screen.blit(peca_onca, rect)
            

    # Indica visualmente qual peça esta selecionada
    if selected is not None:
        pygame.draw.circle(screen, AZUL, vertex_positions[selected], 30, 3)

    # Mostra o número de turnos
    font = pygame.font.SysFont(None, 36)
    txt_Nturnos = font.render(f"Nº de Turnos: {cont_turno}", True, BRANCO)
    screen.blit(txt_Nturnos, (20,20))

    # Mostra de quem é o turno (Onça ou Cachorros)
    texto = font.render(f"Turno: {'Onça' if turno == -1 else 'Cachorros'}", True, BRANCO)
    screen.blit(texto, (20, 60))

    # Exibe a Contagem de capturas
    txt_captura = font.render(f"Capturados: {capturados}/5", True, BRANCO)
    screen.blit(txt_captura, (20, 100))

    # Exibe a mensagem de Fim de jogo
    if fim_de_jogo:
        screen.blit(fundo_jogo, (0,0))

        txt_fim_onca = [
                f"FIM DE JOGO! {vencedor}",
                f"Depois de {cont_turno} turnos",
                f"Capturou {capturados} Cachorros",
                "Pressione ESC para voltar ao menu inicial"
            ]
            
        txt_fim_cachorros = [
            f"FIM DE JOGO! {vencedor},",
            f"Depois de {cont_turno} turnos",
            f"Sacrificou {capturados} Cachorros",
            "Pressione ESC para voltar ao menu inicial"
        ]

        txt_nao_concluida = [
            f"FIM DE JOGO! {vencedor},",
            f"Depois de {cont_turno} turnos",
            "Pressione ESC para voltar ao menu inicial"
        ]

        txt_falta_combatividade_onca = [
            f"FIM DE JOGO! {vencedor},",
            f"Depois de {cont_turno} turnos",
            "Pressione ESC para voltar ao menu inicial"
        ]
        
        txt_falta_combatividade_cachorro = [
            f"FIM DE JOGO! {vencedor},",
            f"Depois de {cont_turno} turnos",
            "Pressione ESC para voltar ao menu inicial"
        ]



        if vencedor == "Vitória da Onça":
            txt_fim = txt_fim_onca
        elif vencedor == "Vitória dos Cachorros":
            txt_fim = txt_fim_cachorros
        elif vencedor == "Partida não concluída":
            txt_fim = txt_nao_concluida
        elif vencedor == "Combatividade (Onça)":
            txt_fim = txt_falta_combatividade_onca
        elif vencedor == "Combatividade (Cachorro)":
            txt_fim = txt_falta_combatividade_cachorro

        for i, linha in enumerate(txt_fim):
            txt = font.render(linha, True, BRANCO)
            screen.blit(txt, (400,300 + i * 50))



def get_vertex_clicked(mouse_pos):
    # Verifica se o clique está próximo de algum vértice (raio de 15px)
    for i, pos in enumerate(vertex_positions):
        dist = (mouse_pos[0] - pos[0]) ** 2 + (mouse_pos[1] - pos[1]) ** 2
        if dist <= 20 ** 2:
            return i
    return None


#Função que executa o movimento das peças
def move_piece(from_idx, to_idx):
    global capturados

    # Movimento normal
    if matriz_jogo[from_idx][to_idx] == 1 and estado_do_jogo[to_idx] == 0:
        estado_do_jogo[to_idx] = estado_do_jogo[from_idx]
        estado_do_jogo[from_idx] = 0
        return True

    # Captura (só onça pode)
    if estado_do_jogo[from_idx] == -1 and estado_do_jogo[to_idx] == 0:
        movimento = movimentos_validos_onca(estado_do_jogo.index(-1),estado_do_jogo,saltos_onca)
        if to_idx in movimento:
            if matriz_jogo[from_idx][to_idx] == 0: #Verifica se foi um salto
                for destino, meio in saltos_onca.get(from_idx, []): #Encontra Cachorro Saltado
                        if destino == to_idx:
                                if estado_do_jogo[meio] == 1:
                                    estado_do_jogo[meio] = 0  #Remove o cachorro capturado
                                    estado_do_jogo[from_idx] = 0
                                    estado_do_jogo[to_idx] = -1
                                    capturados += 1
                                    break
                return True
    return False


aguardando_movimento_ia = False
tempo_inicio_espera = 0

def adugo_run_player_vs_onca(profundidade):
    global selected, turno, fim_de_jogo, vencedor, aguardando_movimento_ia, tempo_inicio_espera, nos_visitados, cont_turno, capturados
    global estado_do_jogo

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and not fim_de_jogo and turno == 1:  # Turno Manual cachorros
                
                idx = get_vertex_clicked(pygame.mouse.get_pos())
                if idx is not None:
                    if selected is None:
                        if estado_do_jogo[idx] == turno:
                            selected = idx
                    else:
                        if move_piece(selected, idx):
                            cont_turno +=1
                            resultado = condicao_vitoria(estado_do_jogo.index(-1), estado_do_jogo)
                            if resultado in ["Vitória da Onça", "Vitória dos Cachorros"]:
                                fim_de_jogo = True
                                vencedor = resultado
                            if not fim_de_jogo:
                                turno = -1  # Troca para a Onça
                                aguardando_movimento_ia = False  # Reinicia delay da IA
                            selected = None
                        else:
                            selected = None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    estado_do_jogo = inicializacao()
                    fim_de_jogo = False
                    vencedor = None 
                    selected = None
                    turno = -1  # Onça começa
                    capturados = 0
                    nos_visitados = 0
                    cont_turno = 0
                    return "menu"
                    

        # Movimento automático da Onça (jogada da IA)
        if turno == -1 and not fim_de_jogo:
            
            if not aguardando_movimento_ia:
                tempo_inicio_espera = pygame.time.get_ticks()
                aguardando_movimento_ia = True
            elif pygame.time.get_ticks() - tempo_inicio_espera >= 500:  # Tempo de delay
                inicio = time.time()  
                valor, melhor_jogada = minimax(estado_do_jogo, True, profundidade, utilidade_onca_2)
                fim = time.time()

                print(f"Tempo de execução: {fim - inicio:.4f} segundos")
                print(f"Nós visitados: {nos_visitados}")
                nos_visitados = 0

                pygame.time.delay(2000)  # Delay extra

                destino = melhor_jogada.index(-1)
                origem = estado_do_jogo.index(-1)
                move_piece(origem, destino)
                cont_turno +=1

                resultado = condicao_vitoria(estado_do_jogo.index(-1), estado_do_jogo)
                if resultado in ["Vitória da Onça", "Vitória dos Cachorros"]:
                    fim_de_jogo = True
                    vencedor = resultado

                turno = 1  # Volta para os Cachorros
                selected = None

        draw_board()  # Desenha tudo na tela

        
        pygame.display.flip()  # Atualiza a janela
        clock.tick(60)  # Limita para 60 FPS


def adugo_run_player_vs_cachorros(profundidade):
    global selected, turno, fim_de_jogo, vencedor, aguardando_movimento_ia, tempo_inicio_espera, nos_visitados, cont_turno, capturados
    global estado_do_jogo

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    estado_do_jogo = inicializacao()
                    fim_de_jogo = False
                    vencedor = None 
                    selected = None
                    turno = -1  # Onça começa
                    capturados = 0
                    nos_visitados = 0
                    cont_turno = 0
                    return "menu"

            # Turno manual da Onça (player)
            elif event.type == pygame.MOUSEBUTTONDOWN and not fim_de_jogo and turno == -1: 
                idx = get_vertex_clicked(pygame.mouse.get_pos())
                if idx is not None:
                    if estado_do_jogo[idx] == -1 and selected is None:
                        selected = idx
                    else:
                        if move_piece(selected, idx):
                            cont_turno +=1
                            resultado = condicao_vitoria(estado_do_jogo.index(-1), estado_do_jogo)
                            if resultado in ["Vitória da Onça", "Vitória dos Cachorros"]:
                                fim_de_jogo = True
                                vencedor = resultado
                            if not fim_de_jogo:
                                turno = 1  # Troca para os cachorros (IA)
                                aguardando_movimento_ia = False  # Reinicia delay da IA
                            selected = None
                        else:
                            selected = None

        # Movimento automático dos cachorros (jogada da IA)
        if turno == 1 and not fim_de_jogo:
            
            if not aguardando_movimento_ia:
                tempo_inicio_espera = pygame.time.get_ticks()
                aguardando_movimento_ia = True
            elif pygame.time.get_ticks() - tempo_inicio_espera >= 500:  # Tempo de delay
                inicio = time.time()
                # O minimax agora procura a melhor jogada para o jogador 1 (cachorros)
                valor, melhor_jogada = minimax_cachorro(estado_do_jogo, True, profundidade, utilidade_cachorros_2)
                fim = time.time()

                print(f"Tempo de execução: {fim - inicio:.4f} segundos")
                print(f"Nós visitados: {nos_visitados}")
                nos_visitados = 0

                pygame.time.delay(2000)  # Delay extra

                try:
                    # Esta é a parte corrigida para encontrar a origem e o destino
                    diferencas = [i for i, (a, b) in enumerate(zip(estado_do_jogo, melhor_jogada)) if a != b]
                    
                    if not diferencas:
                        print("Erro: A melhor jogada é idêntica ao estado atual do tabuleiro.")
                        fim_de_jogo = True
                        vencedor = "Erro de Jogada (sem movimento)"
                        break

                    origem = [i for i in diferencas if estado_do_jogo[i] == turno and melhor_jogada[i] == 0][0]
                    destino = [i for i in diferencas if estado_do_jogo[i] == 0 and melhor_jogada[i] == turno][0]

                except IndexError:
                    print("Erro ao encontrar jogada. As listas de estados são idênticas ou a lógica está incorreta.")
                    fim_de_jogo = True
                    vencedor = "Erro de Jogada"
                    break

                move_piece(origem, destino)
                cont_turno += 1

                resultado = condicao_vitoria(estado_do_jogo.index(-1), estado_do_jogo)
                if resultado in ["Vitória da Onça", "Vitória dos Cachorros"]:
                    fim_de_jogo = True
                    vencedor = resultado

                turno = -1  # Volta para a Onça (player)
                selected = None

        draw_board()  # Desenha tudo na tela
        pygame.display.flip()  # Atualiza a janela
        clock.tick(60)  # Limita para 60 FPS


num_teste = 99


def adugo_run_ia_vs_ia(
    profundidade_onca,
    profundidade_cachorros,
    utilidade_onca_func,
    utilidade_cachorros_func
):
    global selected, turno, fim_de_jogo, vencedor
    global aguardando_movimento_ia, tempo_inicio_espera, nos_visitados, cont_turno
    global estado_do_jogo, clock
    global capturados
    global num_teste

    # Históricos para detectar falta de combatividade
    historico_onca = []
    historico_cachorros = []

    cont_vitoria_onca = 0
    cont_vitoria_cachorro = 0
    ##med_turnos = 0
    empate = 0
    combatividade_onca = 0
    combatividade_cachorro = 0
    with open("logs_ia_vs_ia.txt", "w", encoding="utf-8"):
        pass  # só abre e fecha, apagando o conteúdo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    estado_do_jogo = inicializacao()
                    fim_de_jogo = False
                    vencedor = None 
                    selected = None
                    turno = -1  # Onça começa
                    capturados = 0
                    nos_visitados = 0
                    cont_turno = 0
                    historico_onca = []
                    historico_cachorros = []
                    return "menu"

        if not fim_de_jogo:
            if not aguardando_movimento_ia:
                tempo_inicio_espera = pygame.time.get_ticks()
                aguardando_movimento_ia = True

            elif pygame.time.get_ticks() - tempo_inicio_espera >= 500:
                print(f"Turno da {'Onça' if turno == -1 else 'Cachorros'} (IA)")

                inicio = time.time()

                profundidade = profundidade_onca if turno == -1 else profundidade_cachorros
                func_utilidade = utilidade_onca_func if turno == -1 else utilidade_cachorros_func

                #Verifica se é a função de utilidade 0 da onça ou dos cachorros, pois com ela nao é necessário utilizar o minimax
                if func_utilidade == utilidade_cachorros_0:
                    melhor_jogada = utilidade_cachorros_0(estado_do_jogo)
                elif func_utilidade == utilidade_onca_0:
                    melhor_jogada = utilidade_onca_0(estado_do_jogo)
                else:
                    if turno == -1:
                        valor, melhor_jogada = minimax(
                            estado_do_jogo,
                            maximizador = True,
                            profundidade=profundidade,
                            func_utilidade=func_utilidade
                        )
                    else:
                        valor, melhor_jogada = minimax_cachorro(
                            estado_do_jogo,
                            maximizador = True,
                            profundidade=profundidade,
                            func_utilidade=func_utilidade
                        )

                fim = time.time()
                print(f"Tempo de execução: {fim - inicio:.4f} segundos")
                print(f"Nós visitados: {nos_visitados}")
                nos_visitados = 0

                #pygame.time.delay(1000)

                try:
                    # Esta é a parte corrigida para encontrar a origem e o destino
                    diferencas = [i for i, (a, b) in enumerate(zip(estado_do_jogo, melhor_jogada)) if a != b]
                    
                    if not diferencas:
                        print("Erro: A melhor jogada é idêntica ao estado atual do tabuleiro.")
                        fim_de_jogo = True
                        vencedor = "Erro de Jogada (sem movimento)"
                        break

                    origem = [i for i in diferencas if estado_do_jogo[i] == turno and melhor_jogada[i] == 0][0]
                    destino = [i for i in diferencas if estado_do_jogo[i] == 0 and melhor_jogada[i] == turno][0]

                except IndexError:
                    print("Erro ao encontrar jogada. As listas de estados são idênticas ou a lógica está incorreta.")
                    fim_de_jogo = True
                    vencedor = "Erro de Jogada"
                    break

                move_piece(origem, destino)
                cont_turno += 1
                
                if turno == -1:
                    historico_onca.append((origem,destino))
                    print(historico_onca)
                else:
                    historico_cachorros.append((origem,destino))
                    print(historico_cachorros)


                resultado = condicao_vitoria(estado_do_jogo.index(-1), estado_do_jogo)
                 # Empate por falta de combatividade
                if turno == -1 and falta_de_combatividade(historico_onca):
                    fim_de_jogo = True
                    empate = empate + 1
                    combatividade_onca = combatividade_onca + 1 
                    vencedor = "Combatividade (Onça)"
                elif turno == 1 and falta_de_combatividade(historico_cachorros):
                    fim_de_jogo = True
                    empate = empate + 1
                    combatividade_cachorro = combatividade_cachorro + 1 
                    vencedor = "Combatividade (Cachorros)"
                # Vitória normal ou limite de turnos
                elif resultado in ["Vitória da Onça", "Vitória dos Cachorros"] or cont_turno >= 110:
                    fim_de_jogo = True
                    if cont_turno >= 110 and resultado not in ["Vitória da Onça", "Vitória dos Cachorros"]:
                        empate = empate + 1
                        vencedor = "Partida não concluída"
                    elif resultado == "Vitória da Onça":
                        cont_vitoria_onca = cont_vitoria_onca + 1
                        vencedor = resultado
                    elif resultado == "Vitória dos Cachorros":
                        cont_vitoria_cachorro = cont_vitoria_cachorro + 1
                        vencedor = resultado

                if fim_de_jogo:
                    print(f"Fim de jogo: {vencedor}")
                    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    ##med_turnos += cont_turno
                    try:
                        with open("logs_ia_vs_ia.txt", "a", encoding="utf-8") as f:
                            f.write(f"{data_hora} | Turnos: {cont_turno} | Resultado: {vencedor} | Profundidade: {profundidade} | "
                            f"Cachorros Capturados: {capturados}/5 | " 
                            f"Função Onça: {utilidade_onca_func.__name__} | "
                            f"Função Cachorro: {utilidade_cachorros_func.__name__}\n")
                            if(num_teste>0): #LOOP para testar 100x
                                num_teste = num_teste - 1
                                estado_do_jogo = inicializacao()
                                fim_de_jogo = False
                                vencedor = None 
                                selected = None
                                turno = 1  # Onça começa
                                capturados = 0
                                nos_visitados = 0
                                cont_turno = 0
                                historico_onca = []
                                historico_cachorros = []
                            else:
                                # Ao fim dos testes, grava o resumo total

                                f.write("\n===== RESUMO FINAL =====\n")
                                f.write(f"Vitórias Onça: {cont_vitoria_onca}\n")
                                f.write(f"Vitórias Cachorros: {cont_vitoria_cachorro}\n")
                                f.write(f"Partidas não concluidas: {empate}\n")
                                f.write(f"Falta de Combatividade dos Cachorros: {combatividade_cachorro}\n")
                                f.write(f"Falta de Combatividade da Onça: {combatividade_onca}\n")
                                ##f.write(f"Nº médio de Turnos: {med_turnos/100}\n")
                                f.write("========================\n\n")

                    except Exception as e:
                        print(f"Erro ao salvar resultado: {e}")

                turno *= -1
                selected = None
                aguardando_movimento_ia = False

               

        draw_board()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    adugo_run_ia_vs_ia(5,5,utilidade_onca_0,utilidade_cachorros_2)
