import framework
import first_state
import character
import Background
import Food
from pico2d import*
import os

name = "MainState"

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
    global juel, lave, background, food_juel, food_lave
    background = Background.Background01()
    food_juel = Food.Food_juel()
    food_lave = Food.Food_lave()
    juel = character.Juel()
    lave = character.Lave()
    framework.reset_time()

def exit():
    global juel, lave, background, food_juel, food_lave
    del(food_juel)
    del(food_lave)
    del(juel)
    del(lave)
    del(background)

def update(frame_time):
    juel.update(frame_time)
    lave.update(frame_time)
    if juel.y >= (food_juel.y - 20) and juel.y <= (food_juel.y + 20):
        if juel.x >= (food_juel.x - 10) and juel.x <= (food_juel.x + 10):
            food_juel.update()
    if lave.y >= (food_lave.y - 20) and lave.y <= (food_lave.y + 20):
        if lave.x >= (food_lave.x - 10) and lave.x <= (food_lave.x + 10):
            food_lave.update()


def draw(frame_time):
    clear_canvas()
    background.draw()
    food_juel.draw()
    food_lave.draw()
    juel.draw()
    lave.draw()
    update_canvas()
    delay(0.08)