import sys, pygame, time, random
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
direction = [img_w, 0]

def new_rect(where):
    rect = img.get_rect()
    rect.x = where[0]
    rect.y = where[1]
    return rect

def init_snake():
    head_pos[0] = int(width/2)
    head_pos[1] = int(height/2)
    direction[0] = img_w
    direction[1] = 0
    return [ new_rect( head_pos ), new_rect( [head_pos[0]+img_w, head_pos[1]] ), new_rect( [head_pos[0]+img_w*2, head_pos[1] ] ), new_rect( [head_pos[0]+img_w*3, head_pos[1] ] ) ]

snake = init_snake()
rabbit = new_rect( head_pos )
screen = pygame.display.set_mode(size)

while 1:
    time.sleep(delay)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT:
              direction = [img_w, 0]
          elif event.key == pygame.K_LEFT:
              direction = [-img_w, 0]
          elif event.key == pygame.K_UP:
              direction = [0, -img_h]
          elif event.key == pygame.K_DOWN:
              direction = [0, img_h]
          elif event.key == pygame.K_ESCAPE or event.key == ord('q'):
              pygame.quit()
              sys.exit()
      if event.type == pygame.QUIT: sys.exit()

    head_pos[0] += direction[0];
    head_pos[1] += direction[1];
    snake.insert( 0, new_rect(head_pos) )
    snake.pop()
    print(head_pos);

    # wall hit
    if head_pos[0] < 0 or head_pos[0] > width or head_pos[1] < 0 or head_pos[1] > height:
        snake = init_snake()

    screen.fill(black)
    for r in snake:
        screen.blit(img, r)
    pygame.display.flip()
