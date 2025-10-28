import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Configurações da janela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Primeiro Jogo")

# Cores (R, G, B)
AZUL = (0, 150, 255)

# Preenche o fundo da tela
tela.fill(AZUL)

# Atualiza a janela
pygame.display.flip()

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
