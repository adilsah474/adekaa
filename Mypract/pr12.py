#class cat:
    #def __self__(self, name="Багира"):
        #self.name = name


    #def neon(self):
      #return "мяу-мяу"

    #def neon_to_file(self, filename, t1neg=1):
         #with open(cat, "n", filename="




import pygame

pygame.init()
dis=pygame.display.set_mode((500,600))


dis_over=False
while not dis_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           print(event)
           pygame.quit()

    R = pygame.Rect(200,180,200,150)
    A = pygame.Rect(220,200,40,40)
    B = pygame.Rect(270,250,60,80)
    roof_points = [(190, 180), (410, 180), (300, 100)]
    pygame.draw.polygon(dis, (178, 34, 34), roof_points)

    colorR = (142,35,142)
    colorA = (125,42,22)
    colorB = (125,212,100)

    dis.fill((135,206,235))
    pygame.draw.rect(dis, colorR,R,0)
    pygame.draw.rect(dis,  colorA,A, 0)
    pygame.draw.rect(dis, colorB, B, 0)
    pygame.draw.polygon(dis, (178, 34, 34), roof_points)
    pygame.display.update()

quit()



