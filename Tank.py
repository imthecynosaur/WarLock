from tkinter import CENTER, Y
import pygame
import os
import math


class Tank:

    velocity = 4
    image = pygame.image.load(os.path.join('Assets/Images/tank.png'))
    scale = 0.07

    def __init__(self, x, y):
        self.image = pygame.transform.scale(
            Tank.image, (int(Tank.image.get_width() * Tank.scale), int(Tank.image.get_height() * Tank.scale)))
        self.center_x = x - self.image.get_width() / 2
        self.center_y = y - self.image.get_height() / 2
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = 0

    def draw(self, win):
        win.blit(self.image, (self.center_x, self.center_y))

    def move(self, destination_x, destination_y):
        teta = math.degrees(math.atan((destination_y - self.rect.centery) /
                                      (destination_x - self.rect.centerx)))

        if (abs(destination_y - self.center_y) < 10 and abs(destination_x - self.center_x) < 10):
            return
        else:
            if((destination_x - self.center_x) > 0):
                self.center_x += Tank.velocity * \
                    math.cos(math.radians(teta))
                self.center_y += Tank.velocity * \
                    math.sin(math.radians(teta))
            elif((destination_x - self.center_x) < 0):
                self.center_x -= Tank.velocity * \
                    math.cos(math.radians(teta))
                self.center_y -= Tank.velocity * \
                    math.sin(math.radians(teta))

    def rotate(self, destination_x, destination_y):
        teta = math.degrees(math.atan((destination_y - self.rect.centery) /
                                      (destination_x - self.rect.centerx)))
