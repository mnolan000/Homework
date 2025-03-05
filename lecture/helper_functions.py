#function definitions
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