import pygame

# init pygame
pygame.init()

# window dimensions
width = 600
height = 400
screen = pygame.display.set_mode((width,height))

#set window title
pygame.display.set_caption("snake")

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
  screen.fill("white")
  #update screen
  pygame.display.flip()
  #fps
  dt = clock.tick(speed)/1000

#quit
pygame.quit