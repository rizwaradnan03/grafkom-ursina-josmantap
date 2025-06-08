from ursina import *
import random

enemy_type = ['prajurit', 'kesatria', 'pahlawan']

class Enemy:
    speed=0.01
    is_moving = False
    damage_cooldown = 0
    attack_cooldown = 0
    
    enemy_color = color.green
    enemy_scale = 0.5
    enemy_health = 45
    enemy_damage = 8
    
    def __init__(self, id):
        random_x = random.randint(-10, 10)
        random_y = random.randint(-10, 10)

        random_type = random.randint(0,2)
        selected_type = enemy_type[random_type]

        if selected_type == "prajurit":
            self.enemy_color = color.green
            self.enemy_health = 45
            self.enemy_scale = 0.5
            self.enemy_damage = 8

        elif selected_type == "kesatria":
            self.enemy_color = color.cyan
            self.enemy_health = 79
            self.enemy_scale = 0.8
            self.enemy_damage = 12

        elif selected_type == "pahlawan":
            self.enemy_color = color.red
            self.enemy_health = 123
            self.enemy_scale = 1.7
            self.enemy_damage = 23

        self.id = id
        self.color = self.enemy_color
        self.health = self.enemy_health
        self.position_x = random_x
        self.position_y = random_y
        self.entity = Entity(
            model='quad',
            color=self.enemy_color,
            position=(random_x, random_y),
            scale=self.enemy_scale,
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

    def check_attack_cooldown(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= time.dt

    def attack(self, player):
        is_dead = False

        if self.attack_cooldown <= 0: 
            player.health -= self.enemy_damage

            if player.health <= 0:
                is_dead = True
            
            self.attack_cooldown = 1

        return {
            'health': player.health,
            'is_dead': is_dead
        }

    def decrement_health(self):
        if self.damage_cooldown <= 0:
            self.damage_cooldown = 1

            self.health = self.health - self.enemy_damage

            if self.health <= 0:
                return {
                    'is_dead': True,
                    'id': self.id
                }
            
        return {
            'is_dead': False,
            'id': self.id
        }