import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Constantes da tela
LARGURA = 600
ALTURA = 400
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Snake Game")

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (80, 80, 80)

# Tamanho dos blocos
TAMANHO_BLOCO = 20

# Relógio e velocidade
clock = pygame.time.Clock()
velocidade = 10

def gerar_fruta():
    x = random.randint(0, (LARGURA // TAMANHO_BLOCO) - 1) * TAMANHO_BLOCO
    y = random.randint(0, (ALTURA // TAMANHO_BLOCO) - 1) * TAMANHO_BLOCO
    return [x, y]

def mostrar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont('arial', 24)
    texto = fonte.render(f'Pontuação: {pontuacao}', True, BRANCO)
    TELA.blit(texto, (10, 10))

def game_over(pontuacao):
    fonte_grande = pygame.font.SysFont('arial', 40)
    fonte_pequena = pygame.font.SysFont('arial', 28)

    # Botões
    botao_reiniciar = pygame.Rect(LARGURA//2 - 120, 230, 240, 45)
    botao_sair = pygame.Rect(LARGURA//2 - 120, 290, 240, 45)

    while True:
        TELA.fill(PRETO)

        texto1 = fonte_grande.render("PERDESTE!", True, VERMELHO)
        texto2 = fonte_pequena.render(f"Pontuação: {pontuacao}", True, BRANCO)
        TELA.blit(texto1, (LARGURA//2 - texto1.get_width()//2, 120))
        TELA.blit(texto2, (LARGURA//2 - texto2.get_width()//2, 170))

        # Botão Reiniciar
        pygame.draw.rect(TELA, CINZA, botao_reiniciar)
        txt_reiniciar = fonte_pequena.render("Jogar de Novo", True, BRANCO)
        TELA.blit(txt_reiniciar, (botao_reiniciar.centerx - txt_reiniciar.get_width()//2,
                                  botao_reiniciar.centery - txt_reiniciar.get_height()//2))

        # Botão Sair
        pygame.draw.rect(TELA, CINZA, botao_sair)
        txt_sair = fonte_pequena.render("Sair", True, BRANCO)
        TELA.blit(txt_sair, (botao_sair.centerx - txt_sair.get_width()//2,
                             botao_sair.centery - txt_sair.get_height()//2))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_reiniciar.collidepoint(evento.pos):
                    return
                if botao_sair.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()

while True:
    cobra = [[100, 100]]
    direcao = 'DIREITA'
    fruta = gerar_fruta()
    pontuacao = 0

    while True:
        clock.tick(velocidade)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direcao != 'BAIXO':
                    direcao = 'CIMA'
                elif evento.key == pygame.K_DOWN and direcao != 'CIMA':
                    direcao = 'BAIXO'
                elif evento.key == pygame.K_LEFT and direcao != 'DIREITA':
                    direcao = 'ESQUERDA'
                elif evento.key == pygame.K_RIGHT and direcao != 'ESQUERDA':
                    direcao = 'DIREITA'

        x, y = cobra[0]
        if direcao == 'CIMA':
            y -= TAMANHO_BLOCO
        elif direcao == 'BAIXO':
            y += TAMANHO_BLOCO
        elif direcao == 'ESQUERDA':
            x -= TAMANHO_BLOCO
        elif direcao == 'DIREITA':
            x += TAMANHO_BLOCO

        nova_cabeca = [x, y]
        cobra.insert(0, nova_cabeca)

        if nova_cabeca == fruta:
            pontuacao += 1
            fruta = gerar_fruta()
        else:
            cobra.pop()

        if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA or nova_cabeca in cobra[1:]:
            break

        TELA.fill(PRETO)
        for segmento in cobra:
            pygame.draw.rect(TELA, VERDE, pygame.Rect(segmento[0], segmento[1], TAMANHO_BLOCO, TAMANHO_BLOCO))
        pygame.draw.rect(TELA, VERMELHO, pygame.Rect(fruta[0], fruta[1], TAMANHO_BLOCO, TAMANHO_BLOCO))
        mostrar_pontuacao(pontuacao)
        pygame.display.flip()

    game_over(pontuacao)
