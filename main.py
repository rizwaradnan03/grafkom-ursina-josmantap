import time
from ursina import *
from player import Player
from enemy import Enemy

app = Ursina()

camera.orthographic = True
camera.fov = 10

player = Player(color=color.azure, position_x=0, position_y=0, direction="right")

player_direction = "right"
health_bar = Text(text=f'Health: {player.health}', position=(-0.85, 0.45), scale=2, origin=(0, 0), background=True)

damage_cooldown = 0
spawn_cooldown = 0

existing_projectile = []
existing_enemy = []


def spawn_enemy():
    invoke(spawn_enemy, delay=5)
    enemy = Enemy(id=len(existing_enemy))

    existing_enemy.append(enemy)

spawn_enemy()

def update():
    global player, damage_cooldown, player_direction

    player_position = player.movement()
    shoot_projectile = player.shoot()
    player.check_cooldown()

    if shoot_projectile:
        existing_projectile.append(shoot_projectile)


    if len(existing_enemy) > 0:
        for x in existing_enemy:
            x.movement(player_position_x=player_position['position_x'], player_position_y=player_position['position_y'])


    if len(existing_projectile) > 0:
        for x in existing_projectile:
            x.move()
            
            for p in existing_enemy:
                if x.entity.intersects(p.entity).hit:
                    check_is_dead = p.decrement_health()
                    
                    if check_is_dead['is_dead'] == True:
                        destroy(p.entity)
                        existing_enemy.remove(p)
                        break

    print("Existing Enemy : ", existing_enemy)

    if len(existing_enemy) > 0:
        if damage_cooldown > 0:
            damage_cooldown -= time.dt

        for x in existing_enemy:
            if player.entity.intersects(x.entity).hit and damage_cooldown <= 0:
                player.health -= 10
                damage_cooldown = 1
                health_bar.text = f'Health: {player.health}'


app.run()
