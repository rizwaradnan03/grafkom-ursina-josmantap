from ursina import *
import random

enemy_type = ['monster1', 'monster2', 'monster3']

class Enemy:
    speed = 0.01
    is_moving = False
    attack_cooldown = 0
    damage_cooldown = 0
    
    enemy_color = color.green
    enemy_scale = 0.5
    enemy_health = 45
    enemy_damage = 8
    
    def __init__(self, id):
        random_x = random.randint(-10, 10)
        random_y = random.randint(-10, 10)

        random_type = random.randint(0, 2)
        selected_type = enemy_type[random_type]

        if selected_type == "monster1":
            self.enemy_color = color.green
            self.enemy_health = 45
            self.enemy_scale = 0.5
            self.enemy_damage = 8
            self.image = 'monster1.png'

        elif selected_type == "monster2":
            self.enemy_color = color.cyan
            self.enemy_health = 79
            self.enemy_scale = 0.8
            self.enemy_damage = 12
            self.image = 'monster2.png'

        elif selected_type == "monster3":
            self.enemy_color = color.red
            self.enemy_health = 123
            self.enemy_scale = 1.7
            self.enemy_damage = 23
            self.image = 'monster3.png'

        self.id = id
        self.color = self.enemy_color
        self.health = self.enemy_health
        self.position_x = random_x
        self.position_y = random_y
        try:
            self.entity = Entity(
                model='quad',
                texture=self.image,
                position=(random_x, random_y),
                scale=self.enemy_scale,
                collider='box',
                double_sided=True
            )
            print(f"Successfully loaded texture {self.image} for enemy {self.id}")
        except Exception as e:
            print(f"Failed to load texture {self.image} for enemy {self.id}: {e}")
            self.entity = Entity(
                model='quad',
                color=self.enemy_color,
                position=(random_x, random_y),
                scale=self.enemy_scale,
                collider='box'
            )
            print(f"Fallback to color {self.enemy_color} for enemy {self.id}")

    
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

    def check_damage_cooldown(self):
        if self.damage_cooldown > 0:
            self.damage_cooldown -= time.dt

    def decrement_health(self, projectile):
        if self.damage_cooldown <= 0:
            self.health = self.health - projectile.damage

            self.damage_cooldown = 1
            
            if self.health <= 0:
                return {
                    'is_dead': True,
                    'id': self.id
                }
            
        return {
            'is_dead': False,
            'id': self.id
        }