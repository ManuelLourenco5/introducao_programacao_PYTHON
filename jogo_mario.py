import pygame
import sys

pygame.init()

# Tela
LARGURA = 800
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Plataforma 2D Completo")

# Cores
BRANCO = (255, 255, 255)
AZUL = (50, 150, 255)
VERDE = (0, 200, 0)
VERDE_ESCURO = (0, 150, 0)
VERMELHO = (200, 50, 50)
PRETO = (0, 0, 0)
CINZA = (180, 180, 180)
DOURADO = (255, 215, 0)

clock = pygame.time.Clock()
FPS = 60

# Jogador
jogador_largura = 50
jogador_altura = 60

def resetar_jogador():
    return 200, 0, 0, 0

jogador_x, jogador_y, vel_x, vel_y = resetar_jogador()

forca_pulo = -15
gravidade = 0.8
vel_terminal = 12
atracao_horizontal = 0.6
pulo_cortado = 0.5
no_chao = False

# Plataformas fixas
plataformas = [
    pygame.Rect(-200, 500, 2000, 40),
    pygame.Rect(200, 400, 150, 20),
    pygame.Rect(500, 300, 150, 20),
    pygame.Rect(750, 200, 120, 20),
]

# Plataformas móveis
plataformas_moveis = [
    {"rect": pygame.Rect(1000, 350, 150, 20), "vel": 2, "min": 1000, "max": 1300},
    {"rect": pygame.Rect(1400, 250, 120, 20), "vel": -2, "min": 1300, "max": 1600}
]

# Plataforma final
plataforma_final = pygame.Rect(1800, 350, 200, 30)

# Inimigos
inimigos = [
    {"rect": pygame.Rect(300, 460, 40, 40), "vel": 2, "min": 300, "max": 500},
    {"rect": pygame.Rect(1200, 460, 40, 40), "vel": -2, "min": 1150, "max": 1400},
]

# ---------------------------------------------------------
#                     MENU ESTILO PONG
# ---------------------------------------------------------
def menu_inicial():
    fonte_grande = pygame.font.SysFont("Arial", 50)
    fonte_botao = pygame.font.SysFont("Arial", 36)

    botao_play = pygame.Rect(LARGURA//2 - 150, 300, 300, 60)

    while True:
        TELA.fill(PRETO)
        titulo = fonte_grande.render("PLATAFORMA 2D", True, BRANCO)
        TELA.blit(titulo, (LARGURA//2 - titulo.get_width()//2, 150))

        # Botão PLAY
        pygame.draw.rect(TELA, CINZA, botao_play)
        txt_play = fonte_botao.render("PLAY", True, BRANCO)
        TELA.blit(txt_play, (botao_play.centerx - txt_play.get_width()//2,
                              botao_play.centery - txt_play.get_height()//2))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN and botao_play.collidepoint(evento.pos):
                return

# ---------------------------------------------------------
#                 TELA DE VITÓRIA
# ---------------------------------------------------------
def tela_vitoria():
    fonte = pygame.font.SysFont(None, 60)
    pequeno = pygame.font.SysFont(None, 40)

    tempo = 0
    while tempo < 120:  # ~2 segundos
        TELA.fill(BRANCO)

        msg = fonte.render("VOCÊ VENCEU!", True, DOURADO)
        voltar = pequeno.render("Voltando ao menu...", True, PRETO)

        TELA.blit(msg, msg.get_rect(center=(LARGURA//2, 250)))
        TELA.blit(voltar, voltar.get_rect(center=(LARGURA//2, 330)))

        pygame.display.flip()
        clock.tick(60)
        tempo += 1

# Mostrar o menu ao iniciar
menu_inicial()

# ---------------------------------------------------------
#                    LOOP DO JOGO
# ---------------------------------------------------------
while True:
    clock.tick(FPS)

    # ---- EVENTOS ----
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    # Movimento horizontal
    aceleracao_x = 0
    if teclas[pygame.K_LEFT]:
        aceleracao_x = -0.8
    elif teclas[pygame.K_RIGHT]:
        aceleracao_x = 0.8
    else:
        if vel_x > 0: vel_x = max(0, vel_x - atracao_horizontal)
        elif vel_x < 0: vel_x = min(0, vel_x + atracao_horizontal)

    vel_x += aceleracao_x
    vel_x = max(-7, min(7, vel_x))

    jogador = pygame.Rect(jogador_x, jogador_y, jogador_largura, jogador_altura)
    jogador.x += vel_x

    # Colisão lateral plataformas fixas
    for pl in plataformas:
        if jogador.colliderect(pl):
            if vel_x > 0: jogador.right = pl.left
            elif vel_x < 0: jogador.left = pl.right
            vel_x = 0

    # Colisão lateral plataformas móveis
    for mov in plataformas_moveis:
        pl = mov["rect"]
        if jogador.colliderect(pl):
            if vel_x > 0: jogador.right = pl.left
            elif vel_x < 0: jogador.left = pl.right
            vel_x = 0

    jogador_x = jogador.x

    # Movimento vertical
    if teclas[pygame.K_SPACE] and no_chao:
        vel_y = forca_pulo
        no_chao = False

    if not teclas[pygame.K_SPACE] and vel_y < 0:
        vel_y *= pulo_cortado

    vel_y += gravidade
    vel_y = min(vel_y, vel_terminal)
    jogador.y += vel_y
    no_chao = False

    # Colisão vertical plataformas fixas
    for pl in plataformas:
        if jogador.colliderect(pl):
            if vel_y > 0:
                jogador.bottom = pl.top
                no_chao = True
                vel_y = 0
            elif vel_y < 0:
                jogador.top = pl.bottom
                vel_y = 0

    # Colisão vertical plataformas móveis
    for mov in plataformas_moveis:
        pl = mov["rect"]
        if jogador.colliderect(pl):
            if vel_y > 0:
                jogador.bottom = pl.top
                no_chao = True
                vel_y = 0
            elif vel_y < 0:
                jogador.top = pl.bottom
                vel_y = 0

    jogador_y = jogador.y

    # Morte por queda
    if jogador_y > 700:
        menu_inicial()
        jogador_x, jogador_y, vel_x, vel_y = resetar_jogador()
        continue

    # Plataformas móveis
    for mov in plataformas_moveis:
        mov["rect"].x += mov["vel"]
        if mov["rect"].x < mov["min"] or mov["rect"].x > mov["max"]:
            mov["vel"] *= -1

    # Inimigos
    for ini in inimigos:
        ini["rect"].x += ini["vel"]
        if ini["rect"].x < ini["min"] or ini["rect"].x > ini["max"]:
            ini["vel"] *= -1
        if jogador.colliderect(ini["rect"]):
            menu_inicial()
            jogador_x, jogador_y, vel_x, vel_y = resetar_jogador()

    # Vitória: somente ao tocar no topo da plataforma final
    if jogador.bottom >= plataforma_final.top and jogador.top < plataforma_final.top and \
       jogador.right > plataforma_final.left and jogador.left < plataforma_final.right and vel_y >= 0:
        jogador.bottom = plataforma_final.top
        vel_y = 0
        tela_vitoria()
        menu_inicial()
        jogador_x, jogador_y, vel_x, vel_y = resetar_jogador()

    # Câmera
    camera_x = jogador_x - LARGURA // 2
    camera_y = jogador_y - ALTURA // 2

    # Desenho
    TELA.fill(BRANCO)
    for pl in plataformas:
        pygame.draw.rect(TELA, VERDE, (pl.x - camera_x, pl.y - camera_y, pl.width, pl.height))
    for mov in plataformas_moveis:
        pl = mov["rect"]
        pygame.draw.rect(TELA, VERDE_ESCURO, (pl.x - camera_x, pl.y - camera_y, pl.width, pl.height))
    for ini in inimigos:
        pl = ini["rect"]
        pygame.draw.rect(TELA, VERMELHO, (pl.x - camera_x, pl.y - camera_y, pl.width, pl.height))
    pygame.draw.rect(TELA, AZUL, (jogador_x - camera_x, jogador_y - camera_y, jogador_largura, jogador_altura))
    pygame.draw.rect(TELA, DOURADO, (plataforma_final.x - camera_x, plataforma_final.y - camera_y, plataforma_final.width, plataforma_final.height))

    pygame.display.flip()
