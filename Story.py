#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""

Created on Wed Dec  8 02:26:14 2021

 

@author: ayush

"""

import pygame as pg
import os
import pyttsx3

def story():
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
        "to his home planet Emojiville. All his food supplies in the",
        "spacecraft got scattered on different planets. The aim of",
        "the game is to retrieve the lost food from the different",
        "planets. Be aware of the planet's gravitational pull as",
        "it effects his mobility. The spacecraft damaged one of its",
        "loading docks during the crash so only essential food items",
        "should be collected. Collecting junk foods will make Elif",
        "fatter to the point where Elif explodes. Collecting",
        "essential items will award you points where a certain",
        "amount of points will allow you to complete the level.",
        "                                     GOOD LUCK!!",
        "  ",
        "  ",
        "  ",
        "  ",
        "  ",
        "  ",
        "  "
    )

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
            self.no_visible_lines=1
            self.between_text=50
            self.margin=150
            self.n_line=0
            self.y_position=400
            

        def draw(self):
            line = self.n_line
            y = self.y_position

            for x in range(self.no_visible_lines):
                # build an image of a text line and display it
                text_image = self.font.render(text[line], True, font_colour)
                game_window.blit(text_image, (width//5, y))
                line = (line + 1) % len(text)
                y = y + self.between_text

        def new_frame(self):
            self.y_position -= 0.04 # entire text glides 1 pixel up
            # check if the first line of text came out through the top
            if self.y_position < self.margin:
                self.n_line = (self.n_line + 1) % len(text)
                self.y_position += self.between_text
            # is there room for another row
            next_line_pos = self.y_position + self.between_text * self.no_visible_lines
            if next_line_pos + self.between_text + self.margin < height:
                self.no_visible_lines = self.no_visible_lines + 1

            self.draw()

        def heading(self):
            Text = self.big_font.render("STORY", True, font_colour)
            center_Text=Text.get_rect(center=(width//2,50))
            game_window.blit(Text,center_Text)

        def skip(self):
            Skip=self.small_font.render("Click to Skip",True,font_colour)
            game_window.blit(Skip, [1130, 680])  

    #main code
    pg.init()

    
    game_window = pg.display.set_mode((width,height))
   
    #Caption of window
    pg.display.set_caption("Story")

    screen=Story()
    story_text=Text()
    
    #Updating the PyGame(pg) Window
    pg.display.flip()

    #converting text to mp3 file with 200 words per minute speed (reference:https://hackthedeveloper.com/text-to-speech-pyttsx3-python/)
    engine = pyttsx3.init()
    engine.setProperty("rate", 200)
    engine.save_to_file(text, './/voice.wav')
    engine.runAndWait()

    #loading the mp3 file to speak the text
    pg.mixer.init()
    pg.mixer.music.load('.//voice.wav')
    pg.mixer.music.play()

    while True:
        close_event = pg.event.poll()
        if close_event.type == pg.QUIT or close_event.type == pg.MOUSEBUTTONDOWN:
            pg.mixer.music.stop()
            return
        # Displaying the Game Level
        screen.display()
        #displaying heading
        story_text.heading()
        #displaying skip button
        story_text.skip()
        #display sliding text
        story_text.new_frame()
        # Updating the PyGame(pg) Window
        pg.display.flip()
