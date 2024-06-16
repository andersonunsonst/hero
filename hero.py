import pygame
import sys

# Inicialização do pygame
pygame.init()

# Definição da janela
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Leitura de Coordenadas de Spritesheet")

# Carregar spritesheet
spritesheet = pygame.image.load("Heroes.gif")

# Definir tamanho do quadro da animação
frame_width = 30
frame_height = 30
zoom_factor = 3  # Fator de zoom

# Coordenadas iniciais do personagem
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2

# Velocidade de movimento do personagem
player_speed = 5
# Direção inicial do personagem
player_direction = "right"  # Pode ser "left" ou "right"

# Função para extrair um quadro da spritesheet em uma coordenada específica
def get_frame(x, y, zoom):
    frame = spritesheet.subsurface((x * frame_width, y * frame_height, frame_width, frame_height))
    return pygame.transform.scale(frame, (frame_width * zoom, frame_height * zoom))

# Coordenada do quadro que você deseja ler da spritesheet
frame_x = 1
frame_y = 0



# Direções de movimento do personagem
move_up = False
move_down = False
move_left = False
move_right = False

# Loop principal do jogo
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_up = True
                player_direction = "up"
            elif event.key == pygame.K_DOWN:
                move_down = True
                player_direction = "down"
            elif event.key == pygame.K_LEFT:
                move_left = True
                player_direction = "left"
            elif event.key == pygame.K_RIGHT:
                player_direction = "right"
                move_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_up = False
            elif event.key == pygame.K_DOWN:
                move_down = False
            elif event.key == pygame.K_LEFT:
                move_left = False
            elif event.key == pygame.K_RIGHT:
                move_right = False

    # Atualizar posição do personagem com base nas teclas pressionadas
    if move_up:
        player_y -= player_speed
    elif move_down:
        player_y += player_speed
    if move_left:
        player_x -= player_speed
    elif move_right:
        player_x += player_speed

    # Limites da tela para o personagem não sair da janela
    player_x = max(0, min(player_x, SCREEN_WIDTH - frame_width))
    player_y = max(0, min(player_y, SCREEN_HEIGHT - frame_height))

    # Renderização
    screen.fill((0, 0, 0))
# Extrair o quadro da spritesheet usando a função get_frame()
  # Desenhar o quadro do personagem na tela
    if player_direction == "left":
        current_frame = pygame.transform.flip(get_frame(frame_x, frame_y, zoom_factor), True, False)  # Flip horizontal
    else:
        current_frame = get_frame(frame_x, frame_y, zoom_factor)
    screen.blit(current_frame, (player_x, player_y))
    pygame.display.flip()

    # Limita a taxa de quadros por segundo
    clock.tick(30)

pygame.quit()
sys.exit()

