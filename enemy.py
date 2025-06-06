from ursina import *
from projectile import Projectile

class Enemy:
    speed=0.01
    is_shooting = False
    is_moving = False

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
        self.health = 100
    
    def movement(self, player_position_x, player_position_y):
        if player_position_x >= self.position_x:
            self.is_moving = True
            self.position_x += self.speed
        elif player_position_x <= self.position_x:
            self.is_moving = True
            self.position_x -= self.speed

        if player_position_y >= self.position_y:
            self.is_moving = True
            self.position_y += self.speed
        elif player_position_y <= self.position_y:
            self.is_moving = True
            self.position_y -= self.speed

        if self.is_moving == True:
            self.entity.y = self.position_y
            self.entity.x = self.position_x

    def decrement_health(self):
        self.health -= 100
        # self.health -= 10

        if self.health == 0:
            return True
    
        return False