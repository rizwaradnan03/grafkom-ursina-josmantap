from ursina import *
from projectile import Projectile
import random

class Enemy:
    speed=0.01
    is_shooting = False
    is_moving = False

    def __init__(self, id):
        random_x = random.randint(-10, 10)
        random_y = random.randint(-10, 10)

        self.id = id
        self.color = color.green
        self.position_x = random_x
        self.position_y = random_y
        self.entity = Entity(
            model='quad',
            color=color.green,
            position=(random_x, random_y),
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

        if self.health == 0:
            return {
                'is_dead': True,
                'id': self.id
            }
        
        return {
                'is_dead': False,
                'id': self.id
            }