import random
import pygame 
from pygame import mixer
from Instructions import instructions
from Story2 import story2
from GameFinal import game
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

pygame.init() 
  
res = (1280,720) 
  
screen = pygame.display.set_mode(res) 
  
# Colours

Gold = (255,215,0)  
Gold2 = (255,165,0)
# light shade of the button 
color_light = (72,61,139) 
  
# dark shade of the button 
color_dark = (0,0,225) 
  
# screen width
width = screen.get_width() 
  
# screen height
heightscreen = screen.get_height() 
height = screen.get_height() + 300
  
#fonts 
font = pygame.font.SysFont('Xolonium-Bold',45)
bigfont = pygame.font.SysFont('Xolonium-Bold',180)
ButtonXPosition = width/2-125
ButtonWidth = 270

#Images
background =  pygame.image.load('Background.jpg')
muted = pygame.transform.scale(pygame.image.load('Muted.png'), (30,30))
unmuted = pygame.transform.scale(pygame.image.load('Unmuted.png'), (30,30))
MuteIcon = unmuted


#Music
mixer.init()
mixer.music.load('Star Wars Music.mp3')
mixer.music.play(loops=-1)    
Music = True

#For the Game Loop
Playing = True



"Game Loop"

while Playing == True: 
    
    #generates background
    screen.blit(background , ( 0,0 ) ) 
    #mouse coordinates 
    mouse = pygame.mouse.get_pos() 
    for ev in pygame.event.get(): 
        
        #Red x quit   
        if ev.type == pygame.QUIT: 
            Playing = False 
          
        "Button Clicking"
        if ev.type == pygame.MOUSEBUTTONDOWN: 
             
            #CAMPAIGN MODE
            if ButtonXPosition <= mouse[0] <= ButtonXPosition+ButtonWidth and height/2-300 <= mouse[1] <= height/2-300+40: 
               pass       
            
            
            #QUIT BUTTON click
            if ButtonXPosition <= mouse[0] <= ButtonXPosition+ButtonWidth and height/2+100 <= mouse[1] <= height/2+100+40: 
               Playing = False     
               
            #Insructions button click    
            if ButtonXPosition <= mouse[0] <= ButtonXPosition+ButtonWidth and height/2-100 <= mouse[1] <= height/2-100+40:
                instructions()
            
            #Play button click
            if ButtonXPosition <= mouse[0] <= ButtonXPosition+ButtonWidth and height/2-200 <= mouse[1] <= height/2-200+40:
                game()
            
            #Story button click
            if ButtonXPosition <= mouse[0] <= ButtonXPosition+ButtonWidth and height/2 <= mouse[1] <= height/2+40:
                story2()
            
            #Mute button clicking
            if 10 <= mouse[0] <= 40 and 10 <= mouse[1] <= 40: 
                if Music == True:
                    mixer.music.pause()
                    MuteIcon = muted
                    Music = False
                elif Music == False:
                    mixer.music.unpause()
                    MuteIcon = unmuted
                    Music = True
                    
                    
                
            
    
    
    "QUIT BUTTON"
      
    if ButtonXPosition <= mouse[0] <= ButtonXPosition + ButtonWidth and height/2+100 <= mouse[1] <= height/2+100+40: 
        pygame.draw.rect(screen,color_light,[ButtonXPosition,height/2+100,ButtonWidth,40]) 
        
          
    else: 
        pygame.draw.rect(screen,color_dark,[ButtonXPosition,height/2+100,ButtonWidth,40]) 
      
    # superimposing the text onto our button 
    text = font.render('QUIT' , True , Gold)
    screen.blit(text , (width/2-35,height/2+100+7)) 
    
    "INSTRUCTIONS BUTTON"
    
    if ButtonXPosition <= mouse[0] <= ButtonXPosition+ButtonWidth and height/2-100 <= mouse[1] <= height/2-100+40: 
        pygame.draw.rect(screen,color_light,[ButtonXPosition,height/2-100,ButtonWidth,40]) 
        
          
    else: 
        pygame.draw.rect(screen,color_dark,[ButtonXPosition,height/2-100,ButtonWidth,40]) 
      
    # superimposing the text onto our button 
    text = font.render('INSTRUCTIONS' , True , Gold)
    screen.blit(text , (width/2-105,height/2-93)) 
      
    
    
    "PLAY SURVIVAL BUTTON"
    
    if ButtonXPosition <= mouse[0] <= ButtonXPosition+ButtonWidth and height/2-200 <= mouse[1] <= height/2-200+40: 
        pygame.draw.rect(screen,color_light,[ButtonXPosition,height/2-200,ButtonWidth,40]) 
        
          
    else: 
        pygame.draw.rect(screen,color_dark,[ButtonXPosition,height/2-200,ButtonWidth,40]) 
      
    # superimposing the text onto our button 
    text = font.render('SURVIVAL' , True , Gold)
    screen.blit(text , (width/2-65,height/2-193)) 
    
    
    "CAMPAIGN BUTTRON"
    
    if ButtonXPosition <= mouse[0] <= ButtonXPosition+ButtonWidth and height/2-300 <= mouse[1] <= height/2-300+40: 
        pygame.draw.rect(screen,color_light,[ButtonXPosition,height/2-300,ButtonWidth,40]) 
        
          
    else: 
        pygame.draw.rect(screen,color_dark,[ButtonXPosition,height/2-300,ButtonWidth,40]) 
      
    # superimposing the text onto our button 
    text = font.render('CAMPAIGN' , True , Gold)
    screen.blit(text , (width/2-65,height/2-293)) 
    
    
    
    "STORY BUTTON"
    
    if ButtonXPosition <= mouse[0] <= ButtonXPosition + ButtonWidth and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,color_light,[ButtonXPosition,height/2,ButtonWidth,40]) 
        
          
    else: 
        pygame.draw.rect(screen,color_dark,[ButtonXPosition,height/2,ButtonWidth,40]) 
      
    # superimposing the text onto our button 
    text = font.render('STORY' , True , Gold)
    screen.blit(text , (width/2-40,height/2+7)) 
    
    
    
    
    "MUTE BUTTON"
    
    if 10 <= mouse[0] <= 40 and 10 <= mouse[1] <= 40: 
        pygame.draw.rect(screen,Gold2,[10,10,30,30]) 
        screen.blit(MuteIcon, (10,10))
        
          
    else: 
        pygame.draw.rect(screen,Gold,[10,10,30,30])
        screen.blit(MuteIcon, (10,10))
    
      
    "Add Border"
    for y in [-100,0,100,200,300]:
        pygame.draw.rect(screen,Gold2,[ButtonXPosition,height/2-y,ButtonWidth,40],4)
    
    "Title"
    Title = bigfont.render('HUNGER WARS' , True , Gold)
    screen.blit(Title , (160,50))
    
    
    # updates the frames of the game 
    pygame.display.update() 
    
#Leaves the game
pygame.quit()
    