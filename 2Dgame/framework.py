import time

class GameState:
    def __init__(self, state):
        self.enter = state.enter
        self.exit = state.exit
        self.pause = state.pause
        self.resume = state.resume
        self.handle_events = state.handle_events
        self.update = state.update
        self.draw = state.darw


running = None
stack = None

def change_state(state):
    global stack
    pop_state()
    stack.append(state)
    state.enter()

def push_state(state):
    global stack
    if(len(stack) > 0):
        stack[-1].pause()
    stack.append(state)
    state.enter()

def pop_state():
    global stack
    if(len(stack) > 0):
        stack[-1].exit()
        stack.pop()
    if(len(stack) > 0):
        stack[-1].resume()

def quit():
    global running
    running = False

def run(first_state):
    global running, stack
    running = True
    stack = [first_state]
    first_state.enter()
    current_time = time.clock()
    while(running):
        frame_time = time.clock() - current_time
        current_time += frame_time
        stack[-1].handle_events(frame_time)
        stack[-1].update(frame_time)
        stack[-1].draw(frame_time)
    while(len(stack) > 0):
        stack[-1].exit()
        stack.pop()

def reset_time():
    global current_time
    current_time = time.clock()