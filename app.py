import pygame
import sys

# Inicialização
pygame.init()
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("O Jogo Mais Difícil do Mundo")

# Carregar Mídia
imagem_fundo = pygame.image.load("fundo.jpg")
imagem_susto = pygame.image.load("susto.jpg")
# Redimensionar a foto do susto para ocupar a tela toda
imagem_susto = pygame.transform.scale(imagem_susto, (largura, altura))

som_estourado = pygame.mixer.Sound("grito.mp3")

# Cores e Variáveis do Jogador
BRANCO = (255, 255, 255)
jogador_pos = [50, 50]
ponto_final = pygame.Rect(700, 500, 50, 50) # Onde o susto acontece

rodando = True
sustou = False

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    if not sustou:
        # Movimentação básica (Setas)
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]: jogador_pos[0] -= 5
        if teclas[pygame.K_RIGHT]: jogador_pos[0] += 5
        if teclas[pygame.K_UP]:    jogador_pos[1] -= 5
        if teclas[pygame.K_DOWN]:  jogador_pos[1] += 5

        # Desenhar cenário e jogador
        tela.blit(imagem_fundo, (0, 0))
        pygame.draw.rect(tela, (255, 0, 0), (jogador_pos[0], jogador_pos[1], 20, 20))
        pygame.draw.rect(tela, (0, 255, 0), ponto_final) # Objetivo

        # Checar se chegou no final
        corpo_jogador = pygame.Rect(jogador_pos[0], jogador_pos[1], 20, 20)
        if corpo_jogador.colliderect(ponto_final):
            sustou = True
            som_estourado.play() # Toca o áudio
    else:
        # Exibe a foto do susto
        tela.blit(imagem_susto, (0, 0))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()