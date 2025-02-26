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

  # draw rectangle
  pygame.draw.rect(
    screen, 
    "green", 
    pygame.Rect((300,320), (50, 50))
  )

  '''#draw circle
  pygame.draw.circle(screen, "red", (100,100), 40)

  #draw line
  pygame.draw.line(
    screen, 
    "pink", 
    (100,100), (200,200), 5)

  #draw ellipse
  pygame.draw.ellipse(
    surface=screen, 
    color="purple", 
    rect=pygame.Rect((100,100), (100,500))
  )'''

  #update screen
  pygame.display.flip()
  #fps
  dt = clock.tick(speed)/1000

#quit
pygame.quit