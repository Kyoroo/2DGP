from pico2d import*
import framework
import main_state

name = "FirstState"
image = None

def enter():
    global image
    image = load_image('Title.png')

def exit():
    global image
    del(image)

def update():
    pass

def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                framework.change_state(main_state)

def pause():
    pass

def resume():
    pass

