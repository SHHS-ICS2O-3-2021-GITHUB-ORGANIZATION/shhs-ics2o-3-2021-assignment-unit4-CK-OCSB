import pygame
from pygame import Color, draw, display, time

pygame.init()
clock = time.Clock()
gameDisplay = display.set_mode((600, 400))

x = 50
y = 50


while True:
 for i in range(250):
     # Make white background
     gameDisplay.fill(Color('white'))
    # Draw a ball
     draw.circle(gameDisplay, Color('purple'), (x, y), 30)
     # Show graphics on screen
     display.flip()
     # change location of center a little bit!!!
     x = x + 1
     y = y + 1
     # Control the refresh speed in frames per second
     clock.tick(45)
##########################
 for i in range(270):
     # Make white background
     gameDisplay.fill(Color('white'))
     # Draw a ball
     draw.circle(gameDisplay, Color('lightblue'), (x, y), 30)
     # Show graphics on screen
     display.flip()
     # change location of center a little bit!!!
     x = x + 1
     y = y - 1
     # Control the refresh speed in frames per second
     clock.tick(45)
##########################
 for i in range (260):
     # Make white background
     gameDisplay.fill(Color('white'))
     # Draw a ball
     draw.circle(gameDisplay, Color('yellow'), (x, y), 30)
     # Show graphics on screen
     display.flip()
     # change location of center a little bit!!!
     x = x - 1
     y = y + 1
     clock.tick(45)
##########################
 for i in range(260):
     # Make white background
     gameDisplay.fill(Color('white'))
     # Draw a ball
     draw.circle(gameDisplay, Color('red'), (x, y), 30)
     # Show graphics on screen
     display.flip()
     # change location of center a little bit!!!
     x = x - 1
     y = y - 1
     # Control the refresh speed in frames per second
     clock.tick(45)