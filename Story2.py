#!/usr/bin/env python3 

# -*- coding: utf-8 -*-

"""

Created on Wed Dec  8 02:26:14 2021

 

@author: ayush

"""

import pygame as pg
import os
import pyttsx3
from pygame import mixer

def story2():
   
    #global variables:
    global game_window
    global font
    global font_color

    
    #display screen global variables
    width=1280
    height=720

    #text global variables
    big_font_size=80   
    font_size=40  
    small_font_size=28  
    font_type="Xolonium-Bold"
    font_colour="gold"
    text = (
        "Elif the emoji crashed his spacecraft while heading back",
        "to his home plant Emojiville. All his food supplies in the",
        "spacecraft got scattered on different planets. The aim of",
        "the game is to retrieve the lost food from the different",
        "planets. The spacecraft damaged one of its loading docks",
        "during the crash so only essential food items should be",
        "collected and not junk foods which include: Burgers,",
        "Pizzas. Only essential items such as Water, Broccolli",
        "Blah and Blah. Collecting essential items will award you",
        "points,where a certain amount of points will allow you to",
        "complete the level. Collecting junk foods will make Elif",
        "fatter to the point where Elif explods.",
        "                                     GOOD LUCK!!",
        "  ",
        "  ",
        "  ",
        "  ",
        "  ",
        "  ",
        "  "
    )
    
    #text sliding global variables 
    y_position=400
    margin = 150 
    txt_margin = 50
    visible_lines=1
    n_line=0
    
    class Story:   
        global game_window
        # Initialising the attributes for game levels
        def __init__(self):
            # Specifying the directory of the Game Levels
            self.story_directory = "Background.jpg"
            self.story_background = pg.image.load(f"{self.story_directory}")

        # Displaying the level at specific position based on x and y co-ordinates 
        def display(self):
            game_window.blit(self.story_background, (0,0))

    class Text:  
        global font,font_color,big_font,small_font

        def __init__(self):
            self.font=pg.font.SysFont(font_type,font_size) 
            self.font_color=pg.Color(font_colour)
            self.big_font=pg.font.SysFont(font_type,big_font_size)
            self.small_font=pg.font.SysFont(font_type,small_font_size)
            self.n_line=n_line
            self.y_position=y_position
            self.visible_lines=visible_lines
            self.txt_margin=txt_margin

        def draw(self):
            line=self.n_line
            y=self.y_position
            for x in range(self.visible_lines):
                # build an image of a text line and display it
                text_image=self.font.render(text[line],True,font_colour)
                game_window.blit(text_image,(width//5, y)) 
                line=(line + 1)%len(text)
                y=y+txt_margin

        def new_frame(self):
            self.y_position -= 0.04 # entire text glides 1 pixel up
            # check if the first line of text came out through the top
            if self.y_position<margin:
                self.n_line=(self.n_line + 1)%len(text)
                self.y_positon=self.y_position+self.txt_margin

            # is there room for another row
            next_line_pos=self.y_position+self.txt_margin*self.visible_lines
            if next_line_pos+self.txt_margin+margin<height:
                self.visible_lines=self.visible_lines+1

            self.draw()
    
        def heading(self): 
            Text=self.big_font.render("STORY",True,font_colour)
            center_Text=Text.get_rect(center=(width//2,50))
            game_window.blit(Text,center_Text)
    
        def skip(self):
            Skip=self.small_font.render("Click to Skip",True,font_colour)
            game_window.blit(Skip, [1130, 680])   

    #main code
    
    pg.init()
    
    TEXT=str(text)

    game_window = pg.display.set_mode((width,height))
 
    pg.display.set_caption("Story")
  
    screen=Story()

    story_text=Text()

    pg.display.flip()

    engine = pyttsx3.init()
    engine.setProperty("rate", 200)
    engine.save_to_file(TEXT, './/voice.wav')
    engine.runAndWait()
    
    pg.mixer.init()
    pg.mixer.music.load('.//voice.wav')
    pg.mixer.music.play()

    while True:
        close_event = pg.event.poll()
        if close_event.type == pg.QUIT:
            break
        if close_event.type == pg.MOUSEBUTTONDOWN:
            mixer.init()
            mixer.music.load('Star Wars Music.mp3')
            mixer.music.play(loops=-1)    
            Music = True
            return Music

        # Displaying the Game Level  
        screen.display()

        #displaying heading
        story_text.heading()
        story_text.draw()
    
        #displaying skip butto
        story_text.skip()

        #displaying gliding text
        story_text.new_frame()

        # Updating the PyGame(pg) Window
        pg.display.flip()

    # quitting/closing the game   
    os._exit(0)

story2()
