import pygame
from Adugo_com_random import *

pygame.init()

# Cores
BRANCO = (255, 255, 255)
VERDE_CLARO = (221, 207, 142)
CREME = (252, 217, 191)
PRETO = (0, 0, 0)
LARANJA = (203, 112, 31)
CINZA = (200, 200, 200)

class Recursos:
    def __init__(self):
        self.font = pygame.font.Font("EldesCordel-Demo.otf", 60)
        self.font_pequena = pygame.font.Font("EldesCordel-Demo.otf", 45)
        self.font_creditos = pygame.font.Font("EldesCordel-Demo.otf", 35)
        self.fonte_grande = pygame.font.Font("EldesCordel-Demo.otf", 90)
        self.font_dropdown = pygame.font.SysFont(None, 28)
        self.font_sys = pygame.font.SysFont(None, 40)

        self.fundo_menu = pygame.transform.scale(pygame.image.load("imagens/Jogo_da_Onca_Padronagem.png"), (1280, 720))
        self.logo = pygame.transform.scale(pygame.image.load("imagens/Logo_JogoDaOnca_transparente3.png"), (600, 337))
        self.regras = pygame.transform.scale(pygame.image.load("imagens/regras_1280_720px.jpg"), (1280, 720))

class Tela:
    def __init__(self, jogo):
        self.jogo = jogo
        self.recursos = jogo.recursos

    def desenhar(self):
        pass

    def eventos(self, eventos):
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.jogo.mudar_estado(MenuPrincipal(self.jogo))

class MenuPrincipal(Tela):
    def desenhar(self):
        screen = self.jogo.screen
        screen.blit(self.recursos.fundo_menu, (0, 0))
        screen.blit(self.recursos.logo, (325, 0))
        self.botoes = []
        opcoes = ["Jogar", "Regras", "Creditos"]
        mouse = pygame.mouse.get_pos()
        for i, texto in enumerate(opcoes):
            rect = self.recursos.font.render(texto, True, CREME).get_rect(center=(625, 350 + i * 80))
            cor = VERDE_CLARO if rect.collidepoint(mouse) else CREME
            txt = self.recursos.font.render(texto, True, cor)
            screen.blit(txt, rect)
            self.botoes.append((texto, rect))

    def eventos(self, eventos):
        super().eventos(eventos)
        for event in eventos:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for texto, rect in self.botoes:
                    if rect.collidepoint(event.pos):
                        if texto == "Jogar":
                            self.jogo.mudar_estado(MenuJogar(self.jogo))
                        elif texto == "Regras":
                            self.jogo.mudar_estado(TelaRegras(self.jogo))
                        elif texto == "Creditos":
                            self.jogo.mudar_estado(TelaCreditos(self.jogo))

class MenuJogar(Tela):
    def desenhar(self):
        screen = self.jogo.screen
        screen.blit(self.recursos.fundo_menu, (0, 0))
        screen.blit(self.recursos.logo, (325, 0))
        self.botoes = []
        opcoes = ["Player vs Player", "Player vs Comp", "Comp vs Comp(fins de estudo)"]
        mouse = pygame.mouse.get_pos()
        for i, texto in enumerate(opcoes):
            rect = self.recursos.font.render(texto, True, CREME).get_rect(center=(625, 350 + i * 80))
            cor = VERDE_CLARO if rect.collidepoint(mouse) else CREME
            txt = self.recursos.font.render(texto, True, cor)
            screen.blit(txt, rect)
            self.botoes.append((texto, rect))

    def eventos(self, eventos):
        super().eventos(eventos)
        for event in eventos:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for texto, rect in self.botoes:
                    if rect.collidepoint(event.pos):
                        if texto == "Player vs Player":
                            self.jogo.mudar_estado(MenuPrincipal(self.jogo))
                        elif texto == "Player vs Comp":
                            self.jogo.mudar_estado(MenuSelecaoPlayervsComp(self.jogo))
                        elif texto == "Comp vs Comp(fins de estudo)":
                            self.jogo.mudar_estado(MenuSelecaoCompvsComp(self.jogo))

class MenuSelecaoPlayervsComp(Tela):
    def __init__(self, jogo):
        super().__init__(jogo)
        self.input_rect = pygame.Rect(1000, 490, 40, 40)
        self.active = False
        self.text = "1"
        self.profundidade = 1
        self.erro = ""

    def desenhar(self):
        screen = self.jogo.screen
        screen.blit(self.recursos.fundo_menu, (0, 0))
        screen.blit(self.recursos.logo, (325, 0))
        self.botoes = []

        opcoes = ["Jogar como Onca", "Jogar como Cachorros", "Nivel de profundidade:"]
        mouse = pygame.mouse.get_pos()

        for i, texto in enumerate(opcoes):
            rect = self.recursos.font.render(texto, True, CREME).get_rect(center=(625, 350 + i * 80))
            cor = VERDE_CLARO if rect.collidepoint(mouse) else CREME
            txt = self.recursos.font.render(texto, True, cor)
            screen.blit(txt, rect)
            self.botoes.append((texto, rect))

        # Desenhar campo de texto (TextField)
        cor_input = VERDE_CLARO if self.active else CINZA
        pygame.draw.rect(screen, cor_input, self.input_rect, border_radius=5)
        fonte_input = self.recursos.font_dropdown
        txt_surface = fonte_input.render(self.text, True, PRETO)
        screen.blit(txt_surface, (self.input_rect.x + 10, self.input_rect.y + 10))

        # Exibir erro, se houver
        if self.erro:
            erro_render = fonte_input.render(self.erro, True, LARANJA)
            screen.blit(erro_render, (self.input_rect.x - 300, self.input_rect.y))

    def eventos(self, eventos):
        super().eventos(eventos)

        for event in eventos:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.input_rect.collidepoint(event.pos):
                    self.active = True
                else:
                    self.active = False

                for texto, rect in self.botoes:
                    if rect.collidepoint(event.pos):
                        if texto == "Jogar como Cachorros":
                            valor = int(self.text)
                            self.profundidade = valor
                            adugo_run_player_vs_onca(self.profundidade)
                        if texto == "Jogar como Onca":
                            valor = int(self.text)
                            self.profundidade = valor
                            adugo_run_player_vs_cachorros(self.profundidade)
                      
            elif event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.unicode.isdigit():
                    self.text += event.unicode

                # Limitar o tamanho e validar
                if len(self.text) > 2:
                    self.text = self.text[:2]


UTILIDADES = {
    "utilidade_onca_0": utilidade_onca_0,
    "utilidade_onca_1": utilidade_onca_1,
    "utilidade_onca_2": utilidade_onca_2,
    "utilidade_cachorro_0": utilidade_cachorros_0,
    "utilidade_cachorro_1": utilidade_cachorros_1,
    "utilidade_cachorro_2": utilidade_cachorros_2,
    "utilidade_cachorro_3": utilidade_cachorros_3,
    "utilidade_cachorro_4": utilidade_cachorros_4,
}



class MenuSelecaoCompvsComp(Tela):
    def __init__(self, jogo):
        super().__init__(jogo)
        self.input_rect = pygame.Rect(1000, 490, 40, 40)
        self.active = False
        self.text = "1"
        self.profundidade = 1
        self.erro = ""

        #Profundidade Onça
        self.input_onca_text = "1"
        self.input_onca_rect = pygame.Rect(450,535,120,40)
        self.active_onca = False

        #Profundidade Cachorros
        self.input_cachorro_text = "1"
        self.input_cachorro_rect = pygame.Rect(1130,535,120,40)
        self.active_cachorro = False

        # Estado das seleções das funções de utilidade (nomes REAIS)
        self.utilidade_onca = "utilidade_onca_0"
        self.utilidade_cachorro = "utilidade_cachorro_0"

        # NOVO: Campo para o número de simulações
        self.input_simulacoes_text = "100"
        self.input_simulacoes_rect = pygame.Rect(0, 0, 200, 40) # Posição será centralizada no desenhar
        self.active_simulacoes = False


    def desenhar(self):
        screen = self.jogo.screen
        screen.blit(self.recursos.fundo_menu, (0, 0))
        screen.blit(self.recursos.logo, (325, 0))
        mouse = pygame.mouse.get_pos()

        fonte = self.recursos.font
        fonte_celula = self.recursos.font_dropdown

        # Títulos
        screen.blit(fonte.render("Onca", True, CREME), (256, 250))
        screen.blit(fonte.render("Cachorro", True, CREME), (800, 250))


        self.retangulos_onca = []
        self.retangulos_cachorro = []

        altura_inicial = 350
        espacamento_h = 20  # espaçamento horizontal
        espacamento_v = 50  # espaçamento vertical
        largura_celula = 100
        altura_celula = 40


        # Coluna Onça
        linhas_onca = [[0,1,2]]
        x_onca = 150

        for linhas, linha in enumerate(linhas_onca):
            for colunas, opcao in enumerate(linha):
                x = x_onca + colunas * (largura_celula + espacamento_h)
                y = altura_inicial + linhas * espacamento_v

                rect = pygame.Rect(x,y,largura_celula,altura_celula)
                nome_func = f"utilidade_onca_{opcao}"
                cor = VERDE_CLARO if self.utilidade_onca == nome_func else CINZA

                pygame.draw.rect(screen, cor, rect, border_radius=5)
                texto = fonte_celula.render(str(opcao), True, PRETO)
                screen.blit(texto, texto.get_rect(center=rect.center))

                self.retangulos_onca.append((nome_func, rect))

        #Profundidade Onça
        label_onca = fonte.render("Profunidade:", True, CREME)
        label_onca_rect = label_onca.get_rect(centery=self.input_onca_rect.centery, right=self.input_onca_rect.left - 10)
        screen.blit(label_onca, label_onca_rect)

        pygame.draw.rect(screen, VERDE_CLARO if self.active_onca else CINZA, self.input_onca_rect, border_radius=5)
        txt_onca = fonte_celula.render(self.input_onca_text,True,PRETO)
        screen.blit(txt_onca, txt_onca.get_rect(center=self.input_onca_rect.center))


        #divisoria 
        pygame.draw.line(
            screen,        # superfície
            CREME,         # cor da linha
            (640, 250),    # ponto inicial (x, y) em cima
            (640, 600),    # ponto final (x, y) embaixo
            3              # espessura da linha
        )


        # Coluna Cachorro com layout automático
        # Definimos a grade: cada sublista é uma linha
        linhas_cachorro = [["0", "1","2"], ["3", "4"]]

        x_base = 750
        y_base = altura_inicial
        largura_celula = 100
        altura_celula = 40
        espacamento_h = 20  # espaçamento horizontal
        espacamento_v = 50  # espaçamento vertical

        self.retangulos_cachorro = []

        for row_idx, linha in enumerate(linhas_cachorro):
            for col_idx, opcao in enumerate(linha):
                x = x_base + col_idx * (largura_celula + espacamento_h)
                y = y_base + row_idx * espacamento_v

                rect = pygame.Rect(x, y, largura_celula, altura_celula)
                nome_func = f"utilidade_cachorro_{opcao}"
                cor = VERDE_CLARO if self.utilidade_cachorro == nome_func else CINZA

                pygame.draw.rect(screen, cor, rect, border_radius=5)
                texto = fonte_celula.render(opcao, True, PRETO)
                screen.blit(texto, texto.get_rect(center=rect.center))

                self.retangulos_cachorro.append((nome_func, rect))

        #Profundidade Cachorro
        label_cachorro = fonte.render("Profundidade:", True, CREME)
        label_cachorro_rect = label_cachorro.get_rect(centery=self.input_cachorro_rect.centery, right=self.input_cachorro_rect.left - 10)
        screen.blit(label_cachorro, label_cachorro_rect)

        pygame.draw.rect(screen, VERDE_CLARO if self.active_cachorro else CINZA, self.input_cachorro_rect, border_radius=5)
        txt_cachorro = fonte_celula.render(self.input_cachorro_text,True,PRETO)
        screen.blit(txt_cachorro, txt_cachorro.get_rect(center=self.input_cachorro_rect.center))

        label_simulacoes = fonte.render("Nº de Partidas:", True, CREME)
        label_sim_rect = label_simulacoes.get_rect(center=(screen.get_width() / 2, 590))
        screen.blit(label_simulacoes, (label_sim_rect.x - 120, label_sim_rect.y))
        
        # NOVO: Desenhar campo de número de simulações
        label_simulacoes = fonte.render("Nº de Partidas:", True, CREME)
        label_sim_rect = label_simulacoes.get_rect(center=(screen.get_width() / 2, 590))
        screen.blit(label_simulacoes, (label_sim_rect.x - 120, label_sim_rect.y))
        
        self.input_simulacoes_rect.centery = label_sim_rect.centery
        self.input_simulacoes_rect.left = label_sim_rect.right - 100
        cor_simulacoes = VERDE_CLARO if self.active_simulacoes else CINZA
        pygame.draw.rect(screen, cor_simulacoes, self.input_simulacoes_rect, border_radius=5)
        txt_simulacoes = fonte_celula.render(self.input_simulacoes_text, True, PRETO)
        screen.blit(txt_simulacoes, txt_simulacoes.get_rect(center=self.input_simulacoes_rect.center))

        # Botão iniciar jogo
        label = "Iniciar Jogo"
        botao_surface = fonte.render(label, True, CREME)

        self.botao_iniciar_rect = botao_surface.get_rect(center=(625,660))

        cor = VERDE_CLARO if self.botao_iniciar_rect.collidepoint(mouse) else CREME
        botao_surface = fonte.render(label, True, cor)
        
        screen.blit(botao_surface, self.botao_iniciar_rect)
        

        # Erro onca
        if self.erro:
            erro_render = fonte_celula.render(self.erro, True, LARANJA)
            screen.blit(erro_render, (self.input_onca_rect.x - 300, self.input_onca_rect.y + 50))

        # Erro cachorro
        if self.erro:
            erro_render = fonte_celula.render(self.erro, True, LARANJA)
            screen.blit(erro_render, (self.input_cachorro_rect.x - 300, self.input_cachorro_rect.y + 50))

    def eventos(self, eventos):
        super().eventos(eventos)

        for event in eventos:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Ativar campo da Onça
                if self.input_onca_rect.collidepoint(event.pos):
                    self.active_onca = True
                    self.active_cachorro = False
                # Ativar campo dos Cachorros
                elif self.input_cachorro_rect.collidepoint(event.pos):
                    self.active_cachorro = True
                    self.active_onca = False

                elif self.input_simulacoes_rect.collidepoint(event.pos):
                    self.active_onca = False
                    self.active_cachorro = False
                    self.active_simulacoes = True
                else:
                    self.active_onca = False
                    self.active_cachorro = False

                # Seleção de função de utilidade Onça
                for nome_func, rect in self.retangulos_onca:
                    if rect.collidepoint(event.pos):
                        self.utilidade_onca = nome_func
                        self.erro = ""

                # Seleção de função de utilidade Cachorro
                for nome_func, rect in self.retangulos_cachorro:
                    if rect.collidepoint(event.pos):
                        self.utilidade_cachorro = nome_func
                        self.erro = ""

                # Botão iniciar jogo
                if self.botao_iniciar_rect.collidepoint(event.pos):
                    try:
                        valor_onca = int(self.input_onca_text)
                        valor_cachorro = int(self.input_cachorro_text)
                        num_partidas = int(self.input_simulacoes_text)
                        if valor_onca < 1 or valor_cachorro < 1:
                            self.erro = "Profundidade menor que 1"
                        elif num_partidas < 1: # NOVO: Validação
                            self.erro = "Número de partidas deve ser maior que 0"
                        else:
                            adugo_run_ia_vs_ia(
                                num_simulacoes = num_partidas-1,
                                profundidade_onca=valor_onca,
                                profundidade_cachorros=valor_cachorro,
                                utilidade_onca_func=UTILIDADES[self.utilidade_onca],
                                utilidade_cachorros_func=UTILIDADES[self.utilidade_cachorro],
                            )
                    except ValueError:
                        self.erro = "Valor inválido"

            elif event.type == pygame.KEYDOWN:
                if self.active_onca:
                    if event.key == pygame.K_BACKSPACE:
                        self.input_onca_text = self.input_onca_text[:-1]
                    elif event.unicode.isdigit() and len(self.input_onca_text) < 2:
                        self.input_onca_text += event.unicode

                elif self.active_cachorro:
                    if event.key == pygame.K_BACKSPACE:
                        self.input_cachorro_text = self.input_cachorro_text[:-1]
                    elif event.unicode.isdigit() and len(self.input_cachorro_text) < 2:
                        self.input_cachorro_text += event.unicode

                elif self.active_simulacoes:
                    if event.key == pygame.K_BACKSPACE:
                        self.input_simulacoes_text = self.input_simulacoes_text[:-1]
                    elif event.unicode.isdigit() and len(self.input_simulacoes_text) < 4:
                        self.input_simulacoes_text += event.unicode






class TelaRegras(Tela):
    def desenhar(self):
        self.jogo.screen.blit(self.recursos.regras, (0, 0))
        txt = pygame.font.Font("EldesCordel-Demo.otf", 24).render("Pressione ESC para voltar ao menu", True, LARANJA)
        self.jogo.screen.blit(txt, (650, 570))

class TelaCreditos(Tela):
    def desenhar(self):
        screen = self.jogo.screen
        screen.blit(self.recursos.fundo_menu, (0, 0))
        screen.blit(self.recursos.logo, (325, 0))
        linhas = [
            "Desenvolvido por:",
            "Carlos Eduardo da Silva Santos e Willian Gomes",
            "Diretor de Arte:",
            "Gabriel Ferrari",
            "Pressione ESC para voltar ao menu"
        ]
        for i, linha in enumerate(linhas):
            txt = self.recursos.font_creditos.render(linha, True, CREME)
            self.jogo.screen.blit(txt, (225, 250 + i * 80))

class Jogo:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Jogo da Onça")
        pygame.display.set_icon(pygame.image.load("imagens/icon_onca.png"))
        self.clock = pygame.time.Clock()
        self.recursos = Recursos()
        self.estado = MenuPrincipal(self)

    def mudar_estado(self, novo_estado):
        self.estado = novo_estado

    def run(self):
        while True:
            eventos = pygame.event.get()
            self.estado.eventos(eventos)
            self.estado.desenhar()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    Jogo().run()
