import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da escala e da tela
ESCALA = 0.133  # Aumentando 33% em relação ao tamanho original
ITEM_LARGURA = int(2314 * ESCALA)
ITEM_ALTURA = int(3500 * ESCALA)
ESPACO_ENTRE_ITENS = 10
COLUNAS_DE_ITENS = 5  # Máximo de itens por categoria

# Dimensões da tela
WIDTH = COLUNAS_DE_ITENS * (ITEM_LARGURA + ESPACO_ENTRE_ITENS) + 200
HEIGHT = 6 * (ITEM_ALTURA + ESPACO_ENTRE_ITENS)  # Aumentado para acomodar todas as categorias

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Vestir Boneca")

# Cores
WHITE = (255, 255, 255)

# Função para redimensionar imagens de acordo com a escala
def redimensionar(imagem):
    return pygame.transform.scale(imagem, (ITEM_LARGURA, ITEM_ALTURA))

# Função para carregar imagens com segurança
def carregar_imagem(nome_arquivo):
    try:
        imagem = pygame.image.load(nome_arquivo)
        return redimensionar(imagem)
    except pygame.error:
        print(f"Erro ao carregar a imagem: {nome_arquivo}")
        return None

# Carregar e redimensionar as imagens
boneca = carregar_imagem("boneca.png")

blusas = [carregar_imagem(f"blusa_{i}.png") for i in range(1, 6)]
partes_baixo = [carregar_imagem(f"parte_baixo_{i}.png") for i in range(1, 6)]
sapatos = [carregar_imagem(f"sapato_{i}.png") for i in range(1, 3)]
cabelos = [carregar_imagem(f"cabelo_{i}.png") for i in range(1, 5)]

# Lista de todos os itens e suas posições iniciais
itens = []

# Organizando as posições iniciais por categoria
for i, blusa in enumerate(blusas):
    if blusa:
        x = 20 + (i % COLUNAS_DE_ITENS) * (ITEM_LARGURA + ESPACO_ENTRE_ITENS)
        y = 20 + 2 * (ITEM_ALTURA + ESPACO_ENTRE_ITENS)
        itens.append((blusa, (x, y)))

for i, parte_baixo in enumerate(partes_baixo):
    if parte_baixo:
        x = 20 + (i % COLUNAS_DE_ITENS) * (ITEM_LARGURA + ESPACO_ENTRE_ITENS)
        y = 20 + 2 * (ITEM_ALTURA + ESPACO_ENTRE_ITENS)
        itens.append((parte_baixo, (x, y)))

for i, sapato in enumerate(sapatos):
    if sapato:
        x = 20 + (i % COLUNAS_DE_ITENS) * (ITEM_LARGURA + ESPACO_ENTRE_ITENS)
        y = 20 + 2 * (ITEM_ALTURA + ESPACO_ENTRE_ITENS)
        itens.append((sapato, (x, y)))

for i, cabelo in enumerate(cabelos):
    if cabelo:
        x = 20 + (i % COLUNAS_DE_ITENS) * (ITEM_LARGURA + ESPACO_ENTRE_ITENS)
        y = 20 + 3 * (ITEM_ALTURA + ESPACO_ENTRE_ITENS)
        itens.append((cabelo, (x, y)))

# Variáveis de arrastar e soltar
item_selecionado = None
offset_x = 0
offset_y = 0

# Função principal
def main():
    global item_selecionado, offset_x, offset_y
    clock = pygame.time.Clock()
    
    while True:
        screen.fill(WHITE)

        # Desenhar a boneca
        if boneca:
            boneca_pos = (WIDTH // 2 - ITEM_LARGURA // 2, HEIGHT // 2 - ITEM_ALTURA // 2)
            screen.blit(boneca, boneca_pos)

        # Desenhar os itens
        for item, pos in itens:
            screen.blit(item, pos)

        # Eventos do Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Clique do mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for i, (item, pos) in enumerate(itens):
                    item_rect = item.get_rect(topleft=pos)
                    if item_rect.collidepoint(mouse_x, mouse_y):
                        item_selecionado = i
                        offset_x = pos[0] - mouse_x
                        offset_y = pos[1] - mouse_y
                        break
            
            # Soltar o mouse
            elif event.type == pygame.MOUSEBUTTONUP:
                item_selecionado = None
            
            # Movimento do mouse
            elif event.type == pygame.MOUSEMOTION:
                if item_selecionado is not None:
                    mouse_x, mouse_y = event.pos
                    new_x = max(0, min(WIDTH - ITEM_LARGURA, mouse_x + offset_x))
                    new_y = max(0, min(HEIGHT - ITEM_ALTURA, mouse_y + offset_y))
                    itens[item_selecionado] = (itens[item_selecionado][0], (new_x, new_y))
        
        pygame.display.flip()
        clock.tick(60)

# Executar o jogo
if __name__ == "__main__":
    main()