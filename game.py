import pygame
import os

pygame.display.set_caption("Warlock")


class Game:
    def __init__(self):
        self.width = 1100
        self.height = 700
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

            self.draw()
            pygame.display.update()

        pygame.quit()

    def draw(self):
        WHITE = (255, 255, 255)
        self.win.fill(WHITE)


game = Game()
game.run()
