import pygame, sys, random

pygame.init()
LARGURA, ALTURA = 600, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo do Galo")

# Cores e fontes
BRANCO = (240, 240, 245)
PRETO = (20, 20, 20)
AZUL = (66, 135, 245)
VERMELHO = (235, 64, 52)
VERDE = (46, 204, 113)
CINZA = (200, 200, 200)
CINZA_ESCURO = (120, 120, 120)
COR_HOVER = (230, 230, 250)

fonte = pygame.font.SysFont("Arial", 80, bold=True)
fonte_titulo = pygame.font.SysFont("Arial", 60, bold=True)
fonte_menu = pygame.font.SysFont("Arial", 40, bold=True)
fonte_turno = pygame.font.SysFont("Arial", 35, bold=True)
fonte_final = pygame.font.SysFont("Arial", 45, bold=True)

# Variáveis de estado
TAMANHO_CELULA = LARGURA // 3
LINHA_LARGURA = 10
tabuleiro = [["" for _ in range(3)] for _ in range(3)]
jogador_atual = "X"
jogo_encerrado = False
vencedor = None
linha_vitoria = None
modo_ia = False
menu_fim = False

# Placar
placar_X = 0
placar_O = 0

# Botões do menu de fim de jogo
botao_reiniciar = None
botao_menu = None

# Funções
def desenhar_tabuleiro():
    TELA.fill(BRANCO)
    for i in range(1, 3):
        pygame.draw.line(TELA, CINZA_ESCURO, (0, i*TAMANHO_CELULA), (LARGURA, i*TAMANHO_CELULA), LINHA_LARGURA)
        pygame.draw.line(TELA, CINZA_ESCURO, (i*TAMANHO_CELULA, 0), (i*TAMANHO_CELULA, ALTURA), LINHA_LARGURA)

    mx, my = pygame.mouse.get_pos()
    if not jogo_encerrado and not menu_fim:
        linha_hover, coluna_hover = my // TAMANHO_CELULA, mx // TAMANHO_CELULA
        if 0 <= linha_hover < 3 and 0 <= coluna_hover < 3 and tabuleiro[linha_hover][coluna_hover] == "":
            pygame.draw.rect(TELA, COR_HOVER, (coluna_hover*TAMANHO_CELULA, linha_hover*TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))

    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] != "":
                texto = fonte.render(tabuleiro[linha][coluna], True, AZUL if tabuleiro[linha][coluna]=="X" else VERMELHO)
                x = coluna*TAMANHO_CELULA + TAMANHO_CELULA//2 - texto.get_width()//2
                y = linha*TAMANHO_CELULA + TAMANHO_CELULA//2 - texto.get_height()//2
                TELA.blit(texto, (x, y))

    if linha_vitoria:
        desenhar_linha_vitoria(*linha_vitoria)

    desenhar_placar()  # mostra placar no topo

    if not modo_ia and not jogo_encerrado and not menu_fim:
        texto_turno = fonte_turno.render(f"Vez do {jogador_atual}", True, AZUL if jogador_atual=="X" else VERMELHO)
        TELA.blit(texto_turno, (LARGURA//2 - texto_turno.get_width()//2, 50))

    if menu_fim:
        desenhar_menu_fim()

def desenhar_placar():
    texto_placar = fonte_turno.render(f"X: {placar_X}  |  O: {placar_O}", True, PRETO)
    TELA.blit(texto_placar, (LARGURA//2 - texto_placar.get_width()//2, 10))

def desenhar_linha_vitoria(tipo, indice):
    esp = TAMANHO_CELULA // 2
    if tipo=="linha":
        y = indice*TAMANHO_CELULA + esp
        pygame.draw.line(TELA, VERDE, (50,y), (LARGURA-50,y), 15)
    elif tipo=="coluna":
        x = indice*TAMANHO_CELULA + esp
        pygame.draw.line(TELA, VERDE, (x,50), (x,ALTURA-50), 15)
    elif tipo=="diag_principal":
        pygame.draw.line(TELA, VERDE, (50,50), (LARGURA-50,ALTURA-50), 15)
    elif tipo=="diag_secundaria":
        pygame.draw.line(TELA, VERDE, (LARGURA-50,50), (50,ALTURA-50), 15)

def checar_vencedor():
    global vencedor, jogo_encerrado, linha_vitoria, menu_fim
    for i in range(3):
        if tabuleiro[i][0]==tabuleiro[i][1]==tabuleiro[i][2]!="" :
            vencedor = tabuleiro[i][0]; linha_vitoria=("linha",i); jogo_encerrado=True; menu_fim=True; return
    for i in range(3):
        if tabuleiro[0][i]==tabuleiro[1][i]==tabuleiro[2][i]!="" :
            vencedor = tabuleiro[0][i]; linha_vitoria=("coluna",i); jogo_encerrado=True; menu_fim=True; return
    if tabuleiro[0][0]==tabuleiro[1][1]==tabuleiro[2][2]!="" :
        vencedor = tabuleiro[0][0]; linha_vitoria=("diag_principal",0); jogo_encerrado=True; menu_fim=True; return
    if tabuleiro[0][2]==tabuleiro[1][1]==tabuleiro[2][0]!="" :
        vencedor = tabuleiro[0][2]; linha_vitoria=("diag_secundaria",0); jogo_encerrado=True; menu_fim=True; return
    if all(cell!="" for row in tabuleiro for cell in row):
        vencedor = None; jogo_encerrado=True; menu_fim=True

def reiniciar_jogo():
    global tabuleiro, jogador_atual, jogo_encerrado, vencedor, linha_vitoria, menu_fim
    tabuleiro = [["" for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogo_encerrado = False
    vencedor = None
    linha_vitoria = None
    menu_fim = False

def jogada_ia():
    vazios = [(l,c) for l in range(3) for c in range(3) if tabuleiro[l][c]==""] 
    if vazios:
        linha, coluna = random.choice(vazios)
        tabuleiro[linha][coluna] = "O"

def menu_inicial():
    global modo_ia
    fade()
    while True:
        TELA.fill(BRANCO)
        titulo = fonte_titulo.render("Jogo do Galo", True, PRETO)
        opc1 = fonte_menu.render("1 Jogador (contra IA)", True, PRETO)
        opc2 = fonte_menu.render("2 Jogadores", True, PRETO)
        rect1 = pygame.Rect(LARGURA//2-180, ALTURA//2-40, 360, 60)
        rect2 = pygame.Rect(LARGURA//2-180, ALTURA//2+50, 360, 60)
        pygame.draw.rect(TELA, CINZA, rect1, border_radius=10)
        pygame.draw.rect(TELA, CINZA, rect2, border_radius=10)
        TELA.blit(titulo, (LARGURA//2 - titulo.get_width()//2,150))
        TELA.blit(opc1, (LARGURA//2 - opc1.get_width()//2, ALTURA//2-35))
        TELA.blit(opc2, (LARGURA//2 - opc2.get_width()//2, ALTURA//2+55))
        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                pygame.quit(); sys.exit()
            if evento.type==pygame.MOUSEBUTTONDOWN:
                if rect1.collidepoint(evento.pos): modo_ia=True; fade(); return
                if rect2.collidepoint(evento.pos): modo_ia=False; fade(); return

def desenhar_menu_fim():
    global botao_reiniciar, botao_menu
    menu_rect = pygame.Rect(LARGURA//2-150, ALTURA//2-120, 300, 300)
    pygame.draw.rect(TELA, CINZA, menu_rect, border_radius=12)
    pygame.draw.rect(TELA, CINZA_ESCURO, menu_rect, 3, border_radius=12)
    texto_resultado = f"{'Empate!' if vencedor is None else f'{vencedor} venceu!'}"
    msg = fonte_final.render(texto_resultado, True, PRETO)
    TELA.blit(msg, (LARGURA//2 - msg.get_width()//2, ALTURA//2 - 100))

    botao_reiniciar = pygame.Rect(LARGURA//2-120, ALTURA//2, 240, 50)
    botao_menu = pygame.Rect(LARGURA//2-120, ALTURA//2+70, 240, 50)

    mx, my = pygame.mouse.get_pos()
    cor1 = CINZA_ESCURO if not botao_reiniciar.collidepoint((mx,my)) else CINZA
    cor2 = CINZA_ESCURO if not botao_menu.collidepoint((mx,my)) else CINZA
    pygame.draw.rect(TELA, cor1, botao_reiniciar, border_radius=8)
    pygame.draw.rect(TELA, cor2, botao_menu, border_radius=8)

    txt1 = fonte_menu.render("Tentar de Novo", True, BRANCO)
    txt2 = fonte_menu.render("Voltar ao Menu", True, BRANCO)
    TELA.blit(txt1, (LARGURA//2 - txt1.get_width()//2, ALTURA//2+5))
    TELA.blit(txt2, (LARGURA//2 - txt2.get_width()//2, ALTURA//2+75))

def fade():
    fade_surface = pygame.Surface((LARGURA, ALTURA))
    fade_surface.fill(BRANCO)
    for alpha in range(0,255,10):
        fade_surface.set_alpha(alpha)
        TELA.blit(fade_surface,(0,0))
        pygame.display.update()
        pygame.time.delay(10)

# Loop principal
clock = pygame.time.Clock()
menu_inicial()

while True:
    desenhar_tabuleiro()
    pygame.display.flip()
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            pygame.quit(); sys.exit()
        elif evento.type==pygame.MOUSEBUTTONDOWN:
            if not jogo_encerrado and not menu_fim:
                x, y = pygame.mouse.get_pos()
                linha, coluna = y // TAMANHO_CELULA, x // TAMANHO_CELULA
                if tabuleiro[linha][coluna]=="":
                    tabuleiro[linha][coluna] = jogador_atual
                    checar_vencedor()
                    if not jogo_encerrado:
                        jogador_atual = "O" if jogador_atual=="X" else "X"
                        if modo_ia and jogador_atual=="O" and not jogo_encerrado:
                            jogada_ia()
                            checar_vencedor()
                            if not jogo_encerrado:
                                jogador_atual="X"
            elif menu_fim:
                mx, my = pygame.mouse.get_pos()
                if botao_reiniciar.collidepoint((mx,my)):
                    # Atualiza placar ao clicar "Tentar de Novo"
                    if vencedor=="X": placar_X += 1
                    elif vencedor=="O": placar_O += 1
                    reiniciar_jogo()
                elif botao_menu.collidepoint((mx,my)):
                    reiniciar_jogo()
                    menu_inicial()
                    placar_X, placar_O = 0, 0  # opcional: reset placar ao voltar ao menu
