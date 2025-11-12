import pygame
import sys
import re
import numpy as np
from collections import deque # Necessário para a inicializacao() se fosse mais complexa, mas mantemos por padrão

# =============================================================================
# 1. REUTILIZAÇÃO DO CÓDIGO ORIGINAL (Adugo_com_random.py)
# Copiamos as constantes, posições e assets para o replay funcionar
# =============================================================================

# --- CORES ---
BRANCO = (255, 255, 255)
LARANJA = (203, 112, 31)
VERDE_CLARO = (221, 207, 142)
CREME = (252, 217, 191)
PRETO = (0, 0, 0)
CINZA = (200, 200, 200)
VERMELHO = (200, 50, 50)
AZUL = (50, 50, 200)
AMARELO = (230, 230, 0)

# --- MATRIZ DE ADJACÊNCIA (Necessária para desenhar as linhas) ---
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
(440, 50), (540, 50), (640, 50), (740, 50), (840, 50),
 (440, 150), (540, 150), (640, 150), (740, 150), (840, 150),
(440, 250), (540, 250), (640, 250), (740, 250), (840, 250),
(440, 350), (540, 350), (640, 350), (740, 350), (840, 350),
(440, 450), (540, 450), (640, 450), (740, 450), (840, 450),
(540, 550), (640, 550), (740, 550), (440, 650), (640, 650), (840, 650)
]

# --- FUNÇÃO DE INICIALIZAÇÃO (Para o Turno 0) ---
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

# --- SETUP DO PYGAME E ASSETS ---
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Replay do Jogo da Onça")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
font_btn = pygame.font.SysFont(None, 40)

# Tente carregar as imagens, se falhar, use formas geométricas
try:
    peca_onca = pygame.transform.scale(pygame.image.load("imagens/ONÇA.png"), (50,50))
    peca_cachorro = pygame.transform.scale(pygame.image.load("imagens/CACHORRO.png"), (50,50))
    fundo_jogo = pygame.transform.scale(pygame.image.load("imagens/Tabuleiro_Tabuleiro_Frente.png").convert(),(1280,720))
    IMAGENS_OK = True
except FileNotFoundError:
    print("Aviso: Arquivos de imagem não encontrados. Usando círculos coloridos.")
    IMAGENS_OK = False
    fundo_jogo = pygame.Surface((1280, 720))
    fundo_jogo.fill(CREME) # Um fundo genérico

# =============================================================================
# 2. LÓGICA DO REPLAY
# =============================================================================

def parse_log(nome_arquivo):
 """
 Lê um arquivo de log e extrai a sequência de estados do tabuleiro.
 Retorna uma lista de listas, onde cada lista interna é um estado.
 """
 historico_estados = []
 # Adiciona o "Turno 0" (estado inicial)
 historico_estados.append(inicializacao())

 # Regex para encontrar a linha de estado e capturar o conteúdo
 # r"..." -> string crua
 # \s* -> qualquer espaço em branco
 # \[\[(.*?)\]\] -> captura (.*?) qualquer coisa entre '[[' e ']]'
 regex = re.compile(r"Estado Atual do Tabuleiro:\s*\[\[(.*?)\]\]")
 
 try:
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
     for linha in f:
        match = regex.search(linha)
        if match:
            # Grupo 1 é o conteúdo capturado: "1, 0, -1, ..."
            estado_str = match.group(1)
 
            # Converte a string "1, 0, -1" para a lista de inteiros [1, 0, -1]
            estado_lista = [int(x.strip()) for x in estado_str.split(',')]
            historico_estados.append(estado_lista)
            
    print(f"Log '{nome_arquivo}' carregado. {len(historico_estados) - 1} turnos encontrados.")
    return historico_estados

 except FileNotFoundError:
    print(f"Erro: Arquivo de log '{nome_arquivo}' não encontrado.")
    return None
 except Exception as e:
    print(f"Erro ao ler o log: {e}")
    return None


def draw_replay_ui(estado_do_jogo, turno_num, total_turnos, btn_prev, btn_next):
    """
    Desenha o estado atual do tabuleiro e a interface de replay.
    """
    # --- Desenha Fundo e Linhas ---
    if IMAGENS_OK:
        screen.blit(fundo_jogo,(0,0))
    else:
        screen.fill(CREME) # Fundo genérico

    for i in range(31):
        for j in range(i+1, 31):
            if matriz_jogo[i][j] == 1:
                pygame.draw.line(screen, BRANCO, vertex_positions[i], vertex_positions[j], 2)

    # --- Desenha Vértices e Peças ---
    for i, pos in enumerate(vertex_positions):
        pygame.draw.circle(screen, CINZA, pos, 20) # Círculo base

        if estado_do_jogo[i] == 1: # Cachorro
            if IMAGENS_OK:
                rect = peca_cachorro.get_rect(center=pos)
                screen.blit(peca_cachorro, rect)
            else:
                pygame.draw.circle(screen, LARANJA, pos, 22) # Círculo alternativo
        
        elif estado_do_jogo[i] == -1: # Onça
            if IMAGENS_OK:
                 rect = peca_onca.get_rect(center=pos)
                 screen.blit(peca_onca, rect)
            else:
                pygame.draw.circle(screen, PRETO, pos, 25) # Círculo alternativo

    # --- Desenha UI (Contador e Botões) ---

    # Contador de Turno
    txt_turno = font.render(f"Turno: {turno_num} / {total_turnos}", True, BRANCO)
    screen.blit(txt_turno, (20, 20))

    # Calcular e desenhar capturas
    total_inicial_cachorros = 14 # Baseado na sua função inicializacao()
    cachorros_atuais = estado_do_jogo.count(1)
    capturados = total_inicial_cachorros - cachorros_atuais

    txt_captura = font.render(f"Capturados: {capturados}/5", True, BRANCO)
    screen.blit(txt_captura, (20, 60)) # Posição logo abaixo do contador de turno

    # Botão Anterior
    pygame.draw.rect(screen, CINZA, btn_prev, border_radius=5)
    txt_prev = font_btn.render("Anterior", True, PRETO)
    txt_rect_prev = txt_prev.get_rect(center=btn_prev.center)
    screen.blit(txt_prev, txt_rect_prev)
    
    # Botão Próximo
    pygame.draw.rect(screen, CINZA, btn_next, border_radius=5)
    txt_next = font_btn.render("Próximo", True, PRETO)
    txt_rect_next = txt_next.get_rect(center=btn_next.center)
    screen.blit(txt_next, txt_rect_next)

def main_replay(caminho_do_log):
    """
    Loop principal do sistema de replay.
    """

    # 1. Carregar os dados do log
    historico_estados = parse_log(caminho_do_log)
    if not historico_estados:
        print("Saindo do programa, log não pôde ser carregado.")
        pygame.quit()
        sys.exit()

    # 2. Variáveis de estado do Replay
    turno_atual = 0 # Este é o ÍNDICE da lista 'historico_estados'
    total_turnos = len(historico_estados) - 1 # O número do último turno

    # 3. Definir área dos botões
    # (x, y, largura, altura)
    btn_prev = pygame.Rect(20, 650, 150, 50)
    btn_next = pygame.Rect(190, 650, 150, 50)

    # 4. Loop Principal
    running = True
    while running:
        # --- Tratamento de Eventos ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Evento de clique
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_prev.collidepoint(event.pos):
                    # Voltar turno (não pode ser menor que 0)
                    turno_atual = max(0, turno_atual - 1)
                    print(f"Mostrando Turno {turno_atual}")

                elif btn_next.collidepoint(event.pos):
                    # Avançar turno (não pode passar do total)
                    turno_atual = min(total_turnos, turno_atual + 1)
                    print(f"Mostrando Turno {turno_atual}")

        # --- Lógica de Desenho ---

        # Pega o estado [1, 1, ..., -1, ...] correspondente ao turno atual
        estado_para_desenhar = historico_estados[turno_atual]

        # Chama a função de desenho
        draw_replay_ui(estado_para_desenhar, turno_atual, total_turnos, btn_prev, btn_next)

        # --- Atualização da Tela ---
        pygame.display.flip()
        clock.tick(30) # Não precisa de 60 FPS, 30 é o bastante

    pygame.quit()
    sys.exit()

# =============================================================================
# 3. PONTO DE ENTRADA
# =============================================================================
if __name__ == "__main__":
    # -----------------------------------------------------------------
    # IMPORTANTE: Coloque aqui o nome do arquivo de log que você quer ler.
    # Ele deve estar na mesma pasta que o script replay.py
    # -----------------------------------------------------------------
    NOME_DO_ARQUIVO_LOG = "/Users/wiul/Downloads/log_20251018_173415.txt" # Exemplo! Troque pelo seu.
    # -----------------------------------------------------------------

    # Verifica se foi passado um argumento (opcional)
    if len(sys.argv) > 1:
        arquivo_log = sys.argv[1]
    else:
        arquivo_log = NOME_DO_ARQUIVO_LOG

    main_replay(arquivo_log)
