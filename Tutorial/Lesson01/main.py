# Create PyGame Screen with background image, icon and exit event
import pygame

running = True

background_color = (255, 255, 255)
pygame.display.set_caption("Lesson 1: Display Window")

# Screen size setup
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)

# Read an image
bg_img = pygame.image.load('background.jpg')

# Resize the image to screen size as background
background_img = pygame.transform.scale(bg_img, screen_size)

# Read an image
icon_img = pygame.image.load('icon.png')

# set the icon
pygame.display.set_icon(icon_img)

# display screen with quit button
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background_color)
    screen.blit(background_img,(0,0))
    pygame.display.update()

pygame.quit()
