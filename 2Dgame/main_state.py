import framework
import first_state
import gameover_state
import character
import Background
import Food
import monster
import json
from pico2d import*
import os

name = "MainState"

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def handle_events(frame_time):
    global juel, lave
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            framework.change_state(first_state)
        else:
            juel.handle_events(event)
            lave.handle_events(event)

def enter():
    global juel, lave, background, food_juels, food_laves, monsters, font, obj, fireballs, hp, mp, over
    background = Background.Background01()
    monsters = [monster.Monster() for i in range(2)]
    food_juels = [Food.Food_juel() for i in range(2)]
    food_laves = [Food.Food_lave() for i in range(2)]
    fireballs = [monster.Fireball() for i in range(3)]
    hp = Food.HP()
    mp = Food.MP()
    font = load_font('Binggrae.ttf', 40)
    obj = 4
    over = False

    f = open('data_file.txt', 'r')
    data = json.load(f)
    f.close()

    Juel_state_table = {
        "LEFT_STAND" : character.Juel.LEFT_STAND,
        "RIGHT_STAND" : character.Juel.RIGHT_STAND
    }

    Lave_state_table = {
        "LEFT_STAND" : character.Lave.LEFT_STAND,
        "RIGHT_STAND" : character.Lave.RIGHT_STAND
    }

    juel = character.Juel()
    juel.x = data['Juel']['X']
    juel.y = data['Juel']['Y']
    juel.state = Juel_state_table[data['Juel']['StartState']]

    lave = character.Lave()
    lave.x = data['Lave']['X']
    lave.y = data['Lave']['Y']
    lave.state = Lave_state_table[data['Lave']['StartState']]

    framework.reset_time()

def exit():
    global juel, lave, background, food_juels, food_laves, monsters, fireballs, hp, mp

    del(juel)
    del(lave)
    del(background)
    for food in food_juels:
        del(food)
    for food in food_laves:
        del(food)
    for monster in monsters:
        del(monster)
    for fireball in fireballs:
        del(fireball)
    del(hp)
    del(mp)


def update(frame_time):
    global obj, over

    juel.update(frame_time)
    juel.delay_frame()
    lave.delay_frame()
    lave.update(frame_time)

    for monster in monsters:
        monster.update(frame_time)

    for fireball in fireballs:
        fireball.update(frame_time)

    for food in food_juels:
        if collide(juel, food):
            food_juels.remove(food)
            obj -= 1

    for food in food_laves:
        if collide(lave, food):
            food_laves.remove(food)
            obj -= 1

    for fireball in fireballs:
        if collide(juel, fireball):
            if juel.delay_time == 0:
                hp.update()
                juel.delay_time = 1
            if hp.state >= 3:
                over = True
        if collide(lave, fireball):
            if lave.delay_time == 0:
                mp.update()
                lave.delay_time = 1
            if mp.state >= 3:
                over = True

    for monster in monsters:
        if collide(juel, monster):
            if juel.delay_time == 0:
                hp.update()
                juel.delay_time = 1
            if hp.state == 3:
                over = True
        if collide(lave, monster):
            if lave.delay_time == 0:
                mp.update()
                lave.delay_time = 1
            if mp.state == 3:
                over = True

    if over == True:
        framework.change_state(gameover_state)

def draw(frame_time):
    global obj

    clear_canvas()
    background.draw()
    hp.draw()
    mp.draw()
    for food in food_juels:
        food.draw()
        food.draw_bb()
    for food in food_laves:
        food.draw()
        food.draw_bb()
    juel.draw()
    lave.draw()
    for monster in monsters:
        monster.draw()
        monster.draw_bb()
    for fireball in fireballs:
        fireball.draw()
        fireball.draw_bb()

    juel.draw_bb()
    lave.draw_bb()

    font.draw(40,560, 'Food = %d' % obj,(255,255,255))


    update_canvas()