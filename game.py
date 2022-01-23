import pygame
import os
from Tank import Tank

pygame.display.set_caption("Warlock")


tank_1 = Tank(200, 200)
tank_2 = Tank(500, 345)
is_moving = False


class Game:
    def __init__(self):
        self.width = 1422
        self.height = 800
        self.win = pygame.display.set_mode((self.width, self.height))
        self.tanks = []
        self.projectiles = []

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        is_moving = True

            self.draw()
            tank_1.draw(self.win)
            try:
                if is_moving:
                    tank_1.move(mouse_x, mouse_y)
                    print(tank_1.rect.centerx, tank_1.rect.centery)
            except:
                pass
            tank_2.draw(self.win)
            pygame.display.update()

        pygame.quit()

    def draw(self):
        WHITE = (255, 255, 255)
        self.win.fill(WHITE)


game = Game()
game.run()
