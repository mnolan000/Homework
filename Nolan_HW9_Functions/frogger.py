"""
File: Nolan_HW9_Functions/frogger.py
Author: Matthew Nolan
Date: 3/4/25
Description: 

"""


import pygame
from pygame.constants import KEYDOWN

# init pygame
pygame.init()

#create font
system_fonts = pygame.font.get_fonts()
print(system_fonts)
my_font = pygame.font.SysFont(system_fonts[0], size=48, bold=True, italic=False)

def draw_text(text, coordinate, text_color, my_font, screen):
  """
  This function draws text to the screen
  text: variable that holds text
  coordinate: holds coordinate values
  text_color: holds the color of the text
  """
  text_image = my_font.render(text, True, text_color)
  text_rect = text_image.get_rect()
  text_rect.topleft = coordinate
  screen.blit(text_image, text_rect)



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
cur_pos = [250,310]
car1_pos = [100,100]
car2_pos = [100,100]
car3_pos = [300,100]
car4_pos = [200, 100]
score = 0


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
        cur_pos[1] -= 60  #y coordinate
      if event.key == pygame.K_s: #down direction
        cur_pos[1] += 60  #y coordinate
      if event.key == pygame.K_a: #left direction
        cur_pos[0] -= 60  #x coordinate
      if event.key == pygame.K_d: #right direction
        cur_pos[0] += 60  #x coordinate
      #arrow keys
      if event.key == pygame.K_UP: #up direction
        cur_pos[1] -= 60  #y coordinate
      if event.key == pygame.K_DOWN: #down direction
        cur_pos[1] += 60  #y coordinate
      if event.key == pygame.K_LEFT: #left direction
        cur_pos[0] -= 60  #x coordinate
      if event.key == pygame.K_RIGHT: #right direction
        cur_pos[0] += 60  #x coordinate
  
  """Update our game state"""
  
  
  #set direction of cars
  car_speed = 25
  car1_pos[0] += car_speed
  car2_pos[0] -= car_speed
  car3_pos[0] += car_speed
  car4_pos[0] -= car_speed
  

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
    pygame.Rect((0,200), (600, 300))
  )
  #road
  pygame.draw.rect(
    screen, 
    "black", 
    pygame.Rect((0,50), (600, 255))
  )
  
  #cars
  car1 = pygame.draw.rect(
    screen, 
    "purple", 
    pygame.Rect((car1_pos[0],70), (70, 50))
  )
  if car1_pos[0] == 600:
    car1_pos[0] = 0

 
  car2 = pygame.draw.rect(
    screen, 
    "blue", 
    pygame.Rect((car2_pos[0],130), (70, 50))
  )
  if car2_pos[0] == 0:
    car2_pos[0] = 600

  car3 = pygame.draw.rect(
    screen, 
    "magenta", 
    pygame.Rect((car3_pos[0],190), (70, 50))
  )
  if car3_pos[0] == 600:
    car3_pos[0] = 0

  car4 = pygame.draw.rect(
    screen, 
    "red", 
    pygame.Rect((car4_pos[0],250), (70, 50))
  )
  if car4_pos[0] == 0:
    car4_pos[0] = 600
    
  #end
  end = pygame.draw.rect(
    screen, 
    "pink", 
    pygame.Rect((0,0), (600, 60))
  )
  # draw frog

  frog = pygame.draw.rect(
    screen, 
    "green", 
    pygame.Rect(cur_pos[0], cur_pos[1], 50, 50)
  )

  draw_text(f'score: {score}', (0,0), "black", my_font, screen)

  if pygame.Rect.colliderect(frog, car1) or     pygame.Rect.colliderect(frog, car2) or pygame.Rect.colliderect(frog, car3) or pygame.Rect.colliderect(frog, car4):
    score -=1
    cur_pos = [250,310]
    if score < 0:
      draw_text("You lost!", (250,0), "red", my_font, screen)
      

  if pygame.Rect.colliderect(frog, end):
    score +=1
    cur_pos = [250,310]
    if score >= 5:
      draw_text("You won!", (250,0), "red", my_font, screen)
      
      
  

  #update screen
  pygame.display.flip()
  #fps
  dt = clock.tick(speed)/1000


#quit
pygame.quit