import sys, pygame, time
pygame.init()

size = width, height = 320, 240
head_pos = [ int(width/2), int(height/2) ]
black = 0, 0, 0
length = 1
delay = 0.1

# TODO:
# - rabbits subset
# - snake growing
# - rabbit eating event
# - tail eating event
# - wall hit event

img = pygame.image.load("intro_ball.gif")
img_w = img.get_rect().width
img_h = img.get_rect().height

def new_rect(where):
    rect = img.get_rect()
    rect.x = where[0]
    rect.y = where[1]
    return rect

snake = [ new_rect( head_pos ) ]
screen = pygame.display.set_mode(size)

while 1:
    time.sleep(delay)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT:
              head_pos[0] += img_w
          elif event.key == pygame.K_LEFT:
              head_pos[0] -= img_w
          elif event.key == pygame.K_UP:
              head_pos[1] -= img_h
          elif event.key == pygame.K_DOWN:
              head_pos[1] += img_h
          elif event.key == pygame.K_ESCAPE or event.key == ord('q'):
              pygame.quit()
              sys.exit()
      if event.type == pygame.QUIT: sys.exit()

    snake.append( new_rect( head_pos ) )

    if head_pos[0] < 0 or head_pos[0] > width or head_pos[1] < 0 or head_pos[1] > height:
        head_pos = [ int(width/2), int(height/2) ]
        snake = [ new_rect( head_pos ) ]

    screen.fill(black)
    for r in snake:
        screen.blit(img, r)
    pygame.display.flip()
