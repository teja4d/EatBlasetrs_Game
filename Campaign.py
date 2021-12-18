# Importing Required Modules
import pygame
import os
import random
import math
from Lost import lost
from Won import won

def campaign():
    global speed

    # Declaring Global Variables
    global screen_width,screen_height
    global game_window

    global player_points
    global key_stoke,size_stoke
    global element_speed
    global new_x, new_y
    global paths
    global density
    global PlayGame
    global hero_width,hero_height
    global total_points

    global enemy_width,enemy_height

    global score

    global level1_points,level2_points,level3_points,level4_points

    level1_points,level2_points,level3_points,level4_points = 50,100,150,200


    total_points = 0
    paths = 3
    density = 20
    score=5
    player_points = 0
    # Specifying Screen Resolution
    screen_width = 1280
    screen_height = 720

    hero_height = 40
    hero_width = 40

    enemy_height = 30
    enemy_width = 40


    key_stoke=10
    size_stoke=3
    element_speed =5

    new_x = 0
    new_y = 0

    # Adjusting the screen resolution of the game window
    game_window = pygame.display.set_mode((screen_width, screen_height))

    # Loading Image in PyGame and Storing it in an object
    level_0 = pygame.image.load(".//L0.jpg")
    level_1 = pygame.image.load(".//L1.jpg")
    level_2 = pygame.image.load(".//L2.jpg")
    level_3 = pygame.image.load(".//L3.jpg")
    level_4 = pygame.image.load(".//L4.jpg")

    # class GamePhysics:

    class Live:
        
    

        def __init__(self):
            self.directory = './/Assests//Lives//0001.png'
            self.position_x = screen_width - 50
            self.position_y = 10
            self.life = pygame.image.load(f"{self.directory}")
            self.width = 25
            self.height = 30
            self.total_life_count = 3
            
        def display(self):
            # Using the game window declared globally
            global game_window
            # Scaling the Smiley object to small size
            self.life = pygame.transform.smoothscale(
                self.life, (self.width, self.height))
            # Specifying where to place the enemy object in the game window, but it won't be displayed until window is updated
            if self.total_life_count >= 1:
                game_window.blit(self.life, (self.position_x, self.position_y))
            if self.total_life_count >= 2:
                game_window.blit(
                    self.life, (self.position_x - 30, self.position_y))
            if self.total_life_count >= 3:
                game_window.blit(
                    self.life, (self.position_x - 60, self.position_y))

    Hero_Images_Directory = ['.//Assests//Hero//Wondering//', './/Assests//Hero//Tensed//',
                            './/Assests//Hero//Unwell//', './/Assests//Hero//Angry//']

    class Character:
        def __init__(self):
            # Specifying the directory where animations are present
            self.directory = []
            # List to store all the images found from the directory
            self.animation_images = self.fetch_images(self.directory)
            # Storing Animation Index Value
            self.animation_index = 0
            # Creating Hero Character using the Images found
            self.hero_character = pygame.image.load(f"{self.animation_images[0]}")
            # Defining the scale/resolution of the hero
            self.size = hero_height
            # Specifying the position of the Hero in X-Coordinates
            self.position_x = screen_width//2
            # Specifying the position of the Hero in Y-Coordinates
            self.position_y = screen_height//2
            # Eat is set to boolean to know whether hero should eat or not
            self.eat = False
            # After Eating each time, the hero state gets updated
            self.state = 0

        # def __init__(self):
            # Specifying the position of the Hero in X-Coordinates
            self.position = 1

        def displayChar(self, x, y, size_x, size_y, character):
            # Using the game window declared globally

            # Scaling the Smiley object to small size
            self.hero_character = pygame.transform.smoothscale(
                character, (size_x, size_y))
            # Specifying where to place the enemy object in the game window, but it won't be displayed until window is updated
            game_window.blit(self.hero_character, (x, y))

        def fetch_images(self, directory):
            # Empty list to store all the images found
            images_list = []
            # Iterating thorugh all the files in the directory
            for each_image in os.listdir(f"{directory}"):
                # Identifying only '.PNG' files
                if each_image[-4:] == '.png':
                    # Add the PNG Files found to list
                    images_list = images_list + [f"{directory}{each_image}"]
            # Returning the list of PNG images found in the directory
            return images_list
        
        
        def isColliding(smiley,burg):
            meanValue=smiley.size
            x1=x3= smiley.position_x
            y1=y2 = smiley.position_y
            x2=x4 = smiley.position_x + smiley.size
            
            y3=y4 = smiley.position_y + smiley.size
            
            
            
            x_mean = (x1+x2+x3+x4)/4
            y_mean = (y1+y2+y3+y4)/4

            # Fetching co-ordinates of Enemy

            x5 = x7 = burg.position_x
            y5 = y6 = burg.position_y
            x6 = x8 = burg.position_x + burg.width
            y6 = burg.position_y
            y7 = y8 = burg.position_y + burg.height

            bx_mean = (x5+x6+x7+x8)/4
            by_mean = (y5+y6+y7+y8)/4

            # Fetching co-ordinates of Smiley
            distance = math.sqrt(
                (math.pow(x_mean - bx_mean, 2)+(math.pow(y_mean - by_mean, 2))))

            if distance < meanValue//2:
                #print(distance)
                #meanValue =+2.5
                
                return True
            else:
                return False


    class Hero(Character):
        # Initialising the attributes for the hero
        def __init__(self):
            # Specifying the directory where animations are present
            self.directory = ['.//Assests//Hero//Wondering//', './/Assests//Hero//Tensed//',
                            './/Assests//Hero//Unwell//', './/Assests//Hero//Angry//']
            # List to store all the images found from the directory
            self.animation_images = self.fetch_images(self.directory[0])
            # Storing Animation Index Value
            self.animation_index = 0
            # Creating Hero Character using the Images found
            self.hero_character = pygame.image.load(f"{self.animation_images[0]}")
            # Defining the scale/resolution of the hero
            self.size = hero_height
            # Specifying the position of the Hero in X-Coordinates
            self.position_x = screen_width//2
            # Specifying the position of the Hero in Y-Coordinates
            self.position_y = screen_height//2
            # Eat is set to boolean to know whether hero should eat or not
            self.eat = False
            # After Eating each time, the hero state gets updated
            self.state = 0

            # Audio

        # Defining Method to Animate the Character

        def animate(self):
            # Updating the animation index back to normal after Complete animation
            if self.animation_index >= len(self.animation_images):
                self.animation_index = 0
            # Loading the next animation frame of the character
            self.hero_character = pygame.image.load(
                f"{self.animation_images[self.animation_index]}")
            # Updating animation index count
            # self.animation_index += 1
            self.update_animationIndex()
            # Calling display method to show the newly loaded smiley character
            self.display()

        # Defining Method to update Animation Index
        def update_animationIndex(self):
            global PlayGame
            # Checking if eat is enabled or not
            if total_lives.total_life_count <= 0:
                pygame.mixer.music.stop()
                pygame.mixer.Channel(1).stop()
                lost()
                PlayGame = False
                
               
            
            if self.eat:
                # Updating the images only after one complete animation
                if self.animation_index >= len(self.animation_images)-1:
                    # self.state += 1
                    if self.state > 3:
                        self.state = 0
                        self.animation_images = self.fetch_images(
                            self.directory[self.state])
                        total_lives.total_life_count -= 1
                    else:
                        self.animation_images = self.fetch_images(
                            self.directory[self.state])
                    self.eat = False

            self.animation_index += 1

        def Increase_State(self):
            self.state += 1

        # Defining method to increase size
        # Should Animate to increase the Size
        def Increase_Size(self):
            # Increase the size of the character
            self.size += size_stoke

        # Defining Method to show the eat animation
        def eat_animation(self):
            # Loading Eating Animation
            self.animation_images = self.fetch_images(f".//Assests/Hero//Eating//")
            self.eat = True

        def display(self):
            if smiley.position_x > screen_width - smiley.size :
                smiley.position_x = screen_width - smiley.size
                
            if smiley.position_x < 0:
                smiley.position_x = 0
            if smiley.position_y > screen_height - smiley.size:
                smiley.position_y = screen_height - smiley.size
            if smiley.position_y <0:
                smiley.position_y=0
            self.displayChar(self.position_x, self.position_y,
                            self.size, self.size, self.hero_character)


    class Enemy(Character):
    
        
        # Initialising the attributes for the Enemy Character
        def __init__(self,x=random.randint(0,screen_width),y=random.randint(0,screen_height)):#z=random.randint(0,paths)):
            # Specifying the directory where Enemy Images are located
            self.directory = [".//Assests//Enemy//Bad//",
                            ".//Assests//Enemy//Good//"]
            self.Images = []
            self.Images = self.Images + self.fetch_images(self.directory[0])
            self.Images = self.Images + self.fetch_images(self.directory[1])
            # Fetcing all the required Images from the given directory
            # Loading the Enemy Character from the given directory
            self.character_image = self.Images[random.randint(
                0, (len(self.Images)-1))]
            self.enemy_character = pygame.image.load(self.character_image)
            # Specifying the enemy width
            self.width = enemy_width
            # Specifying the enemy height
            self.height = enemy_height
            # Specifying the enemy X Co-ordinate
            self.position_x = x  # random.randint(0,1280)
            # Specifying the enemy Y Co-ordinate
            self.position_y = y  # 720//2
            #
            self.stop_position = False
            self.direction = random.randint(0,paths)
            
            
            
            # Fetching co-ordinates of Enemy

        def display(self):
            # Using the game window declared globally
            self.displayChar(self.position_x, self.position_y,
                            self.width, self.height, self.enemy_character)
            # Updating the poistion of the enemy
            self.update_position(self.stop_position)

        # Method to update position
        def update_position(self, val):

            if not val:

                if self.direction == 0:
                    # print(f'x:{position}')
                    self.position_x -= element_speed

                if self.direction == 1:
                    # print(position)
                    self.position_y += element_speed

                if self.direction == 2:
                    # print(position)
                    self.position_y -= element_speed

                if self.direction == 3:
                    # print(position)
                    self.position_x += element_speed

                if self.direction == 4:
                    # print(f'x:{position}')
                    self.position_x -= element_speed

                    self.position_y += element_speed

                if self.direction == 5:
                    # print(position)
                    self.position_y += element_speed
                    self.position_x -= element_speed

                if self.direction == 6:
                    # print(f'x:{position}')
                    self.position_x -= element_speed
                    self.position_y -= element_speed
                if self.direction == 7:
                    # print(position)
                    self.position_y += element_speed
                    self.position_x += element_speed
                    
        # Updating X Co-ordinate of the enemy
            if self.position_x < 0 or self.position_y > screen_height or self.position_y < 0 or self.position_x > screen_width :
                self.position_x=random.randint(0,screen_width - enemy_width )
                self.position_y=random.randint(0,screen_height -enemy_height)
                self.direction=random.randint(0,paths)
                
        # Method to decrease enemy size
        def decrease_size(self):
            # Decreasing the Width of enemy
            self.width = self.width - 2
            # Decreasing the Height of  enemy
            self.height = self.height - 2
            # Updating width to Zero if the width is less than zero
            if self.width < 0:
                self.width = 0
            # Updating Height to Zero if the height is less than zero
            if self.height < 0:
                self.height = 0
            if self.width == 0 and self.height == 0:
                self.position_x = 0
                self.position_y = 0
            # Updating boolean value to prevent object from moving
            self.stop_position = True

        # Method to update the position of the enemy
        def reset_position(self):
            self.stop_position = False
            self.position_x = random.randint(0, screen_width-self.width)
            self.position_y = random.randint(0, screen_height-self.height)
            self.width = enemy_width
            self.height = enemy_height
            
            self.enemy_character = pygame.image.load(self.Images[random.randint(0, (len(self.Images)-1))])
            self.direction = random.randint(0,paths)


    #created update points function

    def update_points(Image_string):
    
        global player_points
        if 'Good' in Image_string:

            player_points = player_points + score
            return True
        else:
            return False
            

    # Initiating PyGame
    pygame.init()
    pygame.mixer.init()
    # Activate Clock
    clock = pygame.time.Clock()

    # Initiating Hero
    smiley = Hero()

    #generating enemimes
    a=[]
    for i in range(density):
        i = Enemy(random.randint(0,screen_width-enemy_width),random.randint(0,screen_height-enemy_height))
        a.append(i)
        
    
        
    # Initiating Lives
    total_lives = Live()
    pygame.font.init()
    myfont = pygame.font.SysFont('Xolonium-Bold', 30)


    # Specifying boolean value store the play or exit the game
    PlayGame = True
    enable = False

    pygame.mixer.Channel(1).play(pygame.mixer.Sound('.//Assests//Sounds//Level_0.wav'))
    # Iterating the loop if the boolean value is true
    while PlayGame:
        # Fetching the event inside the game window

        event = pygame.event.poll()
        # Checking if the event is related to closing the window or not
        if event.type == pygame.QUIT:
            # If the event is related to closing the window, update PlayGame as false
            PlayGame = False
            #pygame.quit(0)

        # Game Physics
        # Checking and updating the positions based on the key press
        if event.type == pygame.KEYDOWN:
            # Updating the position to left
            if event.key == pygame.K_LEFT:
                new_x = -key_stoke
                pygame.mixer.music.load('.//Assests//Sounds//Move.wav')
                pygame.mixer.music.play(-1)
            # Updating the position to right
            if event.key == pygame.K_RIGHT:
                new_x = key_stoke
                pygame.mixer.music.load('.//Assests//Sounds//Move.wav')
                pygame.mixer.music.play(-1)
            # Updating the position to Up
            if event.key == pygame.K_UP:
                new_y = -key_stoke
                pygame.mixer.music.load('.//Assests//Sounds//Move.wav')
                pygame.mixer.music.play(-1)
            # Updating the position to down
            if event.key == pygame.K_DOWN:
                new_y = key_stoke
                pygame.mixer.music.load('.//Assests//Sounds//Move.wav')
                pygame.mixer.music.play(-1)

        # Checking and Updating the positions based on key release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                new_x = 0
                # pygame.mixer.music.load('.//Assests//Sounds//Move.wav')
                pygame.mixer.music.stop()
            if event.key == pygame.K_RIGHT:
                new_x = 0
                # pygame.mixer.music.load('.//Assests//Sounds//Move.wav')
                pygame.mixer.music.stop()
            if event.key == pygame.K_UP:
                new_y = 0
                # pygame.mixer.music.load('.//Assests//Sounds//Move.wav')
                pygame.mixer.music.stop()
            if event.key == pygame.K_DOWN:
                new_y = 0
                pygame.mixer.music.stop()
            
            
        smiley.position_x += new_x
        smiley.position_y += new_y
        
        
        
        
        # Displaying game window
        if player_points<= level1_points :
        
            paths = 3
            game_window.blit(level_0, (0, 0))
            total_points = 50
            
        if player_points > level1_points :
            x=0.2
            paths = 4
            game_window.blit(level_1, (0, 0))
            element_speed=5+x
            x +=5
            total_points = 100

        if player_points > level2_points :
            x=0.3
            paths = 4 
            element_speed=5+x
            x+=0.5
            smiley.position_y +=3
            game_window.blit(level_2, (0, 0))
            total_points = 150
        if player_points > level3_points :
            x=0.4
            paths = 6
            element_speed=6+x 
            x+=0.5
            smiley.position_y +=5
            total_points = 200
            game_window.blit(level_3, (0, 0))
        if player_points > level4_points :
            x=0.4
            paths = 7
            total_points = 300
            element_speed=8+x
            x+=0.2
            game_window.blit(level_4, (0, 0))
        if player_points >= 300:
            won()
            PlayGame = False
        # Animating Smiley
        smiley.animate()
        
        # Enemy Display
        for i in a:
            i.display()
            if Character.isColliding(smiley,i):
                #burger.decrease_size()
                i.position_x=0
                i.position_y=0
                smiley.eat_animation()
                pygame.mixer.music.load('.//Assests//Sounds//Eat.wav')
                pygame.mixer.music.play()

                gainedPoints = update_points(i.character_image)
                
            
                
                a.append(Enemy(random.randint(0,screen_width-enemy_width),random.randint(0,screen_height-enemy_height)))
                a.pop(random.randint(0,len(a)-1))
                if not gainedPoints:
                    smiley.Increase_Size()
                    smiley.Increase_State()
                # else:
                #     smiley.Increase_Size()
                i.reset_position()
    
            
        # Displaying Life
        total_lives.display()
        
        # font_obj=pygame.font.Font("C:\Windows\Fonts\Arial.ttf",25) 
        text_object = myfont.render(f"Points = {player_points}/{total_points}",True, (127, 127, 127))

        # points = pygame.font.render(str(100), True,'Red')
        game_window.blit(text_object, (10, 10))

        # Refreshing the game window
        pygame.display.flip()

        # Clock Speed
        clock.tick(30)

    # Exiting the PyGame
    #pygame.quit()

    return 
