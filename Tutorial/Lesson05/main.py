import math
import pygame

pygame.init()


screen_width = 1200
screen_height = 600
# screen setup
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)

# display title and icon setup
pygame.display.set_caption("Lesson5: Adding second player, collision detection")
icon_img = pygame.image.load('icon.png')
pygame.display.set_icon(icon_img)


# background image
bg_img = pygame.image.load('background.jpg')
bg_img = pygame.transform.scale(bg_img, screen_size)
bg_color = (255, 255, 255)

# Define border line
Color_line = (128, 128, 255)

# Border Line Coordinates
# Line 1
x11_border = 150
y11_border = 2
x12_border = 150
y12_border = screen_height

# Line 2
x21_border = screen_width - x11_border
y21_border = 2
x22_border = screen_width - x12_border
y22_border = screen_height


# Bullet characteristics
r1_bullet = 8
# player state define as ready/fire since only one bullet should get fired on the window
pl1_state = 'ready'

# player img
player1_img = pygame.image.load('spaceship.png')

# 90 degree rotation of the first player
player1_img = pygame.transform.rotate(player1_img, 270)

# 180 degree rotation of the second player
player2_img = pygame.transform.rotate(player1_img, 180)

Player1X_Change = 0
Player1Y_Change = 0
collision_text = ''

def collision(X1, Y1, X2, Y2):
    distance = math.sqrt(pow(X1-X2, 2)+pow(Y1-Y2, 2))
    if distance < 50:
        collision_text = 'Hit'
    else:
        collision_text = 'Miss'
    return collision_text

def player(X, Y, player):
    screen.blit(player, (X, Y))

def fire_bullet(X, Y):
    pygame.draw.circle(screen, (255, 255, 0), (X, Y), r1_bullet, 0)
    pl1_state = 'fire'


running = True

# Initial location of the players
Player1_X = 15
Player1_Y = 270

Player2_X = screen_width-80
Player2_Y = 270

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Player1X_Change += 1
            if event.key == pygame.K_LEFT:
                Player1X_Change -= 1
            if event.key == pygame.K_UP:
                Player1Y_Change -= 1
            if event.key == pygame.K_DOWN:
                Player1Y_Change += 1
            if event.key == pygame.K_SPACE and pl1_state == 'ready':
                pl1_state = 'fire'
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Player1X_Change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                Player1Y_Change = 0

    screen.fill(bg_color)
    screen.blit(bg_img, (0, 0))
    # draw borderline
    pygame.draw.line(screen, Color_line, (x11_border, y11_border), (x12_border, y12_border), 3)
    pygame.draw.line(screen, Color_line, (x21_border, y21_border), (x22_border, y22_border), 3)
    Player1_X += Player1X_Change
    Player1_Y += Player1Y_Change

    # Limit the x movements to the borderline
    if Player1_X < 5:
        Player1_X = 5
    elif Player1_X > x12_border-65:
        Player1_X = x12_border-65

    # Limit the y movements to the borderline
    if Player1_Y < 5:
        Player1_Y = 5
    elif Player1_Y > y12_border - 65:
        Player1_Y = y12_border - 65

    player(Player1_X, Player1_Y, player1_img)
    player(Player2_X, Player2_Y, player2_img)
    # initializing the location of the bullet with player location
    if pl1_state == 'ready':
        bullet1_x = Player1_X+70
        bullet1_y = Player1_Y+32
    # if it is in fire state, bullet should be drawn and its trajectories get updated
    if pl1_state == 'fire':
        fire_bullet(bullet1_x, bullet1_y)
        bullet1_x += 2
        # we add 32 pixels as half of the player dimension to compare bullet location with center of the player
        collision_text = collision(Player2_X+32, Player2_Y+32, bullet1_x, bullet1_y)

        if bullet1_x > Player2_X:
            pl1_state = 'ready'
            print("The fire status is: " + collision_text)


    pygame.display.update()
