from ursina import *
from projectile import Projectile
import random

enemy_type = ['prajurit', 'kesatria', 'pahlawan']

class Enemy:
    speed=0.01
    is_moving = False
    damage_cooldown = False
    
    enemy_color = color.green
    enemy_scale = 0.5
    enemy_health = 45
    
    def __init__(self, id):
        random_x = random.randint(-10, 10)
        random_y = random.randint(-10, 10)

        random_type = random.randint(0,2)
        selected_type = enemy_type[random_type]

        if selected_type == "prajurit":
            enemy_color = color.green
            enemy_health = 45
            enemy_scale = 0.5

        elif selected_type == "kesatria":
            enemy_color = color.cyan
            enemy_health = 79
            enemy_scale = 0.8

        elif selected_type == "pahlawan":
            enemy_color = color.red
            enemy_health = 123
            enemy_scale = 1.7

        self.id = id
        self.color = enemy_color
        self.health = enemy_health
        self.position_x = random_x
        self.position_y = random_y
        self.entity = Entity(
            model='quad',
            color=enemy_color,
            position=(random_x, random_y),
            scale=enemy_scale,
            collider='box'
        )
    
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

    def check_cooldown(self):
        if self.damage_cooldown > 0:
            self.damage_cooldown -= time.dt

    def decrement_health(self):
        if self.damage_cooldown <= 0:
            self.damage_cooldown = 1

            self.health = self.health - 23

            if self.health <= 0:
                return {
                    'is_dead': True,
                    'id': self.id
                }
            
        return {
            'is_dead': False,
            'id': self.id
        }