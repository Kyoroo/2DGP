import framework
import first_state
import character
import Background
import Food
from pico2d import*
import os

name = "MainState"

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                juel.jump_right = False
                juel.move = False
                if juel.key == True:
                    juel.state = juel.RIGHT_STAND
                    juel.key = False
            elif event.key == SDLK_LEFT:
                juel.jump_left = False
                juel.move = False
                if juel.key == True:
                    juel.state = juel.LEFT_STAND
                    juel.key = False
            elif event.key == SDLK_a:
                lave.jump_left = False
                lave.move = False
                if lave.key == True:
                    lave.state = lave.LEFT_STAND
                    lave.key = False
            elif event.key == SDLK_d:
                lave.jump_right = False
                lave.move = False
                if lave.key == True:
                    lave.state = lave.RIGHT_STAND
                    lave.key = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                framework.change_state(first_state)
            elif event.key == SDLK_RIGHT:
                juel.move = True
                juel.jump_right = True
                if juel.jump == 0:
                    juel.state = juel.RIGHT_RUN
                    juel.key = True
            elif event.key == SDLK_LEFT:
                juel.move = True
                juel.jump_left = True
                if juel.jump == 0:
                    juel.state = juel.LEFT_RUN
                    juel.key = True
            elif event.key == SDLK_UP:
                if juel.jump == 0:
                    if juel.state == juel.LEFT_STAND:
                        juel.state = juel.LEFT_JUMP
                        juel.jump = 1
                        juel.key = False
                    else:
                        juel.state = juel.RIGHT_JUMP
                        juel.jump = 1
                        juel.key = False
            elif event.key == SDLK_a:
                lave.moce = True
                lave.jump_left = True
                if lave.jump == 0:
                    lave.state = lave.LEFT_RUN
                    lave.key = True
            elif event.key == SDLK_d:
                lave.jump_right = True
                lave.move = True
                if lave.jump == 0:
                    lave.state = lave.RIGHT_RUN
                    lave.key = True
            elif event.key == SDLK_w:
                if lave.jump == 0:
                    if lave.state == lave.LEFT_STAND:
                        lave.state = lave.LEFT_JUMP
                        lave.jump = 1
                        lave.key = False
                    else:
                        lave.state = lave.RIGHT_JUMP
                        lave.jump = 1
                        lave.key = False

def enter():
    global juel, lave, background, food_juel, food_lave
    background = Background.Background01()
    food_juel = Food.Food_juel()
    food_lave = Food.Food_lave()
    juel = character.Juel()
    lave = character.Lave()

def exit():
    global juel, lave, background, food_juel, food_lave
    del(food_juel)
    del(food_lave)
    del(juel)
    del(lave)
    del(background)

def update():
    juel.update()
    lave.update()
    if juel.y >= (food_juel.y - 20) and juel.y <= (food_juel.y + 20):
        if juel.x >= (food_juel.x - 10) and juel.x <= (food_juel.x + 10):
            food_juel.update()
    if lave.y >= (food_lave.y - 20) and lave.y <= (food_lave.y + 20):
        if lave.x >= (food_lave.x - 10) and lave.x <= (food_lave.x + 10):
            food_lave.update()


def draw():
    clear_canvas()
    background.draw()
    food_juel.draw()
    food_lave.draw()
    juel.draw()
    lave.draw()
    update_canvas()
    delay(0.08)