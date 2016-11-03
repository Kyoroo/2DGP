from pico2d import*

class Juel:

    temp = 0
    image1 = None

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


    RIGHT_RUN, LEFT_RUN, LEFT_STAND, RIGHT_STAND, LEFT_JUMP, RIGHT_JUMP = 0, 1, 2, 3, 4, 5

    def handle_right_stand(self):
        pass

    def handle_left_stand(self):
        pass

    def handle_right_run(self):
        if self.key == True:
            self.x += 5
            self.x = min(self.x, 785)

    def handle_left_run(self):
        if self.key == True:
            self.x -= 5
            self.x = max(self.x, 15)

    def handle_right_jump(self):
        if self.jump == 1:
            self.y += 10
            if self.jump_right == True:
                self.x += 5
                self.x = min(self.x, 785)
            if self.jump_left == True:
                self.state = self.LEFT_JUMP
            if (Juel.temp + 80) == self.y:
                self.jump = 2
        elif self.jump == 2:
            self.y -= 10
            if self.jump_right == True:
                self.x += 5
                self.x = min(self.x, 785)
            if self.jump_left == True:
                self.state = self.LEFT_JUMP
            if self.y == Juel.temp:
                if self.move == True:
                    self.state = self.RIGHT_RUN
                    self.key = True
                else:
                    self.state = self.RIGHT_STAND
                self.jump = 0

    def handle_left_jump(self):
        if self.jump == 1:
            self.y += 10
            if self.jump_left == True:
                self.x -= 5
                self.x = max(self.x, 15)
            if self.jump_right == True:
                self.state = self.RIGHT_JUMP
            if (Juel.temp + 80) == self.y:
                self.jump = 2
        elif self.jump == 2:
            self.y -= 10
            if self.jump_left == True:
                self.x -= 5
                self.x = max(self.x, 15)
            if self.jump_right == True:
                self.state = self.RIGHT_JUMP
            if self.y == Juel.temp:
                if self.move == True:
                    self.state = self.LEFT_RUN
                    self.key = True
                else:
                    self.state = self.LEFT_STAND
                self.jump = 0

    handle_state = {
        RIGHT_RUN: handle_right_run,
        LEFT_RUN: handle_left_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand,
        LEFT_JUMP: handle_left_jump,
        RIGHT_JUMP: handle_right_jump
    }

    def handle_events(self, event):
        if event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                self.jump_right = False
                self.move = False
                if self.key == True:
                    self.state = self.RIGHT_STAND
                    self.key = False
            elif event.key == SDLK_LEFT:
                self.jump_left = False
                self.move = False
                if self.key == True:
                    self.state = self.LEFT_STAND
                    self.key = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                self.move = True
                self.jump_right = True
                if self.jump == 0:
                    self.state = self.RIGHT_RUN
                    self.key = True
            elif event.key == SDLK_LEFT:
                self.move = True
                self.jump_left = True
                if self.jump == 0:
                    self.state = self.LEFT_RUN
                    self.key = True
            elif event.key == SDLK_UP:
                if self.jump == 0:
                    if self.state == self.LEFT_STAND:
                        self.state = self.LEFT_JUMP
                        self.jump = 1
                        self.key = False
                    else:
                        self.state = self.RIGHT_JUMP
                        self.jump = 1
                        self.key = False

    def __init__(self):
        self.x, self.y = 20, 80
        self.frame = 0
        self.state = 3
        self.key = False
        self.jump = 0
        self.jump_left = False
        self.jump_right = False
        self.move = False
        Juel.temp = self.y
        if Juel.image1 == None:
            self.image = load_image('juel.png')

    def draw(self):
        self.image.clip_draw(self.frame*50, self.state*80, 50, 80, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.handle_state[self.state](self)


class Lave:
    temp = 0
    image2 = None

    RIGHT_RUN, LEFT_RUN, LEFT_STAND, RIGHT_STAND, LEFT_JUMP, RIGHT_JUMP = 0, 1, 2, 3, 4, 5

    def handle_right_stand(self):
        pass

    def handle_left_stand(self):
        pass

    def handle_right_run(self):
        if self.key == True:
            self.x += 5
            self.x = min(self.x, 785)

    def handle_left_run(self):
        if self.key == True:
            self.x -= 5
            self.x = max(self.x, 15)

    def handle_right_jump(self):
        if self.jump == 1:
            self.y += 10
            if self.jump_right == True:
                self.x += 5
                self.x = min(self.x, 785)
            if self.jump_left == True:
                self.state = self.LEFT_JUMP
            if (Lave.temp + 80) == self.y:
                self.jump = 2
        elif self.jump == 2:
            self.y -= 10
            if self.jump_right == True:
                self.x += 5
                self.x = min(self.x, 785)
            if self.jump_left == True:
                self.state = self.LEFT_JUMP
            if self.y == Lave.temp:
                if self.move == True:
                    self.state = self.RIGHT_RUN
                    self.key = True
                else:
                    self.state = self.RIGHT_STAND
                self.jump = 0

    def handle_left_jump(self):
        if self.jump == 1:
            self.y += 10
            if self.jump_left == True:
                self.x -= 5
                self.x = max(self.x, 15)
            if self.jump_right == True:
                self.state = self.RIGHT_JUMP
            if (Lave.temp + 80) == self.y:
                self.jump = 2
        elif self.jump == 2:
            self.y -= 10
            if self.jump_left == True:
                self.x -= 5
                self.x = max(self.x, 15)
            if self.jump_right == True:
                self.state = self.RIGHT_JUMP
            if self.y == Lave.temp:
                if self.move == True:
                    self.state = self.LEFT_RUN
                    self.key = True
                else:
                    self.state = self.LEFT_STAND
                self.jump = 0

    handle_state = {
        RIGHT_RUN: handle_right_run,
        LEFT_RUN: handle_left_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand,
        LEFT_JUMP: handle_left_jump,
        RIGHT_JUMP: handle_right_jump
    }

    def handle_events(self, event):
        if event.type == SDL_KEYUP:
            if event.key == SDLK_a:
                self.jump_left = False
                self.move = False
                if self.key == True:
                    self.state = self.LEFT_STAND
                    self.key = False
            elif event.key == SDLK_d:
                self.jump_right = False
                self.move = False
                if self.key == True:
                    self.state = self.RIGHT_STAND
                    self.key = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                self.move = True
                self.jump_left = True
                if self.jump == 0:
                    self.state = self.LEFT_RUN
                    self.key = True
            elif event.key == SDLK_d:
                self.jump_right = True
                self.move = True
                if self.jump == 0:
                    self.state = self.RIGHT_RUN
                    self.key = True
            elif event.key == SDLK_w:
                if self.jump == 0:
                    if self.state == self.LEFT_STAND:
                        self.state = self.LEFT_JUMP
                        self.jump = 1
                        self.key = False
                    else:
                        self.state = self.RIGHT_JUMP
                        self.jump = 1
                        self.key = False

    def __init__(self):
        self.x, self.y = 780, 80
        self.frame = 0
        self.state = 2
        self.key = False
        self.jump = 0
        self.jump_left = False
        self.jump_right = False
        self.move = False
        Lave.temp = self.y
        if Lave.image2 == None:
            self.image = load_image('lave.png')

    def draw(self):
        self.image.clip_draw(self.frame*50, self.state*80, 50, 80, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.handle_state[self.state](self)