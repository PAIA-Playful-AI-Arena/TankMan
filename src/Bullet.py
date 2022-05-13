from .env import *

vec = pygame.math.Vector2


class Bullet(pygame.sprite.Sprite):
    def __init__(self, player_no: int, center: tuple, rot: int):
        pygame.sprite.Sprite.__init__(self)
        self.rect = BULLET_SIZE.copy()
        self.rect.center = center
        self.hit_rect = self.rect
        self.hit_rect.width -= 2
        self.hit_rect.height -= 2
        self.hit_rect.center = self.rect.center
        self.speed = 10
        self._no = player_no
        self.rot = rot
        self.angle = 3.14 / 180 * (self.rot + 90)
        self.move = {"left_up": vec(-self.speed, -self.speed), "right_up": vec(self.speed, -self.speed),
                     "left_down": vec(-self.speed, self.speed), "right_down": vec(self.speed, self.speed),
                     "left": vec(-self.speed, 0), "right": vec(self.speed, 0), "up": vec(0, -self.speed),
                     "down": vec(0, self.speed)}

    def update(self):
        self.hit_rect.center = self.rect.center
        if self.rot == 0:
            self.rect.center += self.move["left"]
        elif self.rot == 315 or self.rot == -45:
            self.rect.center += self.move["left_up"]
        elif self.rot == 270 or self.rot == -90:
            self.rect.center += self.move["up"]
        elif self.rot == 225 or self.rot == -135:
            self.rect.center += self.move["right_up"]
        elif self.rot == 180 or self.rot == -180:
            self.rect.center += self.move["right"]
        elif self.rot == 135 or self.rot == -225:
            self.rect.center += self.move["right_down"]
        elif self.rot == 90 or self.rot == -270:
            self.rect.center += self.move["down"]
        elif self.rot == 45 or self.rot == -315:
            self.rect.center += self.move["left_down"]

        if self.rect.bottom < 0 or self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.kill()

    def get_image_data(self):
        image_data = {"_id": "bullets", "x": self.rect.x, "y": self.rect.y,
                      "width": self.rect.width, "height": self.rect.height, "angle": self.angle}
        return image_data