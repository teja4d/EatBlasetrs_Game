import pygame
from pygame import mixer
 

def instructions():
# Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GOLD = (255, 215, 0)
    
    pygame.init()
     
    #global variables:
    FONT_STYLE = "Xolonium-Bold"
    BIG_FONT_SIZE = 80
    SMALL_FONT_SIZE = 40
    MEDIUM_FONT_SIZE = 50
    SMALLER_FONT_SIZE = 28
    FONT_COLOUR = GOLD
    
    global screen
    
    #mixer.init()
    #mixer.music.load('Star Wars Music.mp3')
    #mixer.music.play()
    
    class instructions:
        global screen
        # Initialising the attributes for game levels
        def __init__(self):
            # Specifying the directory of the Game Levels
            self.instructions_directory = "Background.jpg"
            self.Group_Project_background = pygame.image.load(f"{self.instructions_directory}")
       
        # Displaying the level at specific position based on x and y co-ordinates
        def display(self):
            screen.blit(self.Group_Project_background, (0,0))
     
        # Set the screen background
        #screen.fill(BLACK)
    
    intro = instructions()
    
    # Set the height and width of the screen
    size = [1280, 720]
    screen = pygame.display.set_mode(size)
     
    pygame.display.set_caption("Instruction Screen")
     
    # Loop until the user clicks the close button.
    done = False
     
    # This is a font we use to draw text on the screen (size 36)
    smallfont = pygame.font.SysFont(FONT_STYLE, SMALL_FONT_SIZE)
    bigfont = pygame.font.SysFont(FONT_STYLE, BIG_FONT_SIZE)
    smallerfont = pygame.font.SysFont(FONT_STYLE, SMALLER_FONT_SIZE)
    mediumfont = pygame.font.SysFont(FONT_STYLE, MEDIUM_FONT_SIZE)
    
    display_instructions = True
    instruction_page = 1
    
    
    # -------- Instruction Page Loop -----------
    while not done and display_instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                instruction_page += 1
                if instruction_page == 3:
                    display_instructions = False
    
    
        if instruction_page == 1:
            intro.display()
            text = bigfont.render("INSTRUCTIONS", True, FONT_COLOUR)
            screen.blit(text, [450, 40])
            text = mediumfont.render("Aim Of The Game", True, FONT_COLOUR)
            screen.blit(text, [520, 120])
            height = 190
            Instruction = ["You must move Elif the Emoji to avoid the falling junk food and retrieve the healthy food", "There are 4 levels and all of them must be completed in order to win the game", "Good luck!!"]
            for element in Instruction:
                text = smallfont.render(element, True, FONT_COLOUR)
                screen.blit(text, [40, height])
                height += 40
               
            text = smallerfont.render("Click to Continue", True, FONT_COLOUR)
            screen.blit(text, [1080, 680])
           
            # Draw instructions, page 1
            # This could also load an image created in another program.
            # That could be both easier and more flexible.
    
                 
           
         
        if instruction_page == 2:
            intro.display()
            # Draw instructions, page 2
            text = bigfont.render("INSTRUCTIONS", True, FONT_COLOUR)
            screen.blit(text, [450, 40])
         
            text = mediumfont.render("Movement Keys", True, FONT_COLOUR)
            screen.blit(text, [540, 120])
           
            height = 230
            Instruction = ["Move up = UP KEY", "Move down = DOWN KEY", "Move left = LEFT KEY", "Move right = RIGHT KEY"]
            for element in Instruction:
               text = smallfont.render(element, True, FONT_COLOUR)
               screen.blit(text, [40, height])
               height += 90
            arrow_image = pygame.image.load(".//arrows_Transparent.png")
            arrow_image = pygame.transform.scale(arrow_image, (450, 350))
            screen.blit(arrow_image, (650,200))
           
            text = smallerfont.render("Click to return Home", True, FONT_COLOUR)
            screen.blit(text, [1050, 680])
         
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
         
        # Be IDLE friendly. If you forget this line, the program will 'hang'
        # on exit.
    return
    