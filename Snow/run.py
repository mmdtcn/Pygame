
# Import the pygame module
import pygame
# Import random for random numbers
import random

# Convert mp3 to ogg - https://stackoverflow.com/questions/62543965/pygame-audio-error-unrecognized-audio-format
# pip install pydub
# AudioSegment.from_mp3("mymp3.mp3").export('myogg.ogg', format='ogg')

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Flake(pygame.sprite.Sprite):
    def __init__(self):
        super(Flake, self).__init__()
        #self.surf = pygame.Surface((75, 25))  # For development before images added
        self.surf = pygame.image.load("flake-small.png").convert_alpha()
        #self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(random.randint(0,SCREEN_WIDTH), random.randint(-SCREEN_HEIGHT/10, 0))
        )
        self.ground = False
        self.speed = random.randint(1,7)

    def update(self):
        if not self.ground:
            self.rect.move_ip(0,self.speed + random.randint(-1,1))
        #self.move = True
        

class Block(pygame.sprite.Sprite):
    def __init__(self,x,y, x_offset = 0):
        super(Block, self).__init__()
        self.surf = pygame.Surface( (20, 20))
        self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect(
            bottomleft = (x * 40 + x_offset,SCREEN_HEIGHT - SCREEN_HEIGHT/10 - y * 40)
        )
    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-1,0)
        if self.rect.right < 0:
            #blip.play()
            self.kill()

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super(Floor, self).__init__()
        self.surf = pygame.Surface( (SCREEN_WIDTH, 10))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(
            topleft = (0,SCREEN_HEIGHT - SCREEN_HEIGHT/10)
        )

    def update(self):
        pass
            
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


# Setup the clock for a decent framerate
clock = pygame.time.Clock()



# Load and play background music
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/
#pygame.mixer.music.load("Apoxode.mp3")
#pygame.mixer.music.load("george.ogg")
#pygame.mixer.music.play(loops=-1)

#blip = pygame.mixer.Sound("658266__matrixxx__retro-inspect-sound-ui-or-in-game-notification.wav")


#
# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

astroid_image = pygame.image.load("asteroid-single.png").convert_alpha()


# Create a custom event for adding a new snowflake
TIMER_UPDATE = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_UPDATE, 100)
time = 0


# Create groups to hold flakes and blocks
# - flakes
# - all_sprites is used for rendering
flakes = pygame.sprite.Group()
player_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


#level = [(0,0),(5,0), (5,1)]
#for x,y in level:
#    b = Block(x,y, SCREEN_WIDTH)
#    solids.add(b)
#    all_sprites.add(b)

# Variable to keep the main loop running
running = True

# Fill the screen with grey
screen.fill((50, 50, 50))


floor = Floor()
all_sprites.add(floor)


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
        # Add a new flake?
        elif event.type == TIMER_UPDATE:
            flake = Flake()
            all_sprites.add(flake)
            flakes.add(flake)


    # See if any flake is touching another
    hits = pygame.sprite.groupcollide(all_sprites, flakes, False, False)
    for a, bs in hits.items():
        if a == floor:
            for b in bs:
                b.ground = True
        #a.move = False
        for b in bs:
            if a != b and a != floor and a.ground and a.rect.bottom - 5 < b.rect.bottom :
                b.ground = True

    # Move objects
    flakes.update()

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    

    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

