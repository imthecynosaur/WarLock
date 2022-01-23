from tkinter import Y
import pygame
import os
import math


class Tank:

    velocity = 8
    image = pygame.image.load(os.path.join('Assets/Images/tank.png'))
    scale = 0.07

    def __init__(self, x, y):
        self.tank = pygame.transform.scale(
            Tank.image, (int(Tank.image.get_width() * Tank.scale), int(Tank.image.get_height() * Tank.scale)))
        self.rect = self.tank.get_rect()
        self.rect.center = (x, y)

    def draw(self, win):
        win.blit(self.tank, self.rect)

    def move(self, destination_x, destination_y):
        teta = math.degrees(math.atan((destination_y - self.rect.centery) /
                                      (destination_x - self.rect.centerx)))

        if (abs((destination_y - self.rect.centery)) < 4 and abs(destination_x - self.rect.centerx) < 4):
            return
        else:
            if((destination_x - self.rect.centerx) > 0 and (destination_y - self.rect.centery) > 0):
                self.rect.centerx += Tank.velocity * \
                    math.cos(math.radians(teta))
                self.rect.centery += Tank.velocity * \
                    math.sin(math.radians(teta))
            elif((destination_x - self.rect.centerx) > 0 and (destination_y - self.rect.centery) < 0):
                self.rect.centerx += Tank.velocity * \
                    math.cos(math.radians(teta))
                self.rect.centery += Tank.velocity * \
                    math.sin(math.radians(teta))
            elif((destination_x - self.rect.centerx) < 0 and (destination_y - self.rect.centery) < 0):
                self.rect.centerx -= Tank.velocity * \
                    math.cos(math.radians(teta))
                self.rect.centery -= Tank.velocity * \
                    math.sin(math.radians(teta))
            elif((destination_x - self.rect.centerx) < 0 and (destination_y - self.rect.centery) > 0):
                self.rect.centerx -= Tank.velocity * \
                    math.cos(math.radians(teta))
                self.rect.centery -= Tank.velocity * \
                    math.sin(math.radians(teta))

        return teta


# tank1 = Tank(200, 300)

# while True:
#     n = int(input())
#     m = int(input())
#     print(tank1.move(n, m))
