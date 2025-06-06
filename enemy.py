from ursina import *
from projectile import Projectile

class Enemy:
    speed=0.05
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
        print("Posisi Y Player : ", player_position_y)

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

    def shoot(self):
        if held_keys['space']:
            self.is_shooting = True
            if self.is_shooting == True:
                projectile = Projectile(color=color.red, position_x=self.entity.x, position_y=self.entity.y, direction=self.direction)
                self.is_shooting = False

            return projectile