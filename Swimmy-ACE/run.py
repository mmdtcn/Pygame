
# Dj Rkod - Pulse (George Ellinas Remix) by George_Ellinas (c) copyright 2008 Licensed under a Creative Commons Attribution (3.0) license. https://dig.ccmixter.org/files/George_Ellinas/14073 
# Import the pygame module
import pygame
# Import random for random numbers
import random


# Define a Player object by extending pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        #self.surf = pygame.Surface((75, 25))  # For development before images added
        self.surf = pygame.image.load("ship.png").convert_alpha()
        #self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH / 3, SCREEN_HEIGHT/2)
        )
        self.gravity = 1

    def update(self, pressed_keys):
        if self.rect.bottom < SCREEN_HEIGHT * 7 / 8 and alive:
            self.rect.move_ip(0, self.gravity)
            self.gravity += 0.1
        if pressed_keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.move_ip(0, -10)
            self.gravity = 1
            blip.play()
        

class Block(pygame.sprite.Sprite):
    def __init__(self,x,y, x_offset = 0):
        super(Block, self).__init__()
        self.surf = pygame.Surface( (50, 50))
        self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect(
            bottomleft = (x * 50 + x_offset,SCREEN_HEIGHT * 7 / 8 - y * 50)
        )

    def update(self):
        global alive
        global current_x
        if alive:
            self.rect.move_ip(-5,0)
        if self.rect.right < 0:
            # One one block leaves the screen, spawn more
            for y in range(3):
                b = Block(current_x,random.randint(0,10), SCREEN_WIDTH)
                solids.add(b)
                all_sprites.add(b)
            current_x +=1
            self.kill()

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super(Floor, self).__init__()
        self.surf = pygame.Surface( (SCREEN_WIDTH, 10))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(
            topleft = (0,SCREEN_HEIGHT * 7 /8 )
        )

    def update(self):
        pass
            

# Setup for sounds. Defaults are good.
pygame.mixer.init()



# Initialize pygame
pygame.init()
pygame.font.init()

#Score is time until you die
time = 0
alive = True
current_x = 0  # The x column to spawn the next level

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

def final_score():
    score_font = font.render(f"Final Time: {time}  r to Reset", True, (0,0,0))
    screen.blit(score_font, (200, 400))


# Load and play background music
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/
#pygame.mixer.music.load("Apoxode.mp3")
pygame.mixer.music.load("george.ogg")
pygame.mixer.music.play(loops=-1)

blip = pygame.mixer.Sound("658266__matrixxx__retro-inspect-sound-ui-or-in-game-notification.wav")


#
# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.Font(None, 36)

# Create a custom event for keeping time
TIMER_UPDATE = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_UPDATE, 100)


# Instantiate player. 
player = Player()

# Create groups to hold all sprites for rendering and collisions.
solids = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Generate a first level
level = [(0,0),(5,0), (5,1), (5,4), (5,5), (5,8), (5,9)]
for x in range(5):
    level.append( (x * 2, random.randint(0,10))    )
for x,y in level:
    b = Block(x,y, SCREEN_WIDTH)
    solids.add(b)
    all_sprites.add(b)
    current_x = x

# Variable to keep the main loop running
running = True

# Fill the screen with white
screen.fill((255, 255, 255))


floor = Floor()
all_sprites.add(floor)
solids.add(floor)


# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == pygame.KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == pygame.K_ESCAPE:
                running = False
            # r for reset was typed
            elif event.key == pygame.K_r:  
                score = 0
                time = 0
                alive = True
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == pygame.QUIT:
            running = False
        # Update time
        elif event.type == TIMER_UPDATE and alive:
            time += .250

    # Alternate way to handle key presses, get all presses and send them to players for interpretation
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Move objects
    solids.update()

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Did the player hit any boxes?
    if pygame.sprite.spritecollideany(player, solids):
        final_score()
        alive = False
        print("you die")

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Draw the score to the screen
    score_text = font.render(f'Time: {time:0.2f}', True, (255, 50, 50))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

