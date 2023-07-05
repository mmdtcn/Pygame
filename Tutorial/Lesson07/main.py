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
r_bullet = 8
# player state define as ready/fire since only one bullet should get fired on the window
pl1_state = 'ready'
pl2_state = 'ready'


# player img
player1_img = pygame.image.load('spaceship.png')

# 90 degree rotation of the first player
player1_img = pygame.transform.rotate(player1_img, 270)

# 180 degree rotation of the second player
player2_img = pygame.transform.rotate(player1_img, 180)

Player1X_Change = 0
Player1Y_Change = 0

Player2X_Change = 0
Player2Y_Change = 0

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

def fire_bullet(X, Y, player):
    pygame.draw.circle(screen, (255, 255, 0), (X, Y), r_bullet, 0)
    if player == 'PL1':
        pl1_state = 'fire'
    elif player == 'PL2':
        pl2_state ='fire'


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
            # First Player Key Events
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
            # Second Player Key Events
            if event.key == pygame.K_KP6:
                Player2X_Change += 1
            if event.key == pygame.K_KP4:
                Player2X_Change -= 1
            if event.key == pygame.K_KP8:
                Player2Y_Change -= 1
            if event.key == pygame.K_KP2:
                Player2Y_Change += 1
            if event.key == pygame.K_KP7 and pl2_state == 'ready':
                pl2_state = 'fire'
        if event.type == pygame.KEYUP:
            # Player 1 Stoppage
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Player1X_Change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                Player1Y_Change = 0
            # Player 2 Stoppage
            if event.key == pygame.K_KP4 or event.key == pygame.K_KP6:
                Player2X_Change = 0
            if event.key == pygame.K_KP2 or event.key == pygame.K_KP8:
                Player2Y_Change = 0

    screen.fill(bg_color)
    screen.blit(bg_img, (0, 0))
    # draw borderline
    pygame.draw.line(screen, Color_line, (x11_border, y11_border), (x12_border, y12_border), 3)
    pygame.draw.line(screen, Color_line, (x21_border, y21_border), (x22_border, y22_border), 3)
    Player1_X += Player1X_Change
    Player1_Y += Player1Y_Change

    Player2_X += Player2X_Change
    Player2_Y += Player2Y_Change

    # First Player
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

    # Second Player
     # Limit the x movements to the borderline
    if Player2_X > screen_width-65:
        Player2_X = screen_width-65
    elif Player2_X < x22_border:
        Player2_X = x22_border

    # Limit the y movements to the borderline
    if Player2_Y < 5:
        Player2_Y = 5
    elif Player2_Y > y22_border - 65:
        Player2_Y = y22_border - 65


    player(Player1_X, Player1_Y, player1_img)
    player(Player2_X, Player2_Y, player2_img)
    # initializing the location of the bullet with player location
    if pl1_state == 'ready':
        bullet1_x = Player1_X+70
        bullet1_y = Player1_Y+32
    
    if pl2_state == 'ready':
        bullet2_x = Player2_X-70
        bullet2_y = Player2_Y+32

    # Player 1: if it is in fire state, bullet should be drawn and its trajectories get updated
    if pl1_state == 'fire':
        fire_bullet(bullet1_x, bullet1_y,'PL1')
        bullet1_x += 2
        # we add 32 pixels as half of the player dimension to compare bullet location with center of the player
        collision_text = collision(Player2_X+32, Player2_Y+32, bullet1_x, bullet1_y)
       
        if bullet1_x > Player2_X:
            pl1_state = 'ready'
            print("Player 1: The fire status is: " + collision_text)
    
     # Player 2: if it is in fire state, bullet should be drawn and its trajectories get updated
    if pl2_state == 'fire':
        fire_bullet(bullet2_x, bullet2_y,'PL2')
        bullet2_x -= 2
        # we add 32 pixels as half of the player dimension to compare bullet location with center of the player
        collision_text = collision(Player1_X+32, Player1_Y+32, bullet2_x, bullet2_y)
    
        if bullet2_x < Player1_X:
            pl2_state = 'ready'
            print("Player 2: The fire status is: " + collision_text)


    pygame.display.update()
