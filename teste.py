import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 32)

# Opções pré-definidas
options = ['Opção 1', 'Opção 2', 'Opção 3']
selected_option = options[0]  # Padrão

# Caixa principal
box_rect = pygame.Rect(200, 150, 200, 40)

# Estado da caixa
box_active = False

running = True
while running:
    screen.fill((30, 30, 30))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if box_rect.collidepoint(event.pos):
                box_active = not box_active
            elif box_active:
                # Checa se clicou em alguma das opções
                for i, option in enumerate(options):
                    option_rect = pygame.Rect(box_rect.x, box_rect.y + (i + 1) * box_rect.height, box_rect.width, box_rect.height)
                    if option_rect.collidepoint(event.pos):
                        selected_option = option
                        box_active = False

    # Desenha a caixa principal
    pygame.draw.rect(screen, (70, 70, 70), box_rect)
    text_surf = font.render(selected_option, True, (255, 255, 255))
    screen.blit(text_surf, (box_rect.x + 5, box_rect.y + 5))

    # Se ativo, desenha as opções
    if box_active:
        for i, option in enumerate(options):
            option_rect = pygame.Rect(box_rect.x, box_rect.y + (i + 1) * box_rect.height, box_rect.width, box_rect.height)
            pygame.draw.rect(screen, (100, 100, 100), option_rect)
            option_surf = font.render(option, True, (255, 255, 255))
            screen.blit(option_surf, (option_rect.x + 5, option_rect.y + 5))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
