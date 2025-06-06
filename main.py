from ursina import *
from projectile import Projectile

app = Ursina()

camera.orthographic = True
camera.fov = 10

player = Entity(model='quad', color=color.azure, scale=(1, 1), position=(0, 0), collider='box')
enemy = Entity(model='quad', color=color.red, scale=0.5, position=(4, 0), collider='box')

player_health = 100
player_direction = "right"
health_bar = Text(text=f'Health: {player_health}', position=(-0.85, 0.45), scale=2, origin=(0, 0), background=True)

damage_cooldown = 0

existing_projectile = []

def update():
    global player_health, damage_cooldown, player_direction

    speed = 5 * time.dt
    if held_keys['a']:
        player.x -= speed
        player_direction = "left"

    elif held_keys['d']:
        player.x += speed
        player_direction = "right"

    elif held_keys['w']:
        player.y += speed
        player_direction = "up"

    elif held_keys['s']:
        player.y -= speed
        player_direction = "down"

    if held_keys['space']:
        projectile = Projectile(color=color.red, position_x=player.x, position_y=player.y, direction=player_direction)
        existing_projectile.append(projectile)

    if len(existing_projectile) > 0:
        for x in existing_projectile:
            x.move()

    if damage_cooldown > 0:
        damage_cooldown -= time.dt

    if player.intersects(enemy).hit and damage_cooldown <= 0:
        player_health -= 10
        damage_cooldown = 1
        health_bar.text = f'Health: {player_health}'
        print("Player hit! Health:", player_health)

app.run()
