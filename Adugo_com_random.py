import pygame
import numpy as np
import sys
import time
import random

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
    (250, 50),  (350, 50),  (450, 50),  (550, 50),  (650, 50),
    (250, 150), (350, 150), (450, 150), (550, 150), (650, 150),
    (250, 250), (350, 250), (450, 250), (550, 250), (650, 250),
    (250, 350), (350, 350), (450, 350), (550, 350), (650, 350),
    (250, 450), (350, 450), (450, 450), (550, 450), (650, 450),
    (350, 550), (450, 550), (550, 550), (250, 650), (450, 650), (650, 650)
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

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (200, 50, 50)
BLUE = (50, 50, 200)
YELLOW = (230, 230, 0)

pygame.init()
screen = pygame.display.set_mode((900, 800))
pygame.display.set_caption("Jogo da Onça")
clock = pygame.time.Clock()

selected = None
turno = -1  # Onça começa
capturados = 0
fim_de_jogo = False
vencedor = None
nos_visitados = 0



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
    print("Jogadas possíveis da onça:", len(filhos))


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


#Função minimax retorna a melhor jogada com base na função objetiva
#Tem como entrada o estado atual do jogo, um booleano para identificar qual jogador será maximizado e a profundidade da árvore gerada.
def minimax(estado_atual, maximizador, profundidade, alpha=float('-inf'), beta=float('inf')):
        global nos_visitados  # Indica que estamos usando a variável global
        nos_visitados += 1 

        if profundidade == 0 or condicao_vitoria(estado_atual.index(-1), estado_atual) == "Vitória dos Cachorros" or condicao_vitoria(estado_atual.index(-1), estado_atual) == "Vitória da Onça":
            utilidade = utilidade_onca_1(estado_atual)
            return utilidade, estado_atual

        if maximizador:
            maior_avaliacao = float('-inf')
            melhores_estados = []
            for filho in gerar_estados_futuros_onca(estado_atual):
                avaliacao, _ = minimax(filho,False, profundidade - 1, alpha, beta)
                if avaliacao > maior_avaliacao:
                    maior_avaliacao = avaliacao
                    melhores_estados = [filho]
                elif avaliacao == maior_avaliacao:
                    melhores_estados.append(filho)
                #Começa Corte Alpha Beta
                if avaliacao >= beta:
                    break
                alpha = max(alpha, avaliacao)
                #Acaba Corte Alpha Beta

            melhor_estado = random.choice(melhores_estados)
            print(f"Valor: {maior_avaliacao}, Melhor Posição: {melhor_estado.index(-1)}, Estado do tabuleiro: {melhor_estado}")
            return maior_avaliacao, melhor_estado
        else:
            menor_avaliacao = float('inf')
            melhores_estados = []
            for filho in gerar_estados_futuros_cachorros(estado_atual):
                avaliacao, _ = minimax(filho,True, profundidade - 1, alpha, beta)
                if avaliacao < menor_avaliacao:
                    menor_avaliacao = avaliacao
                    melhores_estados = [filho]
                elif avaliacao == menor_avaliacao:
                    melhores_estados.append(filho)
                #Começa Corte Alpha Beta
                if avaliacao <= alpha:
                    break
                beta = min(beta, avaliacao)
                #Acaba Corte Alpha Beta

            melhor_estado = random.choice(melhores_estados)
            print(f"Valor: {menor_avaliacao}, Posição: {melhor_estado.index(-1)}, Estado do tabuleiro: {melhor_estado}")
            return menor_avaliacao, melhor_estado



def draw_board():
    screen.fill(WHITE)

    # Desenha as Arestas
    for i in range(31):
        for j in range(i+1, 31):
            if matriz_jogo[i][j] == 1:
                pygame.draw.line(screen, BLACK, vertex_positions[i], vertex_positions[j], 2)

    # Desenha os Vértices e as peças
    for i, pos in enumerate(vertex_positions):
        pygame.draw.circle(screen, GRAY, pos, 15)
        if estado_do_jogo[i] == 1:
            pygame.draw.circle(screen, RED, pos, 10)
        elif estado_do_jogo[i] == -1:
            pygame.draw.circle(screen, YELLOW, pos, 10)

    # Indica visualmente qual peça esta selecionada
    if selected is not None:
        pygame.draw.circle(screen, BLUE, vertex_positions[selected], 20, 3)

    # Mostra de quem é o turno (Onça ou Cachorros)
    font = pygame.font.SysFont(None, 36)
    texto = font.render(f"Turno: {'Onça' if turno == -1 else 'Cachorros'}", True, BLACK)
    screen.blit(texto, (20, 20))

    # Exibe a Contagem de capturas
    txt_captura = font.render(f"Capturados: {capturados}/5", True, BLACK)
    screen.blit(txt_captura, (20, 60))

    # Exibe a mensagem de Fim de jogo
    if fim_de_jogo:
        txt_fim = font.render(f"FIM DE JOGO! {vencedor}", True, (255, 0, 0))
        screen.blit(txt_fim, (275, 700))


def get_vertex_clicked(mouse_pos):
    # Verifica se o clique está próximo de algum vértice (raio de 15px)
    for i, pos in enumerate(vertex_positions):
        dist = (mouse_pos[0] - pos[0]) ** 2 + (mouse_pos[1] - pos[1]) ** 2
        if dist <= 15 ** 2:
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

#Função que retorna o vértice do meio, quando existe um salto
#Não utilizada, pois o saltos estão sendo mapeados por um dicionario
def get_middle_vertex(a, b):
    for mid in range(31):
        if matriz_jogo[a][mid] == 1 and matriz_jogo[mid][b] == 1:
            return mid
    return None

aguardando_movimento_ia = False
tempo_inicio_espera = 0

# LOOP PRINCIPAL
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
        elif event.type == pygame.MOUSEBUTTONDOWN and not fim_de_jogo and turno == 1: #Turno Manual cachorros
            idx = get_vertex_clicked(pygame.mouse.get_pos())
            if idx is not None:
                if selected is None:
                    if estado_do_jogo[idx] == turno:
                        selected = idx
                else:
                    if move_piece(selected, idx):
                        resultado = condicao_vitoria(estado_do_jogo.index(-1), estado_do_jogo)
                        if resultado in ["Vitória da Onça", "Vitória dos Cachorros"]:
                            fim_de_jogo = True
                            vencedor = resultado
                        if not fim_de_jogo:
                            turno = -1  # Troca para a Onça
                            aguardando_movimento_ia = False  # Garante que o delay seja reiniciado no turno da onça
                        selected = None
                    else:
                        selected = None


    # Movimento automático da Onça (jogada da IA)
    if turno == -1 and not fim_de_jogo:

        if not aguardando_movimento_ia:
            # Inicia o tempo de espera da IA
            tempo_inicio_espera = pygame.time.get_ticks()
            aguardando_movimento_ia = True

        elif pygame.time.get_ticks() - tempo_inicio_espera >= 500: #Tempo de delay
            # Delay passou, IA pode agir
            inicio = time.time()
            valor ,melhor_jogada = minimax(estado_do_jogo,maximizador=True, profundidade=6) # ajuste a profundidade conforme necessário
            fim = time.time()

            print(f"Tempo de execução: {fim - inicio:.4f} segundos") #Exibe tempo de execucao
            print(f"Nós visitados: {nos_visitados}")                 #Exibe nós visitados
            nos_visitados = 0


            pygame.time.delay(2000) #Adiciona delay ao movimento da onça

            destino = melhor_jogada.index(-1)
            origem = estado_do_jogo.index(-1)
            move_piece(origem, destino)

            resultado = condicao_vitoria(estado_do_jogo.index(-1), estado_do_jogo)
            if resultado in ["Vitória da Onça", "Vitória dos Cachorros"]:
                fim_de_jogo = True
                vencedor = resultado

            turno = 1  # Volta para os Cachorros
            selected = None

    draw_board()  # Desenha tudo na tela
    pygame.display.flip() # Atualiza a janela
    clock.tick(60)  # Limita para 60 FPS
