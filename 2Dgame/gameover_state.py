from pico2d import*
import framework
import first_state

name = "GameOverState"
image = None

def enter():
    global image
    image = load_image('game_over.png')

def exit():
    global image
    del(image)

def update(frame_time):
    pass

def draw(frmae_time):
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                framework.change_state(first_state)

def pause():
    pass

def resume():
    pass

