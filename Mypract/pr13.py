import pygame

from pygame.colordict import THECOLORS
from pygame.examples.go_over_there import clock, running

pygame.init()
dis = pygame.display.set_mode((720,480))
font = pygame.font.SysFont('courienew', 40)

dis_over=False
while not dis_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           print(event)
           pygame.quit()
    a = (255,255,255)
    b = (0,0,0)
    c = (250,140,0)
    d = (100,600,20)
    f = (135,206,235)

    text_x =50
    text_y =50
    speed = 2

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    dis.fill(f)
    pygame.draw.circle(dis,a, (360,360), 60)
    pygame.draw.circle(dis,a,(360,240), 45)
    pygame.draw.circle(dis,a,(360,180),30)

    pygame.draw.circle(dis,b,(350,175),4)
    pygame.draw.circle(dis,b,(370,175),4)

    pygame.draw.polygon(dis,c, [(360,180),(390,185),(360,190)])

    pygame.draw.line(dis, b, (315,240), (250,200), 5)
    pygame.draw.line(dis, b, (405,240), (470,200), 5)

    text = font.render(("Снеговик"), True, THECOLORS["white"])
    dis.blit(text, (50,50))

    pygame.display.update()
    clock.tick(60)

pygame.quit()





























