from ursina import *
from projectile import Projectile
from player import Player
from enemy import Enemy

app = Ursina()

camera.orthographic = True
camera.fov = 10

player = Player(color=color.azure, position_x=0, position_y=0, direction="right")
enemy = Enemy(color=color.yellow, position_x=2, position_y=1, direction="right")
# enemy = Entity(model='quad', color=color.red, scale=0.5, position=(4, 0), collider='box')

player_direction = "right"
health_bar = Text(text=f'Health: {player.health}', position=(-0.85, 0.45), scale=2, origin=(0, 0), background=True)

damage_cooldown = 0

existing_projectile = []
existing_enemy = []

def update():
    global player, damage_cooldown, player_direction

    player_position = player.movement()
    shoot_projectile = player.shoot()

    if shoot_projectile:
        existing_projectile.append(shoot_projectile)

    enemy.movement(player_position_x=player_position['position_x'], player_position_y=player_position['position_y'])

    if len(existing_projectile) > 0:
        for x in existing_projectile:
            x.move()

    if damage_cooldown > 0:
        damage_cooldown -= time.dt

    if player.entity.intersects(enemy.entity).hit and damage_cooldown <= 0:
        player.health -= 10
        damage_cooldown = 1
        health_bar.text = f'Health: {player.health}'
        print("Player hit! Health:", player.health)


app.run()
