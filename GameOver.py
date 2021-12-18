import pygame 


def lost():
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
                 
            
                
                #QUIT BUTTON click
                if ButtonXPosition <= mouse[0] <= ButtonXPosition+ButtonWidth and height/2 <= mouse[1] <= height/2+40: 
                   Playing = False     
                  
        
        
        "QUIT BUTTON"
          
        if ButtonXPosition <= mouse[0] <= ButtonXPosition + ButtonWidth and height/2 <= mouse[1] <= height/2+40: 
            pygame.draw.rect(screen,color_light,[ButtonXPosition,height/2,ButtonWidth,40]) 
            
              
        else: 
            pygame.draw.rect(screen,color_dark,[ButtonXPosition,height/2,ButtonWidth,40]) 
          
        # superimposing the text onto our button 
        text = font.render('MENU' , True , Gold)
        screen.blit(text , (width/2-35,height/2+7)) 
        
    
        
        
        
     
          
        "Add Border"
        for y in [0]:
            pygame.draw.rect(screen,Gold2,[ButtonXPosition,height/2-y,ButtonWidth,40],4)
        
        "Title"
        Title = bigfont.render('GAME OVER' , True , Gold)
        screen.blit(Title , (290,150))
        
        
        # updates the frames of the game 
        pygame.display.update() 
        
    #Leaves the game
    return
