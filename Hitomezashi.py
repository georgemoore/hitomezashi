# Hitomezashi - a hitomezashi pattern generator, in Python using pygame
# Hitomezashi © 2022 by George Moore is licensed under Attribution-NonCommercial-ShareAlike 4.0 International
 
# Needs work...

# Challenge accepted.
# v1.01 Minor bugfix and optimisation

import pygame
import random
import math
import os


STITCH_COUNT_HOZIZONTAL = 100
STITCH_COUNT_VERTICAL = 100
STITCH_LENGTH = 10
STITCH_THICKNESS = 1
STITCH_COLOUR = pygame.Color("darkgoldenrod")

PATCH_WIDTH = STITCH_COUNT_HOZIZONTAL*STITCH_LENGTH
PATCH_HEIGHT = STITCH_COUNT_VERTICAL*STITCH_LENGTH
PATCH_CLOTH_COLOUR = pygame.Color("floralwhite")

PATTERN_WIDTH = PATCH_WIDTH
PATTERN_HEIGHT = PATCH_HEIGHT


# Draw Pattern 
class Pattern:
    
    # Construct Pattern
    
    def __init__(self, pattern_width, pattern_height, stitch_thickness, stitch_colour, stitch_length, stitch_count_horizontal, stitch_count_vertical):
        print("Pattern: Construct")
        
        #Initialise pattern
        self.__pattern_width = pattern_width
        self.__pattern_height = pattern_height
        self.__stitch_thickness = stitch_thickness
        self.__stitch_colour = stitch_colour
        self.__stitch_length = stitch_length
        self.__stitch_count_horizontal = stitch_count_horizontal
        self.__stitch_count_vertical = stitch_count_vertical

        seeds_horizontal = []
        seeds_vertical = []


        #Generate seeds for stitching
        self.generateseeds(stitch_count_horizontal, stitch_count_vertical, seeds_horizontal, seeds_vertical)
        
        #Stitch Pattern
        self.stitchpattern(hitomezashi_patch, stitch_thickness, stitch_colour, stitch_length, stitch_count_horizontal, stitch_count_vertical, seeds_horizontal, seeds_vertical)
        
    
    #Generate Seeds
    def generateseeds(self, stitch_count_horizontal, stitch_count_vertical, seeds_horizontal, seeds_vertical):
        
        print("Pattern: Seed generation")
        
        for h in range(0, stitch_count_horizontal):
            seeds_horizontal.append(random.randint(0,1))
        print("\tH Seed: Ready")

        for v in range(0, stitch_count_vertical):
            seeds_vertical.append(random.randint(0,1))
        print("\tV Seed: Ready")

    #Stitch pattern
    def stitchpattern(self, hitomezashi_patch, stitch_thickness, stitch_colour, stitch_length, stitch_count_horizontal, stitch_count_vertical, seeds_horizontal, seeds_vertical):
        
        print("Stitching: Start")   
                  
        #Stitching Logic
        needle_x = 0
        needle_y = 0
        
        #Draw horizontal line
        print("\tStitching: Horizontally")
        for v in range(0, stitch_count_vertical):
            if seeds_vertical[v] != 1:
                needle_x += stitch_length
            for h in range(0, stitch_count_horizontal):
                pygame.draw.line(hitomezashi_patch, stitch_colour, [needle_x,needle_y], [needle_x+stitch_length,needle_y], stitch_thickness)
                needle_x += stitch_length*2
            needle_x = 0
            needle_y += stitch_length
        
        #Draw vertical line
        print("\tStitching: Vertically")
        for h in range(0, stitch_count_horizontal):
            if seeds_horizontal[h] != 1:
                needle_y += stitch_length
            for v in range(0, stitch_count_vertical):
                pygame.draw.line(hitomezashi_patch, stitch_colour, [needle_x,needle_y], [needle_x,needle_y+stitch_length], stitch_thickness)
                needle_y += stitch_length*2
            needle_y = 0
            needle_x += stitch_length 
        
        print("Stitching: End")
    
    
# Game screen setup
os.system('clear')
print("Hitomezashi: Start")

print("Patch: Create")
pygame.init()
hitomezashi_patch = pygame.display.set_mode((PATCH_WIDTH, PATCH_HEIGHT))
hitomezashi_patch.fill(PATCH_CLOTH_COLOUR)

#Pattern setup
print("Pattern: Create")
hitomezashi_pattern = Pattern(PATTERN_WIDTH, PATTERN_HEIGHT, STITCH_THICKNESS, STITCH_COLOUR, STITCH_LENGTH, STITCH_COUNT_HOZIZONTAL, STITCH_COUNT_VERTICAL)

# Display update
print("Display: Update")
def display_update():
    pygame.display.flip()
# One time display update. Move call inside game loop if introducing animation or  interactivity
display_update()

# Game loop
print("Game Loop: Start")
while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    if e.type ==  pygame.KEYDOWN:
        if e.key == pygame.K_q:
            break
pygame.quit()


print("Game Loop: End")

print("Hitomezashi: End")
