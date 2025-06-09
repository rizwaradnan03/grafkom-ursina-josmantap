from ursina import *
from projectile import Projectile

class Player:
    speed=0.1
    shooting_cooldown = False
    is_moving = False
    health = 100

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
    
    def movement(self):
        if held_keys['a']:
            self.is_moving = True
            self.position_x -= self.speed
            self.direction = "left"

        elif held_keys['d']:
            self.is_moving = True
            self.position_x += self.speed
            self.direction = "right"

        elif held_keys['w']:
            self.is_moving = True
            self.position_y += self.speed
            self.direction = "up"

        elif held_keys['s']:
            self.is_moving = True
            self.position_y -= self.speed
            self.direction = "down"
        
        if self.is_moving == True:
            self.entity.x = self.position_x
            self.entity.y = self.position_y
            
            self.is_moving = False

        return {
            'position_x': self.position_x,
            'position_y': self.position_y,
            'direction': self.direction
        }

    def check_cooldown(self):
        if self.shooting_cooldown > 0:
            self.shooting_cooldown -= time.dt

    def shoot(self, gun):
        if held_keys['space']:
            if self.shooting_cooldown <= 0:
                self.shooting_cooldown = 1
                gun = gun.fire(player=self)
                
                print("gun value : ", gun)

                return gun