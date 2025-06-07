from ursina import *
from projectile import Projectile

class Gun:
    color_projectile = color.green
    damage_projectile = 13
    model_projectile = 'cube'
    speed_projectile = 0.2

    def __init__(self, position_x, position_y, direction, type):

        if type == "pistol":
            self.color_gun = color.green
            self.scale = 0.2
            self.color_projectile = color.yellow
            self.damage_projectile = 13
            self.model_projectile = 'cube'
            self.speed_projectile = 0.1

        elif type == "crossbow":
            self.color_gun = color.black
            self.scale = 0.4
            self.color_projectile = color.black
            self.damage_projectile = 43
            self.model_projectile = 'cube'
            self.speed_projectile = 0.2

        elif type == "sniper":
            self.color_gun = color.blue
            self.scale = 0.3
            self.color_projectile = color.red
            self.damage_projectile = 85
            self.model_projectile = 'cube'
            self.speed_projectile = 0.3

        self.type = type
        
        self.projectile = {
            'color': self.color_projectile,
            'position_x': position_x,
            'position_y': position_y,
            'direction': direction,
            'damage': self.damage_projectile,
            'speed': self.speed_projectile,
            'model': self.model_projectile
        }
        
        self.position_x = position_x
        self.position_y = position_y
        self.direction = direction
        self.entity = Entity(
            model='quad',
            color=self.color_gun,
            position=(position_x, position_y),
            scale=self.scale,
            collider='box'
        )
    
    def position(self, position_x, position_y, direction):
        self.entity.x = position_x
        self.entity.y = position_y
        self.direction = direction
    
    def fire(self, player):
        return Projectile(color=self.projectile['color'], damage=self.projectile['damage'], model=self.projectile['model'], position_x=player.position_x, position_y=player.position_y, speed=self.projectile['speed'], direction=player.direction)