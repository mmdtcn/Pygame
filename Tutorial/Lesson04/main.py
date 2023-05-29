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

# Define border line
Color_line = (128, 128, 255)

# Border Line Coordinates
x1_border = 200
y1_border = 2
x2_border = 200
y2_border = 600

# Bullet characteristics
r_bullet = 8
# player state define as ready/fire since only one bullet should get fired on the window
pl_state = 'ready'

# player img
player_img = pygame.image.load('spaceship.png')

# 90 degree rotation of the player
player_img = pygame.transform.rotate(player_img, 270)

PlayerX_Change = 0
PlayerY_Change = 0

def player(X, Y):
    screen.blit(player_img, (X, Y))

def fire_bullet(X, Y):
    pygame.draw.circle(screen, (255, 255, 0), (X, Y), r_bullet, 0)
    pl_state = 'fire'
    #screen.blit(player_img, (X, Y))

running = True

Player_X = 15
Player_Y = 270

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
            if event.key == pygame.K_SPACE and pl_state=='ready':
                pl_state = 'fire'
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PlayerX_Change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                PlayerY_Change = 0

    screen.fill(bg_color)
    screen.blit(bg_img, (0, 0))
    # draw borderline
    pygame.draw.line(screen, Color_line, (x1_border, y1_border), (x2_border, y2_border), 3)
    Player_X += PlayerX_Change
    Player_Y += PlayerY_Change

    # Limit the x movements to the borderline
    if Player_X < 5:
        Player_X = 5
    elif Player_X > x2_border-65:
        Player_X = x2_border-65

    # Limit the y movements to the borderline
    if Player_Y < 5:
        Player_Y = 5
    elif Player_Y > y2_border - 65:
        Player_Y = y2_border - 65

    player(Player_X, Player_Y)
    # initializing the location of the bullet with p;layer location
    if pl_state == 'ready':
        bullet_x = Player_X+70
        bullet_y = Player_Y+32
    # if it is in fire state, bullet should be drawn and its' trajectories get updated
    if pl_state == 'fire':
        fire_bullet(bullet_x, bullet_y)
        bullet_x += 2
        if bullet_x > 800:
            pl_state = 'ready'

    pygame.display.update()
