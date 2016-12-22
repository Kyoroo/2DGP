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
    global juel, lave, cheet
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            framework.change_state(first_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_c:
            if cheet == False:
                cheet = True
            elif cheet == True:
                cheet = False
        else:
            juel.handle_events(event)
            lave.handle_events(event)

def enter():
    global juel, lave, background, food_juels, food_laves, monsters, font, obj, fireballs, hp, mp, over, cheet, gameover, pause, clear, clear_draw
    background = Background.Background01()
    monsters = [monster.Monster() for i in range(10)]
    food_juels = [Food.Food_juel() for i in range(2)]
    food_laves = [Food.Food_lave() for i in range(2)]
    fireballs = [monster.Fireball() for i in range(25)]
    gameover = gameover_state.gameover()
    clear_draw = gameover_state.clear()
    hp = Food.HP()
    mp = Food.MP()
    font = load_font('Binggrae.ttf', 40)
    obj = 4
    over = False
    cheet = False
    pause = False
    clear = False

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

    background.set_center_object(juel, lave)
    juel.set_background(background)
    lave.set_background(background)
    for mob in monsters:
        mob.set_background(background)
        mob.set_character(juel, lave)
    for fireball in fireballs:
        fireball.set_background(background)
    for food in food_juels:
        food.set_background(background)
    for food in food_laves:
        food.set_background(background)

    framework.reset_time()

def exit():
    global juel, lave, background, food_juels, food_laves, monsters, fireballs, hp, mp, gameover

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
    global pause
    if pause == False:
        global obj, over, cheet, background, clear

        juel.update(frame_time)
        juel.delay_frame()
        lave.delay_frame()
        lave.update(frame_time)
        background.update(frame_time)

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
                if juel.delay_time == 0 and cheet == False:
                    hp.update()
                    juel.delay_time = 1
                if hp.state >= 3:
                    over = True
            if collide(lave, fireball):
                if lave.delay_time == 0 and cheet == False:
                    mp.update()
                    lave.delay_time = 1
                if mp.state >= 3:
                   over = True

        for monster in monsters:
            if collide(juel, monster):
                if juel.delay_time == 0 and cheet == False:
                    hp.update()
                    juel.delay_time = 1
                if hp.state == 3:
                    over = True
            if collide(lave, monster):
                if lave.delay_time == 0 and cheet == False:
                    mp.update()
                    lave.delay_time = 1
                if mp.state == 3:
                    over = True

        if obj == 0:
            pause = True
            clear = True

    if over == True:
        pause = True

def draw(frame_time):
    global obj

    clear_canvas()
    background.draw()
    hp.draw()
    mp.draw()
    for food in food_juels:
        food.draw()
    for food in food_laves:
        food.draw()
    juel.draw()
    lave.draw()
    for monster in monsters:
        monster.draw()
    for fireball in fireballs:
        fireball.draw()

    font.draw(40,560, 'Food = %d' % obj,(255,255,255))
    if pause == True:
        if over == True:
            gameover.draw()
        elif clear == True:
            clear_draw.draw()


    update_canvas()