import time
from ursina import *
from player import Player
from enemy import Enemy
from gun import Gun
import random

app = Ursina()

camera.orthographic = True
camera.fov = 10

player = Player(color=color.azure, position_x=0, position_y=0, direction="right")
gun = Gun(direction=player.direction, position_x=player.position_x, position_y=player.position_y, type="pistol")
health_bar = Text(text=f'Health: {player.health}', position=(-0.25, 0.45), scale=2, origin=(0, 0), background=True)

spawn_cooldown = 0

existing_projectile = []
existing_enemy = []

dropped_gun = []

def spawn_enemy():
    invoke(spawn_enemy, delay=5)
    enemy = Enemy(id=len(existing_enemy))

    existing_enemy.append(enemy)

spawn_enemy()

def spawn_dropped_gun():
    if len(dropped_gun) <= 3:
        invoke(spawn_dropped_gun, delay=8)
        random_x = random.randint(0, 5)
        random_y = random.randint(0, 5)

        gun_type = ["pistol", "crossbow", "sniper", "m4"]

        # random_gun = random.randint(0, len(gun_type) - 1)
        random_gun = 3

        dropped_gun.append(Gun(position_x=random_x, position_y=random_y, direction=player.direction, type=gun_type[random_gun]))

spawn_dropped_gun()

def update():
    global player, gun

    player_position = player.movement()
    shoot_projectiles = player.shoot(gun=gun)
    player.check_cooldown()
    
    gun.position(position_x=player_position['position_x'], position_y=player_position['position_y'], direction=player_position['direction'])

    if shoot_projectiles:
        for i in shoot_projectiles:
            existing_projectile.append(i)

    if len(existing_enemy) > 0:
        for x in existing_enemy:
            x.movement(player_position_x=player_position['position_x'], player_position_y=player_position['position_y'])
            # x.check_cooldown()
            x.check_attack_cooldown()

    if len(existing_projectile) > 0:
        for x in existing_projectile:
            projectile_move = x.move()
            
            for p in existing_enemy:
                if p.entity.intersects(x.entity).hit:
                    check_is_dead = p.decrement_health(x)
                    
                    if check_is_dead['is_dead'] == True:
                        destroy(p.entity)
                        existing_enemy.remove(p)
                        break
            
            # if projectile_move['is_deleted'] == True:
            #     destroy(x.entity)
            #     existing_projectile.remove(x)

    if len(dropped_gun) > 0:
        for x in dropped_gun:
            if player.entity.intersects(x.entity).hit:
                destroy(gun.entity)
                dropped_gun.remove(x)

                gun = x
                break

    if len(existing_enemy) > 0:
        for x in existing_enemy:
            if player.entity.intersects(x.entity).hit:
                attack = x.attack(player)

                if attack['is_dead'] == True:
                    application.quit()

                health_bar.text = f'Health: {player.health}'


app.run()