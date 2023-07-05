
# Dj Rkod - Pulse (George Ellinas Remix) by George_Ellinas (c) copyright 2008 Licensed under a Creative Commons Attribution (3.0) license. https://dig.ccmixter.org/files/George_Ellinas/14073 
# Import the pygame module
import pygame

            

# Setup for sounds. Defaults are good.
pygame.mixer.init()



# Initialize pygame
pygame.init()





# Load and play background music
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/
#pygame.mixer.music.load("Apoxode.mp3")
pygame.mixer.music.load("Apoxode.mp3")
#pygame.mixer.music.play(loops=-1)

blip = pygame.mixer.Sound("notification.wav")
coin = pygame.mixer.Sound("341695__projectsu012__coins-1.wav")
cash = pygame.mixer.Sound("cash.wav") 
siren = pygame.mixer.Sound("470504__onderwish__emergency-siren.wav") 
pop = pygame.mixer.Sound("pop.wav") 

#
# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Variable to keep the main loop running
running = True

# Fill the screen with white
screen.fill((255, 255, 255))



# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == pygame.KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_1:
                blip.play()
            if event.key == pygame.K_2:
                coin.play()
            if event.key == pygame.K_3:
                cash.play()
            if event.key == pygame.K_4:
                siren.play()
            if event.key == pygame.K_5:
                pop.play()
                
            if event.key == pygame.K_s:
                siren.stop()
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == pygame.QUIT:
            running = False

        

    