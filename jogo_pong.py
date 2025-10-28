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

# FPS
clock = pygame.time.Clock()
FPS = 60

# Raquetes
raquete_largura = 10
raquete_altura = 100
raquete_velocidade = 7  # Jogador e IA usam esta velocidade

# Bola
bola = pygame.Rect(LARGURA//2 - 10, ALTURA//2 - 10, 20, 20)
bola_vel_x = 5
bola_vel_y = 5
bola_vel_aumento = 0.5  # aumento progressivo
vel_max = 30  # LIMITE DE VELOCIDADE DA BOLA

# Pontuação
pontos1 = 0
pontos2 = 0
fonte = pygame.font.SysFont("Arial", 36)
fonte_vel = pygame.font.SysFont("Arial", 24)  # Fonte para velocidade

# Função para desenhar tudo
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

    # Velocidade atual
    velocidade_atual = math.sqrt(bola_vel_x**2 + bola_vel_y**2)
    texto_vel = fonte_vel.render(f"Velocidade: {velocidade_atual:.2f}", True, BRANCO)
    TELA.blit(texto_vel, (10, 10))

    pygame.display.flip()

# Função para mostrar menu inicial
def menu_inicial():
    while True:
        TELA.fill(PRETO)
        titulo = fonte.render("PONG GAME", True, BRANCO)
        opc1 = fonte.render("1 - 2 Jogadores", True, BRANCO)
        opc2 = fonte.render("2 - Jogar contra IA", True, BRANCO)
        TELA.blit(titulo, (LARGURA//2 - titulo.get_width()//2, 150))
        TELA.blit(opc1, (LARGURA//2 - opc1.get_width()//2, 300))
        TELA.blit(opc2, (LARGURA//2 - opc2.get_width()//2, 350))
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    return "2jogadores"
                if evento.key == pygame.K_2:
                    return "IA"

# Função para reiniciar a bola
def reset_bola(direcao=1):
    global bola_vel_x, bola_vel_y
    bola.center = (LARGURA//2, ALTURA//2)
    bola_vel_x = 5 * direcao
    bola_vel_y = 5

# Menu inicial
modo = menu_inicial()

# Posições iniciais das raquetes
raquete1 = pygame.Rect(20, ALTURA//2 - raquete_altura//2, raquete_largura, raquete_altura)
raquete2 = pygame.Rect(LARGURA - 30, ALTURA//2 - raquete_altura//2, raquete_largura, raquete_altura)

# Loop principal
while True:
    clock.tick(FPS)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controles jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and raquete1.top > 0:
        raquete1.y -= raquete_velocidade
    if teclas[pygame.K_s] and raquete1.bottom < ALTURA:
        raquete1.y += raquete_velocidade

    # Movimento da IA / Jogador 2
    if modo == "2jogadores":
        if teclas[pygame.K_UP] and raquete2.top > 0:
            raquete2.y -= raquete_velocidade
        if teclas[pygame.K_DOWN] and raquete2.bottom < ALTURA:
            raquete2.y += raquete_velocidade
    else:
        # IA com atraso e erro — rápida como o jogador
        erro_da_ia = 25
        alvo = bola.centery + erro_da_ia

        if alvo > raquete2.centery:
            raquete2.y += raquete_velocidade
        elif alvo < raquete2.centery:
            raquete2.y -= raquete_velocidade

    # Garantir que as raquetes ficam dentro do ecrã
    raquete1.clamp_ip(pygame.Rect(0, 0, LARGURA, ALTURA))
    raquete2.clamp_ip(pygame.Rect(0, 0, LARGURA, ALTURA))

    # Movimento da bola
    bola.x += bola_vel_x
    bola.y += bola_vel_y

    # Colisão com raquetes
    # se colidir, ajusta posição para fora da raquete (evita embebimento) e inverte x
    if bola.colliderect(raquete1):
        # coloca bola à direita da raquete1
        bola.left = raquete1.right
        bola_vel_x *= -1
        # aumenta velocidade
        bola_vel_x += bola_vel_aumento if bola_vel_x > 0 else -bola_vel_aumento
        bola_vel_y += bola_vel_aumento if bola_vel_y > 0 else -bola_vel_aumento

    if bola.colliderect(raquete2):
        # coloca bola à esquerda da raquete2
        bola.right = raquete2.left
        bola_vel_x *= -1
        # aumenta velocidade
        bola_vel_x += bola_vel_aumento if bola_vel_x > 0 else -bola_vel_aumento
        bola_vel_y += bola_vel_aumento if bola_vel_y > 0 else -bola_vel_aumento

    # Colisão com topo e base: corrige posição e inverte y
    if bola.top < 0:
        bola.top = 0
        bola_vel_y *= -1
    if bola.bottom > ALTURA:
        bola.bottom = ALTURA
        bola_vel_y *= -1

    # **Limite de velocidade aplicado ao vector total**
    vel_total = math.sqrt(bola_vel_x**2 + bola_vel_y**2)
    if vel_total > vel_max:
        fator = vel_max / vel_total
        bola_vel_x *= fator
        bola_vel_y *= fator

    # Pontuação (após correcções — garante que bola não está fora do ecrã ao marcar)
    if bola.left <= 0:
        pontos2 += 1
        reset_bola(direcao=1)
    if bola.right >= LARGURA:
        pontos1 += 1
        reset_bola(direcao=-1)

    desenhar_tela(raquete1, raquete2, bola, pontos1, pontos2, bola_vel_x, bola_vel_y)
