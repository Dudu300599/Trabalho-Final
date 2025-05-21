import pygame
from Adugo_com_random import adugo_run
pygame.init()

# Configurações
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Jogo da Onça - Menu Principal")
clock = pygame.time.Clock()
font = pygame.font.Font("EldesCordel-Demo.otf", 60)
fonte_grande = pygame.font.Font("EldesCordel-Demo.otf", 90)
icon = pygame.image.load("imagens/icon_onca.png")
pygame.display.set_icon(icon)


# Cores
BRANCO = (255, 255, 255)
VERDE_CLARO = (221, 207, 142)
CREME = (252, 217, 191)
PRETO = (0, 0, 0)
LARANJA = (203, 112, 31)

#background
fundo_menu = pygame.transform.scale(
    pygame.image.load("imagens/Jogo_da_Onca_Padronagem.png").convert(),
    (1280,720)
)

logo = pygame.transform.scale(
    pygame.image.load("imagens/Logo_JogoDaOnca_transparente3.png").convert_alpha(),
    (600,337)
)
fundo_jogo = pygame.transform.scale(
    pygame.image.load("imagens/Tabuleiro_Tabuleiro_Frente.png").convert(),
    (1280,720)
)

regras_img = pygame.transform.scale(
    pygame.image.load("imagens/regras_1280_720px.jpg").convert(),
    (1280,720)
)
   


# Estados possíveis
estado = "menu"  # pode ser: menu, menu_jogando, regras, recordes

# Botões do menu



def desenhar_menu():
    pygame.display.set_caption("Jogo da Onça - Menu Principal")
    screen.blit(fundo_menu, (0,0))
    screen.blit(logo, (325,0))


    opcoes = ["Jogar", "Regras", "Recordes", "Creditos"]
    botoes = []

    mouse = pygame.mouse.get_pos()

    for i, texto in enumerate(opcoes):
        txt_render = font.render(texto, True, CREME)
        rect = txt_render.get_rect(center=(625, 350 + i * 80))
        botoes.append((texto, txt_render, rect))
        cor = VERDE_CLARO if rect.collidepoint(mouse) else CREME
        txt = font.render(texto, True, cor)
        screen.blit(txt, rect)

        
    return botoes

def desenhar_regras():
    pygame.display.set_caption("Jogo da Onça - Regras")
    screen.blit(regras_img,(0,0))
    texto = "Pressione ESC para voltar ao menu"
    txt = pygame.font.Font("EldesCordel-Demo.otf",24).render(texto, True,LARANJA)
    screen.blit(txt, (650,570))

def desenhar_recordes():
    pygame.display.set_caption("Jogo da Onça - Recordes")
    screen.fill(PRETO)
    recordes = [
        "Recordes:",
        "Jogador1 - 3 vitórias",
        "Jogador2 - 2 vitórias",
        "Jogador3 - 1 vitória",
        "Pressione ESC para voltar ao menu."
    ]
    for i, linha in enumerate(recordes):
        txt = pygame.font.SysFont(None, 40).render(linha, True, BRANCO)
        screen.blit(txt, (50, 100 + i * 50))

def desenhar_creditos():
    pygame.display.set_caption("Jogo da Onça - Créditos")
    screen.fill(PRETO)
    conteudo = [
        "Desenvolvido por:",
        "Carlos Eduardo da Silva Santos e Willian Gomes",
        "Diretor de Arte:",
        "Gabriel Ferrari",
        "Pressione ESC para voltar ao menu"
    ]
    for i, linha in enumerate(conteudo):
        txt = pygame.font.SysFont(None, 40).render(linha, True, BRANCO)
        screen.blit(txt, (50, 100 + i * 50))

def desenhar_menu_jogar():
    #botoes do modo de jogo
    opcoes = ["Player vs Player", "Player vs Comp", "Comp vs Comp(fins de estudo)"]
    botoes = []

    for i, texto in enumerate(opcoes):
        txt_render = font.render(texto, True, CREME)
        rect = txt_render.get_rect(center=(625, 350 + i * 80))
        botoes.append((texto, txt_render, rect))
    
    pygame.display.set_caption("Jogo da Onça")
    screen.blit(fundo_menu, (0,0))
    screen.blit(logo, (325,0))

    mouse = pygame.mouse.get_pos()
    for texto, txt_render, rect in botoes:
        cor = VERDE_CLARO if rect.collidepoint(mouse) else CREME
        txt = font.render(texto, True, cor)
        screen.blit(txt, rect)

    return botoes

def eventos_comuns():
    global estado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                estado = "menu"

def eventos_menu(botoes):
    global estado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for texto, _, rect in botoes:
                if rect.collidepoint(event.pos):
                    if texto == "Jogar":
                        estado = "menu_jogando"
                    elif texto == "Regras":
                        estado = "regras"
                    elif texto == "Recordes":
                        estado = "recordes"
                    elif texto == "Creditos":
                        estado = "creditos"
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                estado = "menu"


def eventos_menu_jogar(botoes_jogar):
    global estado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for texto, _, rect in botoes_jogar:
                if rect.collidepoint(event.pos):
                    if texto == "Player vs Player":
                        estado = "menu"
                    elif texto == "Player vs Comp":
                        estado = "jogandovscomp"
                        adugo_run()
                    elif texto == "Comp vs Comp(fins de estudo)":
                        estado = "menu"
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                estado = 'menu'


def menu_loop():
    global estado
    running = True

    while running:
        # Desenha de acordo com o estado
        if estado == "menu":
            botoes = desenhar_menu()
            eventos_menu(botoes)
        elif estado == "regras":
            desenhar_regras()
            eventos_comuns()
        elif estado == "recordes":
            desenhar_recordes()
            eventos_comuns()
        elif estado == "creditos":
            desenhar_creditos()
            eventos_comuns()
        elif estado == "menu_jogando":
            botoes_jogar = desenhar_menu_jogar()
            eventos_menu_jogar(botoes_jogar)
        elif estado == "jogandovscomp":
            resultado = adugo_run()
            estado = resultado
        elif estado == "sair":
            running == False
        

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# --- MAIN ---
if __name__ == "__main__":
    menu_loop()