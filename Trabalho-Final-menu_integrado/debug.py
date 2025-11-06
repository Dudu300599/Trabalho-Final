import pygame
import sys
import re
import numpy as np
from collections import deque
import os  # Importado para listar arquivos

# =============================================================================
# 1. REUTILIZAÇÃO DO CÓDIGO ORIGINAL (Adugo_com_random.py)
# Constantes, posições e assets para o replay funcionar
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

# Fontes
font = pygame.font.SysFont(None, 36)
font_btn = pygame.font.SysFont(None, 40)
font_title = pygame.font.SysFont(None, 48)  # Para o menu
font_item = pygame.font.SysFont(None, 32)   # Para o menu


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
# 2. LÓGICA DO REPLAY (Funções principais)
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
  
  # Calcular e desenhar capturas (MODIFICADO)
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
  
  # Dica para voltar
  txt_esc = font.render("Pressione ESC para voltar ao menu", True, BRANCO)
  screen.blit(txt_esc, (20, 100))


def main_replay(caminho_do_log):
  """
  Loop principal do sistema de replay.
  (MODIFICADO para retornar ao menu com ESC)
  """
  
  # 1. Carregar os dados do log
  historico_estados = parse_log(caminho_do_log)
  if not historico_estados:
    print("Saindo do programa, log não pôde ser carregado.")
    return # Volta ao menu
  
  # 2. Variáveis de estado do Replay
  turno_atual = 0 # Este é o ÍNDICE da lista 'historico_estados'
  total_turnos = len(historico_estados) - 1 # O número do último turno

  # 3. Definir área dos botões
  #   (x, y, largura, altura)
  btn_prev = pygame.Rect(20, 650, 150, 50)
  btn_next = pygame.Rect(190, 650, 150, 50)

  # 4. Loop Principal
  running = True
  while running:
    # --- Tratamento de Eventos ---
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit() # Se fechar no X, sai do programa todo
        sys.exit()
      
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          running = False # Quebra o loop e volta ao menu
      
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
    clock.tick(30) # Não precisa de 60 FPS, 30 é o bastantes
  # Fim do loop, não fazemos quit() ou exit() aqui, apenas retornamos.


# =============================================================================
# 3. NOVAS FUNÇÕES (Menu de Seleção)
# =============================================================================

def find_logs(log_directory="logs/ia_vs_ia"):
  """Encontra todos os arquivos .txt no diretório de log."""
  
  # Baseado no seu arquivo de menu, os logs estão em "logs/ia_vs_ia"
  if not os.path.isdir(log_directory):
    print(f"Erro: Diretório de log '{log_directory}' não encontrado.")
    return []
  
  log_files = []
  for filename in os.listdir(log_directory):
    if filename.endswith(".txt"):
      log_files.append(os.path.join(log_directory, filename))
  
  # Ordena pelos mais recentes primeiro (assumindo timestamp no nome)
  log_files.sort(reverse=True) 
  return log_files

def log_selection_menu():
  """
  Loop principal do menu de seleção de logs.
  """
  
  log_files = find_logs()
  if not log_files:
    print("Nenhum arquivo de log encontrado na pasta 'logs/ia_vs_ia'. Saindo.")
    pygame.quit()
    sys.exit()

  # Para paginação
  page = 0
  items_per_page = 15 # Ajuste conforme o tamanho da sua tela/fonte
  
  # Botões de paginação
  btn_prev_page_rect = pygame.Rect(20, 650, 150, 50)
  btn_next_page_rect = pygame.Rect(190, 650, 150, 50)

  while True:
    # Preenche o fundo (pode ser uma imagem ou cor)
    screen.fill(CREME) # Cor de fundo do menu
    
    # Título
    title_surf = font_title.render("Selecione um Log para Replay", True, PRETO)
    screen.blit(title_surf, ( (1280 - title_surf.get_width()) // 2, 20))
    
    # Calcular total de páginas
    total_pages = (len(log_files) - 1) // items_per_page
    
    # Pegar logs da página atual
    start_index = page * items_per_page
    end_index = start_index + items_per_page
    current_page_files = log_files[start_index:end_index]
    
    # Lista para guardar retângulos clicáveis
    clickable_logs = [] 
    
    # Desenhar itens da lista
    y_offset = 80
    mouse_pos = pygame.mouse.get_pos()
    
    for log_path in current_page_files:
      # Pega só o nome do arquivo, não o caminho completo
      log_name = os.path.basename(log_path) 
      item_surf = font_item.render(log_name, True, PRETO)
      item_rect = item_surf.get_rect(topleft=(50, y_offset))
      
      # Feedback visual (hover)
      if item_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, CINZA, item_rect.inflate(10, 2)) # Infla o fundo
      
      screen.blit(item_surf, item_rect)
      clickable_logs.append((log_path, item_rect))
      y_offset += 35 # Espaçamento entre os itens

    # Desenhar controles de página
    page_surf = font_item.render(f"Página {page + 1} / {total_pages + 1}", True, PRETO)
    page_rect = page_surf.get_rect(center=(btn_next_page_rect.right + 100, btn_next_page_rect.centery))
    screen.blit(page_surf, page_rect)
    
    pygame.draw.rect(screen, CINZA, btn_prev_page_rect, border_radius=5)
    screen.blit(font_btn.render("Anterior", True, PRETO), btn_prev_page_rect.move(20, 12))
    
    pygame.draw.rect(screen, CINZA, btn_next_page_rect, border_radius=5)
    screen.blit(font_btn.render("Próximo", True, PRETO), btn_next_page_rect.move(25, 12))

    pygame.display.flip()

    # --- Loop de Eventos do Menu ---
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      
      if event.type == pygame.MOUSEBUTTONDOWN:
        # 1. Checa cliques nos logs
        for log_path, rect in clickable_logs:
          if rect.collidepoint(event.pos):
            print(f"Carregando replay: {log_path}")
            main_replay(log_path) # Chama o replay
            # Quando o replay terminar (ESC), ele voltará para este loop
            break # Para de checar os logs
        
        # 2. Checa cliques na paginação
        if btn_prev_page_rect.collidepoint(event.pos):
          page = max(0, page - 1) # Volta a página, sem ficar negativo
        if btn_next_page_rect.collidepoint(event.pos):
          page = min(total_pages, page + 1) # Avança a página, até o limite

# =============================================================================
# 4. PONTO DE ENTRADA (MODIFICADO)
# =============================================================================
if __name__ == "__main__":
    # Agora, em vez de carregar um log, chamamos o menu de seleção
    log_selection_menu()