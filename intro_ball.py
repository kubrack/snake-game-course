import sys, pygame, time
pygame.init()

size = width, height = 320, 240
speed = [1, 0]
black = 0, 0, 0
length = 1

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

# TODO:
# - rabbits subset
# - snake growing
# - rabbit eating event
# - tail eating event
# - wall hit event

while 1:
    time.sleep(0.001)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT:
              speed[0] = 1
              speed[1] = 0
          elif event.key == pygame.K_LEFT:
              speed[0] = -1
              speed[1] = 0
          elif event.key == pygame.K_UP:
              speed[1] = -1
              speed[0] = 0
          elif event.key == pygame.K_DOWN:
              speed[1] = 1
              speed[0] = 0
          elif event.key == pygame.K_ESCAPE or event.key == ord('q'):
              pygame.quit()
              sys.exit()
      if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
