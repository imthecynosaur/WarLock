import os
import pygame


class Player():

    def __init__(self, x, y):
        image = pygame.image.load(os.path.join('Assets/Images/tank.png'))
        scale = 0.07
        self.image = pygame.transform.scale(
            image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.angle = 0


def main():
    player = Player(200, 200)
    while True:

        mx, my = pygame.mouse.get_pos()
        player.angle += 0.03

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

        image_copy = pygame.transform.rotate(player.image, player.angle)
        screen.fill((255, 255, 255))
        screen.blit(image_copy, ((mx - int(player.image.get_width() / 2),
                    my - int(player.image.get_height() / 2))))
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 500))
    main()
