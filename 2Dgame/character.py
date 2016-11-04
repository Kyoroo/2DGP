from pico2d import*



class Juel:

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image1 = None

    RIGHT_RUN, LEFT_RUN, LEFT_STAND, RIGHT_STAND, LEFT_JUMP, RIGHT_JUMP = 0, 1, 2, 3, 4, 5

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
        self.dir = 1
        self.temp = self.y
        if Juel.image1 == None:
            self.image = load_image('juel.png')

    def draw(self):
        self.image.clip_draw(self.frame*50, self.state*80, 50, 80, self.x, self.y)

    def update(self, frame_time):
        distance = Juel.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 8
        if self.state == self.LEFT_RUN:
            if self.key == True:
                self.x -= distance
                self.x = max(self.x, 15)
        elif self.state == self.RIGHT_RUN:
            if self.key == True:
                self.x += distance
                self.x = min(self.x, 785)
        elif self.state == self.RIGHT_JUMP:
            if self.jump == 1:
                self.y += distance
                if self.jump_right == True:
                    self.x += distance
                    self.x = min(self.x, 785)
                if self.jump_left == True:
                    self.state = self.LEFT_JUMP
                if (self.temp + (distance * 8)) < self.y:
                    self.jump = 2
            elif self.jump == 2:
                self.y -= distance
                if self.jump_right == True:
                    self.x += distance
                    self.x = min(self.x, 785)
                if self.jump_left == True:
                    self.state = self.LEFT_JUMP
                if self.y <= self.temp:
                    self.y = self.temp
                    if self.move == True:
                        self.state = self.RIGHT_RUN
                        self.key = True
                    else:
                        self.state = self.RIGHT_STAND
                    self.jump = 0
        elif self.state == self.LEFT_JUMP:
            if self.jump == 1:
                self.y += distance
                if self.jump_left == True:
                    self.x -= distance
                    self.x = max(self.x, 15)
                if self.jump_right == True:
                    self.state = self.RIGHT_JUMP
                if (self.temp + (distance * 8)) < self.y:
                    self.jump = 2
            elif self.jump == 2:
                self.y -= distance
                if self.jump_left == True:
                    self.x -= distance
                    self.x = max(self.x, 15)
                if self.jump_right == True:
                    self.state = self.RIGHT_JUMP
                if self.y <= self.temp:
                    self.y = self.temp
                    if self.move == True:
                        self.state = self.LEFT_RUN
                        self.key = True
                    else:
                        self.state = self.LEFT_STAND
                    self.jump = 0



class Lave:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image2 = None

    RIGHT_RUN, LEFT_RUN, LEFT_STAND, RIGHT_STAND, LEFT_JUMP, RIGHT_JUMP = 0, 1, 2, 3, 4, 5

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
        self.temp = self.y
        if Lave.image2 == None:
            self.image = load_image('lave.png')

    def draw(self):
        self.image.clip_draw(self.frame*50, self.state*80, 50, 80, self.x, self.y)

    def update(self, frame_time):
        self.frame = (self.frame + 1) % 8
        distance = Juel.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 8
        if self.state == self.LEFT_RUN:
            if self.key == True:
                self.x -= distance
                self.x = max(self.x, 15)
        elif self.state == self.RIGHT_RUN:
            if self.key == True:
                self.x += distance
                self.x = min(self.x, 785)
        elif self.state == self.RIGHT_JUMP:
            if self.jump == 1:
                self.y += distance
                if self.jump_right == True:
                    self.x += distance
                    self.x = min(self.x, 785)
                if self.jump_left == True:
                    self.state = self.LEFT_JUMP
                if (self.temp + (distance * 8)) < self.y:
                    self.jump = 2
            elif self.jump == 2:
                self.y -= distance
                if self.jump_right == True:
                    self.x += distance
                    self.x = min(self.x, 785)
                if self.jump_left == True:
                    self.state = self.LEFT_JUMP
                if self.y <= self.temp:
                    self.y = self.temp
                    if self.move == True:
                        self.state = self.RIGHT_RUN
                        self.key = True
                    else:
                        self.state = self.RIGHT_STAND
                    self.jump = 0
        elif self.state == self.LEFT_JUMP:
            if self.jump == 1:
                self.y += distance
                if self.jump_left == True:
                    self.x -= distance
                    self.x = max(self.x, 15)
                if self.jump_right == True:
                    self.state = self.RIGHT_JUMP
                if (self.temp + (distance * 8)) < self.y:
                    self.jump = 2
            elif self.jump == 2:
                self.y -= distance
                if self.jump_left == True:
                    self.x -= distance
                    self.x = max(self.x, 15)
                if self.jump_right == True:
                    self.state = self.RIGHT_JUMP
                if self.y <= self.temp:
                    self.y = self.temp
                    if self.move == True:
                        self.state = self.LEFT_RUN
                        self.key = True
                    else:
                        self.state = self.LEFT_STAND
                    self.jump = 0