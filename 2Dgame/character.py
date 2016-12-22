from pico2d import*

class Juel:

    PIXEL_PER_METER = (10.0 / 0.2)
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image1 = None

    RIGHT_RUN, LEFT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def handle_events(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT: self.xdir += -1
            elif event.key == SDLK_RIGHT: self.xdir += 1
            elif event.key == SDLK_UP: self.ydir += 1
            elif event.key == SDLK_DOWN: self.ydir -= 1

        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT: self.xdir += 1
            elif event.key == SDLK_RIGHT: self.xdir += -1
            elif event.key == SDLK_UP: self.ydir -= 1
            elif event.key == SDLK_DOWN: self.ydir += 1

    def __init__(self):
        self.x, self.y = 20, 80
        self.frame = 0
        self.state = 2
        self.jump = False
        self.jump_state = 0
        self.move = 0
        self.xdir = 0
        self.ydir = 0
        self.total_frames = 0
        self.delay_time = 0
        if Juel.image1 == None:
            self.image = load_image('juel.png')

    def set_background(self, bg):
        self.bg = bg

    def draw(self):
        sx = self.x - self.bg.window_left
        sy = self.y - self.bg.window_bottom
        self.image.clip_draw(self.frame*50, self.state*80, 50, 80, sx, sy)

    def get_bb(self):
        sx = self.x - self.bg.window_left
        sy = self.y - self.bg.window_bottom
        return sx - 20, sy - 40, sx + 20, sy + 35

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        distance = Juel.RUN_SPEED_PPS * frame_time
        if (self.xdir == -1 and self.ydir == -1) or (self.xdir == 1 and self.ydir == 1) or (
                self.xdir == -1 and self.ydir == 1) or (self.xdir == 1 and self.ydir == -1):
            distance /= math.sqrt(2)
        self.total_frames += Juel.FRAMES_PER_ACTION * Juel.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8
        self.x += (self.xdir * distance)
        self.y += (self.ydir * distance)

        self.x = clamp(25, self.x, self.bg.w - 25)
        self.y = clamp(40, self.y, self.bg.h - 760)

        if self.xdir == -1:
            self.state = self.LEFT_RUN
        elif self.xdir == 1:
            self.state = self.RIGHT_RUN
        elif self.xdir == 0:
            if self.state == self.RIGHT_RUN:
                self.state = self.RIGHT_STAND
            elif self.state == self.LEFT_RUN:
                self.state = self.LEFT_STAND

    def delay_frame(self):
        if self.delay_time > 0:
            self.delay_time +=1
        if self.delay_time > 1000:
            self.delay_time = 0

class Lave:

    image2 = None

    RIGHT_RUN, LEFT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def handle_events(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_a: self.xdir += -1
            elif event.key == SDLK_d: self.xdir += 1
            elif event.key == SDLK_w: self.ydir += 1
            elif event.key == SDLK_s: self.ydir -= 1

        if event.type == SDL_KEYUP:
            if event.key == SDLK_a: self.xdir += 1
            elif event.key == SDLK_d: self.xdir += -1
            elif event.key == SDLK_w: self.ydir -= 1
            elif event.key == SDLK_s: self.ydir += 1

    def __init__(self):
        self.x, self.y = 780, 80
        self.frame = 0
        self.state = 2
        self.jump = False
        self.jump_state = 0
        self.move = 0
        self.xdir = 0
        self.ydir = 0
        self.total_frames = 0
        self.delay_time = 0
        if Lave.image2 == None:
            self.image = load_image('lave.png')

    def set_background(self, bg):
        self.bg = bg

    def draw(self):
        sx = self.x - self.bg.window_left
        sy = self.y - self.bg.window_bottom
        self.image.clip_draw(self.frame*50, self.state*80, 50, 80, sx, sy)

    def get_bb(self):
        sx = self.x - self.bg.window_left
        sy = self.y - self.bg.window_bottom
        return sx - 20, sy - 40, sx + 20, sy + 35

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        distance = Juel.RUN_SPEED_PPS * frame_time
        if (self.xdir == -1 and self.ydir == -1) or (self.xdir == 1 and self.ydir == 1) or (
                self.xdir == -1 and self.ydir == 1) or (self.xdir == 1 and self.ydir == -1):
            distance /= math.sqrt(2)
        self.total_frames += Juel.FRAMES_PER_ACTION * Juel.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8
        self.x += (self.xdir * distance)
        self.y += (self.ydir * distance)

        self.x = clamp(25, self.x, self.bg.w-25)
        self.y = clamp(40, self.y, self.bg.h-760)

        if self.xdir == -1:
            self.state = self.LEFT_RUN
        elif self.xdir == 1:
            self.state = self.RIGHT_RUN
        elif self.xdir == 0:
            if self.state == self.RIGHT_RUN:
                self.state = self.RIGHT_STAND
            elif self.state == self.LEFT_RUN:
                self.state = self.LEFT_STAND

    def delay_frame(self):
        if self.delay_time > 0:
            self.delay_time +=1
        if self.delay_time > 1000:
            self.delay_time = 0