"""
File: Nolan_HW9_Functions/frogger.py
Author: Matthew Nolan
Date: 3/4/25
Description: Frogger game where you win if you make it across the highway 5 times, and your score goes down if you hit a car. Has 3 functions and a visible score.

"""


import pygame
from pygame.constants import KEYDOWN

# init pygame
pygame.init()


def create_font(font, size, bold, italic):
  """This function creates the font that will be used.
  font: the font used from 0-2
  size: size of the font
  bold: True or False
  italic: True or False"""
  global my_font
  system_fonts = pygame.font.get_fonts()
  print(system_fonts)
  my_font = pygame.font.SysFont(system_fonts[font], size, bold, italic)

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

def movement_keys(movement_speed):
  """This function creates the movement with arrrow keys and wasd
  movement_speed: the movement speed of the character"""
  if event.type == KEYDOWN:
    #wasd
    if event.key == pygame.K_ESCAPE: #escape key
      running = False
    if event.key == pygame.K_w: #up direction
      cur_pos[1] -= movement_speed  #y coordinate
    if event.key == pygame.K_s: #down direction
      cur_pos[1] += movement_speed  #y coordinate
    if event.key == pygame.K_a: #left direction
      cur_pos[0] -= movement_speed  #x coordinate
    if event.key == pygame.K_d: #right direction
      cur_pos[0] += movement_speed  #x coordinate
    #arrow keys
    if event.key == pygame.K_UP: #up direction
      cur_pos[1] -= movement_speed  #y coordinate
    if event.key == pygame.K_DOWN: #down direction
      cur_pos[1] += movement_speed  #y coordinate
    if event.key == pygame.K_LEFT: #left direction
      cur_pos[0] -= movement_speed  #x coordinate
    if event.key == pygame.K_RIGHT: #right direction
      cur_pos[0] += movement_speed  #x coordinate

#create font
create_font(0,45,True,False)

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

    movement_keys(60) #make it so you can move with arrow keys and wasd
  """Update our game state"""
  
  
  #set direction of cars
  car_speed = 25
  car1_pos[0] += car_speed
  car2_pos[0] -= car_speed
  car3_pos[0] += car_speed
  car4_pos[0] -= car_speed
  
  #make it so the frog cannot go off screen
  if cur_pos[0] < 0: 
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
  


  #draw starting area
  pygame.draw.rect(
    screen, 
    "pink", 
    pygame.Rect((0,200), (600, 300))
  )
  #draw road
  pygame.draw.rect(
    screen, 
    "black", 
    pygame.Rect((0,50), (600, 255))
  )
  
  #draw cars
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
    
  #draw end area
  end = pygame.draw.rect(
    screen, 
    "pink", 
    pygame.Rect((0,0), (600, 60))
  )
  
  #draw frog

  frog = pygame.draw.rect(
    screen, 
    "green", 
    pygame.Rect(cur_pos[0], cur_pos[1], 50, 50)
  )

  #draw score
  draw_text(f'score: {score}', (0,0), "black", my_font, screen)


  #display text if you win
  if score >= 5:
     draw_text("You won!", (230,0), "blue", my_font, screen)
    
  #if you collide with a car, your score goes down by 1 and youre teleported back
  if pygame.Rect.colliderect(frog, car1) or     pygame.Rect.colliderect(frog, car2) or pygame.Rect.colliderect(frog, car3) or pygame.Rect.colliderect(frog, car4):
    score -= 1
    cur_pos = [250,310]
  #draw text that says you lost if your score is under 1
  if score < 0:
    draw_text("You lost!", (230,0), "red", my_font, screen)
      
  #if you reach the end, your score goes up by 1
  if pygame.Rect.colliderect(frog, end):
    score +=1
    cur_pos = [250,310]

      
  

  #update screen
  pygame.display.flip()
  #fps
  dt = clock.tick(speed)/1000


#quit
pygame.quit