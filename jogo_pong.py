import pygame
import sys
import math  # Para calcular a velocidade total

# Inicializa o Pygame
pygame.init()

# Tamanho da tela
LARGURA = 800
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pong Game")

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (80, 80, 80)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# FPS
clock = pygame.time.Clock()
FPS = 60

# Raquetes
raquete_largura = 10
raquete_altura = 100
raquete_velocidade = 7

# Bola
bola = pygame.Rect(LARGURA//2 - 10, ALTURA//2 - 10, 20, 20)
bola_vel_x = 5
bola_vel_y = 5
bola_vel_aumento = 0.5
vel_max = 30

# Pontuação
pontos1 = 0
pontos2 = 0
fonte = pygame.font.SysFont("Arial", 36)
fonte_vel = pygame.font.SysFont("Arial", 24)

# Desenhar tudo
def desenhar_tela(raquete1, raquete2, bola, pontos1, pontos2, bola_vel_x, bola_vel_y):
    TELA.fill(PRETO)
    pygame.draw.rect(TELA, BRANCO, raquete1)
    pygame.draw.rect(TELA, BRANCO, raquete2)
    pygame.draw.ellipse(TELA, BRANCO, bola)
    pygame.draw.aaline(TELA, BRANCO, (LARGURA // 2, 0), (LARGURA // 2, ALTURA))

    texto1 = fonte.render(str(pontos1), True, BRANCO)
    texto2 = fonte.render(str(pontos2), True, BRANCO)
    TELA.blit(texto1, (LARGURA//4 - texto1.get_width()//2, 20))
    TELA.blit(texto2, (3*LARGURA//4 - texto2.get_width()//2, 20))

    velocidade_atual = math.sqrt(bola_vel_x**2 + bola_vel_y**2)
    texto_vel = fonte_vel.render(f"Velocidade: {velocidade_atual:.2f}", True, BRANCO)
    TELA.blit(texto_vel, (10, 10))

    pygame.display.flip()

# Menu inicial interativo com mouse
def menu_inicial():
    fonte_grande = pygame.font.SysFont("Arial", 50)
    fonte_botao = pygame.font.SysFont("Arial", 36)

    botao_2jog = pygame.Rect(LARGURA//2 - 150, 300, 300, 60)
    botao_ia = pygame.Rect(LARGURA//2 - 150, 380, 300, 60)

    while True:
        TELA.fill(PRETO)
        titulo = fonte_grande.render("PONG GAME", True, BRANCO)
        TELA.blit(titulo, (LARGURA//2 - titulo.get_width()//2, 150))

        pygame.draw.rect(TELA, CINZA, botao_2jog)
        pygame.draw.rect(TELA, CINZA, botao_ia)

        txt_2jog = fonte_botao.render("2 Jogadores", True, BRANCO)
        txt_ia = fonte_botao.render("Jogar contra IA", True, BRANCO)
        TELA.blit(txt_2jog, (botao_2jog.centerx - txt_2jog.get_width()//2, botao_2jog.centery - txt_2jog.get_height()//2))
        TELA.blit(txt_ia, (botao_ia.centerx - txt_ia.get_width()//2, botao_ia.centery - txt_ia.get_height()//2))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_2jog.collidepoint(evento.pos):
                    return "2jogadores"
                if botao_ia.collidepoint(evento.pos):
                    return "IA"

# Reiniciar a bola no centro
def reset_bola(direcao=1):
    global bola_vel_x, bola_vel_y
    bola.center = (LARGURA//2, ALTURA//2)
    bola_vel_x = 5 * direcao
    bola_vel_y = 5

# Menu inicial
modo = menu_inicial()

raquete1 = pygame.Rect(20, ALTURA//2 - raquete_altura//2, raquete_largura, raquete_altura)
raquete2 = pygame.Rect(LARGURA - 30, ALTURA//2 - raquete_altura//2, raquete_largura, raquete_altura)

# Loop principal
while True:
    clock.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and raquete1.top > 0:
        raquete1.y -= raquete_velocidade
    if teclas[pygame.K_s] and raquete1.bottom < ALTURA:
        raquete1.y += raquete_velocidade

    if modo == "2jogadores":
        if teclas[pygame.K_UP] and raquete2.top > 0:
            raquete2.y -= raquete_velocidade
        if teclas[pygame.K_DOWN] and raquete2.bottom < ALTURA:
            raquete2.y += raquete_velocidade
    else:
        erro_da_ia = 25
        alvo = bola.centery + erro_da_ia
        if alvo > raquete2.centery:
            raquete2.y += raquete_velocidade
        elif alvo < raquete2.centery:
            raquete2.y -= raquete_velocidade

    raquete1.clamp_ip(pygame.Rect(0, 0, LARGURA, ALTURA))
    raquete2.clamp_ip(pygame.Rect(0, 0, LARGURA, ALTURA))

    bola.x += bola_vel_x
    bola.y += bola_vel_y

    if bola.colliderect(raquete1):
        bola.left = raquete1.right
        bola_vel_x *= -1
        bola_vel_x += bola_vel_aumento if bola_vel_x > 0 else -bola_vel_aumento
        bola_vel_y += bola_vel_aumento if bola_vel_y > 0 else -bola_vel_aumento

    if bola.colliderect(raquete2):
        bola.right = raquete2.left
        bola_vel_x *= -1
        bola_vel_x += bola_vel_aumento if bola_vel_x > 0 else -bola_vel_aumento
        bola_vel_y += bola_vel_aumento if bola_vel_y > 0 else -bola_vel_aumento

    if bola.top < 0:
        bola.top = 0
        bola_vel_y *= -1
    if bola.bottom > ALTURA:
        bola.bottom = ALTURA
        bola_vel_y *= -1

    vel_total = math.sqrt(bola_vel_x**2 + bola_vel_y**2)
    if vel_total > vel_max:
        fator = vel_max / vel_total
        bola_vel_x *= fator
        bola_vel_y *= fator

    # Pontuação continua — sem pausar
    if bola.left <= 0:
        pontos2 += 1
        reset_bola(direcao=1)
    if bola.right >= LARGURA:
        pontos1 += 1
        reset_bola(direcao=-1)

    desenhar_tela(raquete1, raquete2, bola, pontos1, pontos2, bola_vel_x, bola_vel_y)
