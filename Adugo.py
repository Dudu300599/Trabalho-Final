import pygame
import numpy as np
import sys

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


estado_do_jogo = inicializacao()

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

def movimentos_validos_onca(posicao, posicao_inicial_pecas, matriz_adjacencias, saltos_onca):
    movimentos_possiveis = []
    posicao = int(posicao)

    # Movimentos normais
    for i in range(len(matriz_adjacencias)):
        if matriz_adjacencias[posicao][i] == 1 and posicao_inicial_pecas[i] == 0:
            movimentos_possiveis.append(i)

    # Saltos (capturas)
    for destino, meio in saltos_onca.get(posicao, []):
        if posicao_inicial_pecas[meio] == 1 and posicao_inicial_pecas[destino] == 0:
            movimentos_possiveis.append(destino)

    return movimentos_possiveis


def movimentos_validos_cachorros(posicao,posicao_inicial_pecas, matriz_adjacencias):
  movimentos_possiveis = []
  for i in range(len(matriz_adjacencias)):
    if matriz_adjacencias[posicao][i] == 1: #Verifica se tem aresta entre o vértice atual da peça e outros vértices
        if posicao_inicial_pecas[i] == 0:   #Verifica se a casa adjacente está vazia
          movimentos_possiveis.append(i)    #Adiciona o movimento a lista de movimentos validos
  return movimentos_possiveis

def condicao_vitoria(posicao, posicao_pecas, matriz_adjacencias):
    qnt_cachorros = posicao_pecas.count(1)
    if qnt_cachorros <= 9:
        return "Vitória da Onça"
    if movimentos_validos_onca(posicao, posicao_pecas, matriz_adjacencias,saltos_onca) == []:
        return "Vitória dos Cachorros"
    return None

def utilidade_onca_1(posicao_inicial_pecas): #função utilidade sugerida pelo artigo
  qnt_cachorros = posicao_inicial_pecas.count(1)
  if qnt_cachorros <= 9:
    return 1000
  return 200 * (14-qnt_cachorros)


def gerar_estados_futuros_onca(posicao_inicial_pecas, matriz_adjacencias):
    filhos = []
    pos_onca = posicao_inicial_pecas.index(-1)
    movimentos = movimentos_validos_onca(pos_onca, posicao_inicial_pecas, matriz_adjacencias,saltos_onca)

    for pos_destino in movimentos:
        nova_pos = posicao_inicial_pecas.copy()

        # Trata captura
        if matriz_adjacencias[pos_onca][pos_destino] == 0: #Verifica se foi um salto
                   for destino, meio in saltos_onca.get(pos_onca, []): #Encontra Cachorro Saltado
                        if destino == pos_destino:
                                if nova_pos[meio] == 1:
                                    nova_pos[meio] = 0  #Remove o cachorro capturado
                                    break

        nova_pos[pos_onca] = 0
        nova_pos[pos_destino] = -1

        filhos.append(nova_pos)

    return filhos




def gerar_estados_futuros_cachorros(estado_atual, matriz_adjacencias):
    filhos = []

    for posicao, peca in enumerate(estado_atual):
        if peca == 1:  # Se encontrar um cachorro
            destinos_validos = movimentos_validos_cachorros(posicao, estado_atual, matriz_adjacencias)

            for destino in destinos_validos:
                novo_estado = estado_atual.copy()
                novo_estado[posicao] = 0  # Remove o cachorro da posição atual
                novo_estado[destino] = 1  # Coloca o cachorro na nova posição
                filhos.append(novo_estado)

    return filhos

import math

def minimax_onca(posicao_inicial_pecas, matriz_adjacencias, profundidade):
    def max_value(estado, profundidade):
        if condicao_vitoria(estado.index(-1), estado, matriz_adjacencias) == "Vitória da Onça" or profundidade == 0:
            return utilidade_onca_1(estado), estado
        
        filhos = gerar_estados_futuros_onca(estado, matriz_adjacencias)
        if not filhos:
            return utilidade_onca_1(estado), None  # Não há jogadas possíveis

        v = -math.inf
        melhor_estado = None
        for filho in filhos:
            v2, _ = min_value(filho, profundidade - 1)
            if v2 > v:
                v = v2
                melhor_estado = filho
        #print("Valor Melhor: ",v, "Estado: ",melhor_estado.index(-1))
        return v, melhor_estado

    def min_value(estado, profundidade):
        if condicao_vitoria(estado.index(-1), estado, matriz_adjacencias) == "Vitória dos Cachorros" or profundidade == 0:
            return utilidade_onca_1(estado), estado


        filhos = gerar_estados_futuros_cachorros(estado, matriz_adjacencias)
        if not filhos:
            return utilidade_onca_1(estado), None  # Nenhum movimento
        
        v = math.inf
        pior_estado = None
        for filho in filhos:
            v2, _ = max_value(filho, profundidade - 1)
            if v2 < v:
                v = v2
                pior_estado = filho
        #print("Valor Pior: ",v, "Estado: ",pior_estado.index(-1))
        return v, pior_estado

    _, melhor_estado = max_value(posicao_inicial_pecas, profundidade)
    return melhor_estado


def draw_board():
    screen.fill(WHITE)

    # Arestas
    for i in range(31):
        for j in range(i+1, 31):
            if matriz_jogo[i][j] == 1:
                pygame.draw.line(screen, BLACK, vertex_positions[i], vertex_positions[j], 2)

    # Vértices e peças
    for i, pos in enumerate(vertex_positions):
        pygame.draw.circle(screen, GRAY, pos, 15)
        if estado_do_jogo[i] == 1:
            pygame.draw.circle(screen, RED, pos, 10)
        elif estado_do_jogo[i] == -1:
            pygame.draw.circle(screen, YELLOW, pos, 10)

    # Peça selecionada
    if selected is not None:
        pygame.draw.circle(screen, BLUE, vertex_positions[selected], 20, 3)

    # Turno
    font = pygame.font.SysFont(None, 36)
    texto = font.render(f"Turno: {'Onça' if turno == 2 else 'Cachorros'}", True, BLACK)
    screen.blit(texto, (20, 20))

    # Contagem de capturas
    txt_captura = font.render(f"Capturados: {capturados}/5", True, BLACK)
    screen.blit(txt_captura, (20, 60))

    # Fim de jogo
    if fim_de_jogo:
        txt_fim = font.render(f"FIM DE JOGO! {vencedor}", True, (255, 0, 0))
        screen.blit(txt_fim, (275, 700))

def get_vertex_clicked(mouse_pos):
    for i, pos in enumerate(vertex_positions):
        dist = (mouse_pos[0] - pos[0]) ** 2 + (mouse_pos[1] - pos[1]) ** 2
        if dist <= 15 ** 2:
            return i
    return None

def move_piece(from_idx, to_idx):
    global capturados

    # Movimento normal
    if matriz_jogo[from_idx][to_idx] == 1 and estado_do_jogo[to_idx] == 0:
        estado_do_jogo[to_idx] = estado_do_jogo[from_idx]
        estado_do_jogo[from_idx] = 0
        return True

    # Captura (só onça pode)
    if estado_do_jogo[from_idx] == -1 and estado_do_jogo[to_idx] == 0:
        movimento = movimentos_validos_onca(estado_do_jogo.index(-1),estado_do_jogo,matriz_jogo,saltos_onca)
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

def get_middle_vertex(a, b):
    for mid in range(31):
        if matriz_jogo[a][mid] == 1 and matriz_jogo[mid][b] == 1:
            return mid
    return None




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
                        resultado = condicao_vitoria(estado_do_jogo.index(-1), estado_do_jogo, matriz_jogo)
                        if resultado in ["Vitória da Onça", "Vitória dos Cachorros"]:
                            fim_de_jogo = True
                            vencedor = resultado
                        if not fim_de_jogo:
                            turno = -1  # Troca para a Onça
                        selected = None
                    else:
                        selected = None


    # Movimento automático da Onça (jogada da IA)
    if turno == -1 and not fim_de_jogo:
        melhor_jogada = minimax_onca(estado_do_jogo,matriz_jogo, profundidade=3)  # ajuste a profundidade conforme necessário
        destino = melhor_jogada.index(-1)
        origem = estado_do_jogo.index(-1)
        move_piece(origem, destino)

        resultado = condicao_vitoria(estado_do_jogo.index(-1), estado_do_jogo, matriz_jogo)
        if resultado in ["Vitória da Onça", "Vitória dos Cachorros"]:
            fim_de_jogo = True
            vencedor = resultado

        turno = 1  # Volta para os Cachorros
        selected = None

    draw_board()
    pygame.display.flip()
    clock.tick(60)
