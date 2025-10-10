import pygame

pygame.init()
WIDTH, HEIGHT = 720, 480
dis = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Прямоугольники по порядку")

dis_over = False
num_rects = 8
num_rows = 5

margin = 10
rect_width = (WIDTH - (num_rects + 1) * margin) // num_rects
rect_height = (HEIGHT - (num_rows + 1) * margin) // num_rows

colors = [(255, 255, 255), (255, 0, 0), (0, 0, 255)]

font = pygame.font.SysFont("Arial", 24, bold=True)
counter = 1

while not dis_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dis_over = True

        dis.fill((0, 0, 0))
        counter = 1
        for row in range(num_rows):
            for col in range(num_rects):
                x = col * (rect_width + margin) + margin
                y = row * (rect_height + margin) + margin
                color = colors[(col + row) % len(colors)]
                pygame.draw.rect(dis, color, (x, y, rect_width, rect_height))
                text_surface = font.render(str(counter), True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=(x + rect_width // 2, y + rect_height // 2))
                dis.blit(text_surface, text_rect)

                counter += 1
        pygame.display.update()

pygame.quit()

