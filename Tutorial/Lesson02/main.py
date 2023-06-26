import pygame

pygame.init()

width = 800
height = 600
screen_size =(width,height)
background_color = (255, 255, 255)

screen = pygame.display.set_mode(screen_size)
img = pygame.image.load('background.jpg')
bg_img = pygame.transform.scale(img, screen_size)
icon_img = pygame.image.load('icon.png')

img = pygame.image.load('UIndy_logo.png')
UIndy_img_logo = pygame.transform.scale(img, (100, 100))

pygame.display.set_caption('Lesson2: Draw Objects and Movements')
pygame.display.set_icon(icon_img)

x_rect = 2
y_rect = 300
w_rect = 20
h_rect = 20
vel_rect_x = 6

x_circle = 400
y_circle = 580
r_circle = 10

vel_circle_y = 3

'''
#Additional Circle
x1_circle = 40
y1_circle = 40
r1_circle = 50
'''



# font setup for text
fg_color = (0, 255, 0)
bg_color = (0, 0, 128)
UIndy_font = pygame.font.Font('freesansbold.ttf', 32)
UIndy_text = UIndy_font.render('Welcome to Summer Camp', True, fg_color, bg_color)

# text surface object
UIndy_textRect = UIndy_text.get_rect()
# set the center of the rectangular object.
UIndy_textRect.center = (380, 50)


movement_circle = 'DU'
movement_rect = 'LR'
#movement_circle1='LD'


running = True

while running:
    # creates time delay of 10ms
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)
    screen.blit(bg_img, (0, 0))
    screen.blit(UIndy_img_logo, (40, 2))
    screen.blit(UIndy_text, UIndy_textRect)
    pygame.draw.rect(screen, (0, 0, 255), [x_rect, y_rect, w_rect, h_rect], 0)
    pygame.draw.circle(screen, (255, 255, 0), (x_circle, y_circle), 10, 0)
    #pygame.draw.circle(screen, (255, 255, 255), (x1_circle, y1_circle), r1_circle, 0)

    if x_rect < width-1 and movement_rect == 'LR':
        x_rect += vel_rect_x
    else:
        movement_rect = 'RL'

    if x_rect > 1 and movement_rect == 'RL':
        x_rect -= vel_rect_x
    else:
        movement_rect = 'LR'

    if y_circle < height-20 and movement_circle == 'UD':
        y_circle += vel_circle_y
    else:
        movement_circle = 'DU'

    if y_circle > 100 and movement_circle == 'DU':
        y_circle -= vel_circle_y
    else:
        movement_circle = 'UD'
    '''
    if y1_circle < height-20 and movement_circle1 == 'LD':
        x1_circle += vel_circle_y
        y1_circle += vel_circle_y

    else:
        movement_circle1 = 'RU'

    if y1_circle > 100 and movement_circle1 == 'RU':
        x1_circle -= vel_circle_y
        y1_circle -= vel_circle_y
    else:
        movement_circle1 = 'LD'
    '''

    pygame.display.update()

pygame.quit()
