import pygame

pygame.init()

# screen setup
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)

# display title and icon setup
pygame.display.set_caption("Lesson3: Controlling Player Movement")
icon_img = pygame.image.load('icon.png')
pygame.display.set_icon(icon_img)


# background image
bg_img = pygame.image.load('background.jpg')
bg_img = pygame.transform.scale(bg_img, screen_size)
bg_color = (255, 255, 255)


# font setup for text
fg_color = (0, 255, 0)
bg_color = (0, 0, 128)
my_font = pygame.font.Font('freesansbold.ttf', 32)
my_text = my_font.render('Welcome to My Game', True, fg_color, bg_color)

# text surface object
my_textRect = my_text.get_rect()
# set the center of the rectangular object.
my_textRect.center = (380, 50)


# player img
player_img = pygame.image.load('spaceship.png')

# 90 degree rotation of the player
player_img = pygame.transform.rotate(player_img, 270)

PlayerX_Change = 0
PlayerY_Change = 0

def player(X, Y):
    screen.blit(player_img, (X, Y))

running = True

Player_X = 380
Player_Y = 500

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                PlayerX_Change += 1
            if event.key == pygame.K_LEFT:
                PlayerX_Change -= 1
            if event.key == pygame.K_UP:
                PlayerY_Change -= 1
            if event.key == pygame.K_DOWN:
                PlayerY_Change += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PlayerX_Change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                PlayerY_Change = 0


    screen.fill(bg_color)
    screen.blit(bg_img, (0, 0))
    screen.blit(my_text, my_textRect)
    Player_X += PlayerX_Change
    Player_Y += PlayerY_Change
    player(Player_X, Player_Y)

    pygame.display.update()
