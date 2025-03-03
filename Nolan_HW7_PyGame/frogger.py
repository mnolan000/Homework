"""
File: frogger.py
Author: Matthew Nolan
Date: 3/1/25
Description: Program that creates the shapes for the frog, the cars, the roads, and the start and end areas

"""


import pygame
from pygame.constants import KEYDOWN

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

#frog current position
cur_pos = [300,200]
car1_pos = [100,100]
car2_pos = [100,100]
car3_pos = [100,100]
direction = "left"

"""game loop"""
running = True
while running:
  """Handle events"""
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == KEYDOWN:
      #wasd
      if event.key == pygame.K_ESCAPE: #escape key
        running = False
      if event.key == pygame.K_w: #up direction
        cur_pos[1] -= 50  #y coordinate
      if event.key == pygame.K_s: #down direction
        cur_pos[1] += 50  #y coordinate
      if event.key == pygame.K_a: #left direction
        cur_pos[0] -= 50  #x coordinate
      if event.key == pygame.K_d: #right direction
        cur_pos[0] += 50  #x coordinate
      #arrow keys
      if event.key == pygame.K_UP: #up direction
        cur_pos[1] -= 50  #y coordinate
      if event.key == pygame.K_DOWN: #down direction
        cur_pos[1] += 50  #y coordinate
      if event.key == pygame.K_LEFT: #left direction
        cur_pos[0] -= 50  #x coordinate
      if event.key == pygame.K_RIGHT: #right direction
        cur_pos[0] += 50  #x coordinate
  
  """Update our game state"""
  
  if direction == "left":
    car1_pos[0] -= 20
  if direction == "right":
    car1_pos[0] += 20
  

  if cur_pos[0] < 0:  #x direction
    cur_pos[0] = 0
  if cur_pos[0] > width-50:  
    cur_pos[0] = width-50

  if cur_pos[1] < 0:
    cur_pos[1] = 0
  if cur_pos[1] > height - 50:
    cur_pos[1] = height - 50
  """Draw to our screen"""
  #clear screen
  screen.fill("grey")

  #start
  pygame.draw.rect(
    screen, 
    "pink", 
    pygame.Rect((0,300), (600, 100))
  )
  #road
  pygame.draw.rect(
    screen, 
    "black", 
    pygame.Rect((0,50), (600, 200))
  )
  
  #cars
  direction = "right"
  pygame.draw.rect(
    screen, 
    "purple", 
    pygame.Rect((car1_pos[0],70), (50, 50))
  )
  if car1_pos[0] == 600:
    car1_pos[0] = 0


  pygame.draw.rect(
    screen, 
    "blue", 
    pygame.Rect((car2_pos[0],130), (50, 50))
  )
  pygame.draw.rect(
    screen, 
    "magenta", 
    pygame.Rect((car3_pos[0],190), (50, 50))
  )
  #end
  pygame.draw.rect(
    screen, 
    "pink", 
    pygame.Rect((0,0), (600, 60))
  )
  # draw frog
  pygame.draw.rect(
    screen, 
    "green", 
    pygame.Rect(cur_pos[0], cur_pos[1], 50, 50)
  )
  #update screen
  pygame.display.flip()
  #fps
  dt = clock.tick(speed)/1000

#quit
pygame.quit