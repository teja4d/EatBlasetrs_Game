from pygame import mixer
from Lost import lost
# Import random for random numbers
import random
# Import and initialize pygame library
import pygame
from Won import won
#Import for easy access to keys
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

def Game():
    pygame.init()
    
    # Activate Clock
    clock = pygame.time.Clock()
    
    # Define constants for the screen width and height
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    
    # Create the screen 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #Background
    background = background =  pygame.image.load('Background.jpg')
    
    #Font size and colour
    font_type="Xolonium-Bold"
    font_size=30
    font_colour="gold"
    
    # Create a custom event for adding a new enemy
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 35)
    
    #survival mode background music
    pygame.mixer.init()
    pygame.mixer.music.load('survival.mp3')
    pygame.mixer.music.play(loops=-1)
    
    # Variable to keep the main loop running
    running = True
    
    # Define a Player object by extending pygame.sprite.Sprite
    # The surface drawn on the screen is now an attribute of 'player'
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super(Player, self).__init__()
            self.surf = pygame.image.load("smiley.png").convert()
            self.rect = self.surf.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
            self.size = self.surf.get_size()
         
        # Move the sprite based on user keypresses
        def update(self, pressed_keys):
            if pressed_keys[K_UP]:
                self.rect.move_ip(0,-5)
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
             
        def getbig(self):
            self.surf = pygame.transform.scale(pygame.image.load("smiley.png").convert(), (int(self.size[0]+20), int(self.size[1]+20)))  
            self.size = self.surf.get_size()
            self.topleft = self.rect.topleft
            self.rect = self.surf.get_rect(topleft=(self.topleft))
        
        def death(self):
            self.size = self.surf.get_size()
            if self.size > (600,600):
                self.kill()
                return True
            else:
                return False
    # Define the enemy object by extending pygame.sprite.Sprite
    # The surface you draw on the screen is now an attribute of 'enemy'
    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super(Enemy, self).__init__()
            self.surf = pygame.image.load("pizza.png").convert()
            self.rect = self.surf.get_rect(
                center=(
                    random.choice([random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),random.randint(-100,-20)]),
                    random.choice([random.randint(SCREEN_HEIGHT+20, SCREEN_HEIGHT+100),random.randint(-100,-20)])
                )
            )
            self.xspeed = random.randint(-10, 10)
            self.yspeed = random.randint(-10, 10)
    
        # Move the sprite based on speed
        # Remove the sprite when it passes the edges of the screen
        def update(self):
            self.rect.move_ip(self.xspeed,self.yspeed)
            if self.rect.left < -120:
                self.kill()
            if self.rect.right > SCREEN_WIDTH + 120:
                self.kill()
            if self.rect.top < -120:
                self.kill()    
            if self.rect.bottom > SCREEN_HEIGHT + 120:
                self.kill()
            
    
    # Instantiate player. Right now, this is just a rectangle.
    player = Player()
    
    # Create groups to hold enemy sprites and all sprites
    # - enemies is used for collision detection and position updates
    # - all_sprites is used for rendering
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    
    
    counter, text =60, '60'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font=pygame.font.SysFont(font_type,font_size) 
    
    "GAME LOOP"
    while running:
        #generates background
        screen.blit(background , ( 0,0 ) ) 
        # Look at every event in the queue
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    running = False
                    # pygame.mixer.stop()
            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                running = False
                # pygame.mixer.stop()
    
            # Add a new enemy?
            elif event.type == ADDENEMY:
                # Create the new enemy and add it to sprite groups
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            
            #
            if event.type == pygame.USEREVENT: 
                counter -= 1
                if counter>0:
                    text = str(counter).rjust(3)
                else:
                    return won()
            if event.type == pygame.QUIT: 
                break
        
        countdown_text=font.render(text, True, font_colour)
        screen.blit(countdown_text, (25, 25))
        pygame.display.flip()


        
        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()    
        
        # Update enemy position
        enemies.update()
        
        # Update the player sprite based on user keypresses
        player.update(pressed_keys)
                
    
        # Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        
         #Check if any enemies have collided with the player
        if pygame.sprite.spritecollideany(player, enemies):
         #If so, then remove the player and stop the loop
            #player.kill()
            player.getbig()
            collided_enemy = pygame.sprite.spritecollideany(player, enemies)
            if collided_enemy != None:
                collided_enemy .kill()
            #running = False    
        
        #Check if player dies
        if player.death():
            lost()
            running = False
        # Update the display
        pygame.display.flip()
        
        clock.tick(40)
        
    pygame.mixer.music.stop()
    #Outside of game loop so ends game
    return            