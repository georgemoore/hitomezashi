# Hitomezashi - a hitomezashi pattern generator, in Python using pygame
# Hitomezashi © 2022 is licensed under Attribution-NonCommercial 4.0 International

import pygame
import os

#Initialise Pattern characteristics
STITCH_LENGTH = 20
STITCH_THICKNESS = 1
STITCH_COLOUR = pygame.Color("darkgoldenrod")
PATCH_CLOTH_COLOUR = pygame.Color("floralwhite")
    
# Game screen setup
os.system('clear')
print("Hitomezashi: Start\n")

#Initialise seeds
seeds_horizontal = []
seeds_vertical = []

#Generate horizontal seed from user input
seed = input("Enter Horizontal Seed: ")
for i in seed:
    seeds_horizontal.extend(ord(j)%2 for j in i)

#Generate vertical seed from user input
seed = input("Enter Horizontal Seed: ")
for i in seed:
    seeds_vertical.extend(ord(j)%2 for j in i)

#Pattern setup
stitch_count_horizontal = len(seeds_horizontal)
stitch_count_vertical = len(seeds_vertical)
pattern_width = stitch_count_horizontal*STITCH_LENGTH
pattern_height = stitch_count_vertical*STITCH_LENGTH

pygame.init()
hitomezashi_pattern = pygame.display.set_mode((pattern_width, pattern_height))
hitomezashi_pattern.fill(PATCH_CLOTH_COLOUR)

#Initialise needle
needle_x = 0
needle_y = 0
        
#Draw horizontal stitches
for v in seeds_vertical:
    if seeds_vertical[v] != 1:
        needle_x += STITCH_LENGTH
    for h in seeds_horizontal:
        pygame.draw.line(hitomezashi_pattern, STITCH_COLOUR, [needle_x,needle_y], [needle_x+STITCH_LENGTH,needle_y], STITCH_THICKNESS)
        needle_x += STITCH_LENGTH*2
    needle_x = 0
    needle_y += STITCH_LENGTH
        
#Draw vertical stitches
for h in seeds_horizontal:
    if seeds_horizontal[h] != 1:
        needle_y += STITCH_LENGTH
    for v in seeds_vertical:
        pygame.draw.line(hitomezashi_pattern, STITCH_COLOUR, [needle_x,needle_y], [needle_x,needle_y+STITCH_LENGTH], STITCH_THICKNESS)
        needle_y += STITCH_LENGTH*2
    needle_y = 0
    needle_x += STITCH_LENGTH 
    
# Display update
def display_update():
    pygame.display.flip()
# One time display update. Move call inside game loop if introducing animation or interactivity
display_update()

print("\nHitomezashi: End (Press Q to Quit)")

# Game loop
while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    if e.type ==  pygame.KEYDOWN:
        if e.key == pygame.K_q:
            break
pygame.quit()
