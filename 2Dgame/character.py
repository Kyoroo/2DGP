from pico2d import*

class Juel:

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image1 = None

    RIGHT_RUN, LEFT_RUN, LEFT_STAND, RIGHT_STAND, LEFT_JUMP, RIGHT_JUMP = 0, 1, 2, 3, 4, 5

    def handle_events(self, event):
        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                if self.state == self.RIGHT_RUN:
                    pass
                elif self.jump == False:
                    self.state = self.LEFT_STAND
                elif self.move == 1:
                    self.move = 0
            elif event.key == SDLK_RIGHT:
                if self.state == self.LEFT_RUN:
                    pass
                elif self.jump == False:
                    self.state = self.RIGHT_STAND
                    self.move = 2
                elif self.move == 2:
                    self.move = 0
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                if self.jump == False:
                    self.state = self.LEFT_RUN
                    self.move = 1
                else:
                    self.move = 1
            elif event.key == SDLK_RIGHT:
                if self.jump == False:
                    self.state = self.RIGHT_RUN
                else:
                    self.move = 2
            elif event.key == SDLK_UP:
                if self.jump == True:
                    pass
                else:
                    self.jump = True
                    if self.state == self.RIGHT_STAND or self.state == self.RIGHT_RUN:
                        self.state = self.RIGHT_JUMP
                    elif self.state == self.LEFT_STAND or self.state == self.LEFT_RUN:
                        self.state = self.LEFT_JUMP

    def __init__(self):
        self.x, self.y = 20, 80
        self.frame = 0
        self.state = 2
        self.jump = False
        self.jump_state = 0
        self.move = 0
        self.tmp = self.y
        self.total_frames = 0
        self.delay_time = 0
        if Juel.image1 == None:
            self.image = load_image('juel.png')

    def draw(self):
        self.image.clip_draw(self.frame*50, self.state*80, 50, 80, self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 40, self.x + 20, self.y + 35

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        distance = Juel.RUN_SPEED_PPS * frame_time
        self.total_frames += Juel.FRAMES_PER_ACTION * Juel.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8
        if self.state == self.LEFT_RUN:
            self.x -= distance
            self.x = max(self.x, 15)
        elif self.state == self.RIGHT_RUN:
            self.x += distance
            self.x = min(self.x, 785)
        elif self.state == self.RIGHT_JUMP and self.jump == True:
            if self.move == 1:
                self.state = self.LEFT_JUMP
                self.x -= distance
            if self.move == 2:
                self.x += distance
            if self.jump_state == 0:
                self.y += distance
            if self.y > (self.tmp * 2):
                self.jump_state = 1
            if self.jump_state == 1:
                self.y -= distance
                if self.y < self.tmp:
                    self.y = self.tmp
                    self.jump = False
                    self.jump_state = 0
                    if self.move == 2:
                        self.state = self.RIGHT_RUN
                        self.move = 0
                    else:
                        self.state = self.RIGHT_STAND
                        self.move = 0
        elif self.state == self.LEFT_JUMP and self.jump == True:
            if self.move == 1:
                self.x -= distance
                self.x = max(self.x, 15)
            if self.move == 2:
                self.state = self.RIGHT_JUMP
                self.x += distance
                self.x = min(self.x, 785)
            if self.jump_state == 0:
                self.y += distance
            if self.y > (self.tmp * 2):
                self.jump_state = 1
            if self.jump_state == 1:
                self.y -= distance
                if self.y < self.tmp:
                    self.y = self.tmp
                    self.jump = False
                    self.jump_state = 0
                    if self.move == 1:
                        self.state = self.LEFT_RUN
                        self.move = 0
                    else:
                        self.state = self.LEFT_STAND
                        self.move = 0

    def delay_frame(self):
        if self.delay_time > 0:
            self.delay_time +=1
        if self.delay_time > 1000:
            self.delay_time = 0

class Lave:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image2 = None

    RIGHT_RUN, LEFT_RUN, LEFT_STAND, RIGHT_STAND, LEFT_JUMP, RIGHT_JUMP = 0, 1, 2, 3, 4, 5

    def handle_events(self, event):
        if event.type == SDL_KEYUP:
            if event.key == SDLK_a:
                if self.state == self.RIGHT_RUN:
                    pass
                elif self.jump == False:
                    self.state = self.LEFT_STAND
                elif self.move == 1:
                    self.move = 0
            elif event.key == SDLK_d:
                if self.state == self.LEFT_RUN:
                    pass
                elif self.jump == False:
                    self.state = self.RIGHT_STAND
                    self.move = 2
                elif self.move == 2:
                    self.move = 0
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                if self.jump == False:
                    self.state = self.LEFT_RUN
                    self.move = 1
                else:
                    self.move = 1
            elif event.key == SDLK_d:
                if self.jump == False:
                    self.state = self.RIGHT_RUN
                else:
                    self.move = 2
            elif event.key == SDLK_w:
                if self.jump == True:
                    pass
                else:
                    self.jump = True
                    if self.state == self.RIGHT_STAND or self.state == self.RIGHT_RUN:
                        self.state = self.RIGHT_JUMP
                    elif self.state == self.LEFT_STAND or self.state == self.LEFT_RUN:
                        self.state = self.LEFT_JUMP

    def __init__(self):
        self.x, self.y = 780, 80
        self.frame = 0
        self.state = 2
        self.jump = False
        self.jump_state = 0
        self.move = 0
        self.tmp = self.y
        self.total_frames = 0
        self.delay_time = 0
        if Lave.image2 == None:
            self.image = load_image('lave.png')

    def draw(self):
        self.image.clip_draw(self.frame*50, self.state*80, 50, 80, self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 40, self.x + 20, self.y + 35

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        distance = Lave.RUN_SPEED_PPS * frame_time
        self.total_frames += Lave.FRAMES_PER_ACTION * Lave.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8
        if self.state == self.LEFT_RUN:
            self.x -= distance
            self.x = max(self.x, 15)
        elif self.state == self.RIGHT_RUN:
            self.x += distance
            self.x = min(self.x, 785)
        elif self.state == self.RIGHT_JUMP and self.jump == True:
            if self.move == 1:
                self.state = self.LEFT_JUMP
                self.x -= distance
            if self.move == 2:
                self.x += distance
            if self.jump_state == 0:
                self.y += distance
            if self.y > (self.tmp * 2):
                self.jump_state = 1
            if self.jump_state == 1:
                self.y -= distance
                if self.y < self.tmp:
                    self.y = self.tmp
                    self.jump = False
                    self.jump_state = 0
                    if self.move == 2:
                        self.state = self.RIGHT_RUN
                        self.move = 0
                    else:
                        self.state = self.RIGHT_STAND
                        self.move = 0
        elif self.state == self.LEFT_JUMP and self.jump == True:
            if self.move == 1:
                self.x -= distance
                self.x = max(self.x, 15)
            if self.move == 2:
                self.state = self.RIGHT_JUMP
                self.x += distance
                self.x = min(self.x, 785)
            if self.jump_state == 0:
                self.y += distance
            if self.y > (self.tmp * 2):
                self.jump_state = 1
            if self.jump_state == 1:
                self.y -= distance
                if self.y < self.tmp:
                    self.y = self.tmp
                    self.jump = False
                    self.jump_state = 0
                    if self.move == 1:
                        self.state = self.LEFT_RUN
                        self.move = 0
                    else:
                        self.state = self.LEFT_STAND
                        self.move = 0

    def delay_frame(self):
        if self.delay_time > 0:
            self.delay_time +=1
        if self.delay_time > 1000:
            self.delay_time = 0