import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Game")

# Set up the game clock
clock = pygame.time.Clock()

# Set up the player
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5
player = pygame.Rect(player_x, player_y, player_width, player_height)

# Set up the enemy
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, screen_width - enemy_width)
enemy_y = 0
enemy_speed = 3
enemy = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

# Set up the game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.left -= player_speed
    elif keys[pygame.K_RIGHT] and player.right < screen_width:
        player.right += player_speed
    
    # Move the enemy
    enemy.top += enemy_speed
    if enemy.top > screen_height:
        enemy.left = random.randint(0, screen_width - enemy_width)
        enemy.top = 0
    
    # Check for collisions
    if player.colliderect(enemy):
        game_over = True
    
    # Draw the game objects
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), player)
    pygame.draw.rect(screen, (255, 0, 0), enemy)
    pygame.display.update()
    
    # Limit the game speed
    clock.tick(60)

# Clean up Pygame
pygame.quit()