'''
Space-Invader

A Space Invader game.  Use the arrow keys (left & right) to move the ship
and spacebar to fire.

Author: Paul Talaga
Date: July 2023

'''
import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Keep the game running or pause it?
running = True
pause = False

# Master score
score = 0

# Background
background = pygame.image.load('background.png')

# Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 1000)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("player.png")
        self.rect = self.surf.get_rect(
            # Position on the bottom of the screen
            center=(SCREEN_WIDTH/2 , 
                    SCREEN_HEIGHT * 9.0/10 )
        )

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("enemy.png")
        self.rect = self.surf.get_rect(
            # Randomly put them on the top third of the screen
            center=(random.randint(SCREEN_WIDTH / 8,SCREEN_WIDTH * 8 / 10) , 
                    random.randint(30, SCREEN_HEIGHT / 3 ))
        )
        # Defines how much the enemies move in a time-step, but also the direction
        self.dir = 20

    def update(self):
        self.rect.move_ip(self.dir, 0)
        # Did it reach the end of the screen?  If so switch direction and move down
        if self.rect.right > SCREEN_WIDTH * 9 / 10:
            self.dir *= -1
            self.rect.move_ip(0, 30)
        elif self.rect.left < SCREEN_WIDTH / 10:
            self.dir *= -1
            self.rect.move_ip(0, 30)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super(Bullet, self).__init__()
        self.surf = pygame.image.load("bullet.png")
        self.rect = self.surf.get_rect(
            # Start the bullet centered on the player
            center=(( player.rect.left + player.rect.right) /2 , 
                    player.rect.top )
        )

    def update(self):
        self.rect.move_ip(0, -25)
        # If it left the screen remove it
        if self.rect.bottom < 0:
            self.kill()

# This holds all sprites for painting on the screen
sprites = pygame.sprite.Group()
# Enemy ship sprites.  Separate group used for collision detection
enemies = pygame.sprite.Group()
# Bullets
bullets = pygame.sprite.Group()

player = Player()
sprites.add( player )

# Start game with a group of enemies, with more added periodically
for i in range(10):
    enemy = Enemy()
    sprites.add(enemy)
    enemies.add(enemy)


font = pygame.font.Font('freesansbold.ttf', 32)

textX=10
textY=10

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x,y):
    score_font = font.render("Score: "+str(score), True, (255,255,255))
    screen.blit(score_font, (x, y))

def game_over_text():
    over_text=over_font.render("GAME OVER",True, (255,255,255))
    screen.blit(over_text, (200, 250))



playerX_change = 0

# Game Loop
while running:
    # RGB: Red, Green, Blue
    screen.fill((0, 0, 0))

    # Background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == ADDENEMY:
            enemy = Enemy()
            sprites.add(enemy)
            enemies.add(enemy)
        # check the key press event and see it is escape, right, left, or space
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT:
                playerX_change = -10
            if event.key == pygame.K_RIGHT:
                playerX_change = +10
            if event.key == pygame.K_SPACE:
                if len(bullets) < 2:  # Limit the number of active bullets
                    b = Bullet(player)
                    sprites.add(b)
                    bullets.add(b)
                    bullet_sound=mixer.Sound('laser.wav')
                    bullet_sound.play()
        # check the pressed key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    # Keep player on the screen
    if player.rect.left > 10 and player.rect.right < SCREEN_WIDTH - 10:
        player.rect.move_ip(playerX_change, 0)

    # See if any bullets hit an enemy
    for bullet in bullets:
        enemy_hit = pygame.sprite.spritecollideany(bullet, enemies)
        if enemy_hit:
            score += 1
            bullet.kill()
            enemy_hit.kill()
    
    # See if any enemies hit the player
    if pygame.sprite.spritecollideany(player, enemies):
        game_over_text()
        pause = True

    if not pause:
        enemies.update()
        bullets.update()

    # Draw all sprites
    for entity in sprites:
        screen.blit(entity.surf, entity.rect)
    show_score(textX, textY)
    pygame.display.flip()
    pygame.display.update()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)
