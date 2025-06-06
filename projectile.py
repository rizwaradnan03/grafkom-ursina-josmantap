from ursina import *

class Projectile:
    speed=0.2

    def __init__(self, color, position_x, position_y, direction):
        self.color = color
        self.position_x = position_x
        self.position_y = position_y
        self.direction = direction
        self.entity = Entity(
            model='quad',
            color=color,
            position=(position_x, position_y),
            scale=0.5,
            collider='box'
        )

    def move(self):
        if self.direction == "up":
            self.position_y += 0.2
        elif self.direction == "down":
            self.position_y -= 0.2
        elif self.direction == "right":
            self.position_x += 0.2
        elif self.direction == "left":
            self.position_x -= 0.2
        
        self.entity.x = self.position_x
        self.entity.y = self.position_y
