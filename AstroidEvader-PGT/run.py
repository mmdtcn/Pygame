
# Dj Rkod - Pulse (George Ellinas Remix) by George_Ellinas (c) copyright 2008 Licensed under a Creative Commons Attribution (3.0) license. https://dig.ccmixter.org/files/George_Ellinas/14073 
# Import the pygame module
import pygame
# Import random for random numbers
import random

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        #self.surf = pygame.Surface((75, 25))  # For development before images added
        self.surf = pygame.image.load("ship.png").convert_alpha()
        #self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(40, SCREEN_HEIGHT/2)
        )

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        global score
        global astroid_image
        self.angle = random.choice(([0]* 10) + [-1,1])
        #self.surf = pygame.Surface((20, 10))
        #self.surf.fill((255, 255, 255))
        #pre_image = pygame.image.load("asteroid.png")  # Use global astroid image
        astroid_size = random.randint(20,50)
        self.surf = pygame.transform.scale(astroid_image, (astroid_size,astroid_size))
        self.surf = pygame.transform.rotate(self.surf, random.randint(0,180))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),  # start off the screen
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 10)
        self.speed += int(score / 10)   # make them faster the longer it goes on

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        global score
        global score_increment
        global ADDENEMY
        global blip
        #self.rect.move_ip(-self.speed, 0)
        self.rect.move_ip(-self.speed, self.angle)
        if self.rect.right < 0:
            blip.play()
            score += score_increment
            if(random.randint(0,100) < 10):  # spawn an extra enemy
                pygame.event.post(pygame.event.Event(ADDENEMY))
            self.kill()
            
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Setup for sounds. Defaults are good.
pygame.mixer.init()



# Initialize pygame
pygame.init()
pygame.font.init()

#Score
score = 0
score_increment = 1

# Setup the clock for a decent framerate
clock = pygame.time.Clock()



# Load and play background music
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/
#pygame.mixer.music.load("Apoxode.mp3")
pygame.mixer.music.load("George_Ellinas_-_Dj_Rkod_-_Pulse_(George_Ellinas_Remix).mp3")
pygame.mixer.music.play(loops=-1)

blip = pygame.mixer.Sound("658266__matrixxx__retro-inspect-sound-ui-or-in-game-notification.wav")


#
# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

astroid_image = pygame.image.load("asteroid-single.png").convert_alpha()

font = pygame.font.Font(None, 36)

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Variable to keep the main loop running
running = True

# Fill the screen with white
screen.fill((255, 255, 255))

# Create a surface and pass in a tuple containing its length and width
surf = pygame.Surface((50, 50))

# Give the surface a color to separate it from the background
surf.fill((0, 0, 0))
rect = surf.get_rect()

screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
pygame.display.flip()

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Update enemy position
    enemies.update()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the player on the screen
    #screen.blit(player.surf, player.rect)

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        player.kill()
        running = False

    # Draw the score to the screen
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

# Game is over - Display score
running = True
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        if event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Draw the score to the screen
    score_text = font.render(f'Final Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (SCREEN_WIDTH/2 - font.size(f'Final Score: {score}')[0]/2, SCREEN_HEIGHT/2))

    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)