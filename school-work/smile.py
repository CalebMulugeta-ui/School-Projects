import pygame

white = (255, 255, 255)
black = (0, 0 , 0)
brown = (139, 69, 19)

screen = pygame.display.set_mode((400, 400))
screen.fill(white)

#grid
for l in range(0, 20):
    pygame.draw.line(screen, black, [20*l, 0], [20*l, 400])
    pygame.draw.line(screen, black, [0, 20*l], [400, 20*l])

#circle
pygame.draw.circle(screen, black, [200, 200], 100, 4)
pygame.draw.circle(screen, brown, [160, 160], 10)
pygame.draw.circle(screen, brown, [240, 160], 10)
pygame.draw.arc(screen, black, [(150,220),(100,30)], 3, 0, 3)
pygame.display.update()
pygame.time.delay(5000)