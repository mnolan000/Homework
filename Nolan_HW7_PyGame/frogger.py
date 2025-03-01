"""
File: frogger.py
Author: Matthew Nolan
Date: 3/1/25
Description: Program that creates the shapes for the frog, the cars, the roads, and the start and end areas

"""


import pygame

# init pygame
pygame.init()

# window dimensions
width = 600
height = 400
screen = pygame.display.set_mode((width,height))

#set window title
pygame.display.set_caption("frogger")

#fps
clock = pygame.time.Clock()
dt = 0
speed = 10

"""game loop"""
running = True
while running:
  """Handle events"""
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  """Update our game state"""

  """Draw to our screen"""
  #clear screen
  screen.fill("grey")

  #start
  pygame.draw.rect(
    screen, 
    "pink", 
    pygame.Rect((0,300), (600, 100))
  )
  # draw frog
  pygame.draw.rect(
    screen, 
    "green", 
    pygame.Rect((300,320), (50, 50))
  )
  #roads
  pygame.draw.rect(
    screen, 
    "black", 
    pygame.Rect((0,95), (600, 60))
  )
  pygame.draw.rect(
    screen, 
    "black", 
    pygame.Rect((0,160), (600, 60))
  )
  pygame.draw.rect(
    screen, 
    "black", 
    pygame.Rect((0,225), (600, 60))
  )
  #cars
  
  pygame.draw.rect(
    screen, 
    "purple", 
    pygame.Rect((100,100), (50, 50))
  )
  pygame.draw.rect(
    screen, 
    "blue", 
    pygame.Rect((200,165), (50, 50))
  )
  pygame.draw.rect(
    screen, 
    "magenta", 
    pygame.Rect((400,230), (50, 50))
  )
  #end
  pygame.draw.rect(
    screen, 
    "pink", 
    pygame.Rect((0,0), (600, 60))
  )

  #update screen
  pygame.display.flip()
  #fps
  dt = clock.tick(speed)/1000

#quit
pygame.quit