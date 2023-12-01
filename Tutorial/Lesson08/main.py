import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True

# Background
background = pygame.image.load('background.png')

# Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invader with one enemy")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
# Setting up the coordinates based on display screen width and height (800, 600)
playerX = 368
playerY = 480
playerX_change = 0


enemyImg = pygame.image.load("enemy.png")
# Setting up the random coordinates for enemy using rand function and range of numbers
enemyX = random.randint(0, 800)
enemyY = random.randint(30, 100)
enemyX_change = 3
enemyY_change = 20

# Bullet
bulletImg = pygame.image.load("bullet.png")
# Setting up the random coordinates for enemy using rand function and range of numbers
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
# Ready: you don't see the bullet on the screen
# Fire: the bullet is currently moving
bullet_state = "ready"
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX=10
textY=10

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x,y):
    score = font.render("Score: "+str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text=over_font.render("GAME OVER",True, (255,255,255))
    screen.blit(over_text, (200, 250))
    
def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
    if distance < 25:
        return True
    else:
        return False

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Game Loop
while running:
    # RGB: Red, Green, Blue
    screen.fill((0, 0, 0))
    
    # Background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # check the key press event and see it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = +5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        # check the pressed key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX < 1:
        playerX = 1
    elif playerX > 736:
        playerX = 736
    
    enemyX +=enemyX_change


    # Game Over
    if enemyY>440:
        enemyY = 2000
        game_over_text()
        pygame.display.update()
        pygame.time.delay(20)
        break

    if enemyX<=0:
        enemyX_change = 3
        enemyY += enemyY_change 
    elif enemyX>736:
        enemyX_change = -3
        enemyY += enemyY_change 


    collision = isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        explosion_sound = mixer.Sound('explosion.wav')
        explosion_sound.play()
        bulletY = 480
        bullet_state = "ready"
        score_value+=1
        print(score_value)
        enemyX = random.randint(0, 800)
        enemyY = random.randint(30, 100)

    enemy(enemyX,enemyY)
       
    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX,textY)
    pygame.display.update()
