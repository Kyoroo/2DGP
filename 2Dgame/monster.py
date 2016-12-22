from pico2d import*
import math
import random

class Monster:

    PIXEL_PER_METER = (10.0 / 0.2)
    RUN_SPEED_KMPH = 5.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None

    def __init__(self):
        self.x, self.y = random.randint(100, 2300), random.randint(100, 1040)
        self.frame1 = 0
        self.frame2 = 0
        self.state = random.randint(0,1)
        self.position = 0
        self.stand_time = 0
        self.running_time = 0
        self.total_frames = 0
        self.trace_juel = False
        self.trace_lave = False
        if Monster.image == None:
            self.image1 = load_image('monster_stand.png')
            self.image2 = load_image('monster_running.png')

    def set_background(self, bg):
        self.bg = bg

    def set_character(self, juel, lave):
        self.juel = juel
        self.lave = lave

    def draw(self):
        sx = self.x - self.bg.window_left
        sy = self.y - self.bg.window_bottom
        if self.position == 0:
            self.image1.clip_draw(self.frame1 * 86, self.state * 86, 86, 86, sx, sy)
        else:
            self.image2.clip_draw(self.frame2 * 130, self.state * 75, 130, 75, sx, sy)

    def get_bb(self):
        sx = self.x - self.bg.window_left
        sy = self.y - self.bg.window_bottom
        return sx - 30, sy - 40, sx + 20, sy + 20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        distance = Monster.RUN_SPEED_PPS * frame_time
        self.total_frames += Monster.FRAMES_PER_ACTION * Monster.ACTION_PER_TIME * frame_time
        self.frame1 = int(self.total_frames) % 6
        self.frame2 = int(self.total_frames) % 5
        if math.sqrt(math.pow(self.x-self.lave.x,2) + math.pow(self.y-self.lave.y,2)) < 200:
            self.trace_lave = True
        else:
            self.trace_lave = False
        if math.sqrt(math.pow(self.x - self.juel.x, 2) + math.pow(self.y - self.juel.y, 2)) < 200:
            self.trace_juel = True
        else:
            self.trace_juel = False
        if self.trace_lave == False and self.trace_juel == False:
            if self.position == 0:
                self.stand_time += 1
            if self.stand_time > 2000:
                self.position = 1
                self.stand_time = 0
            if self.position == 1:
                self.running_time += 1
                if self.state == 0:
                    self.x += distance
                    if self.x > 750:
                        self.state = 1
                elif self.state == 1:
                    self.x -= distance
                    if self.x < 50:
                        self.state = 0
            if self.running_time > 2000:
                if self.state == 0:
                    self.state = 1
                else:
                    self.state = 0
                self.position = 0
                self.running_time = 0
        elif self.trace_juel == True:
            if self.x - self.juel.x < 0:
                self.x += distance
                self.position = 1
                self.state = 0
            if self.x - self.juel.x > 0:
                self.x -= distance
                self.position = 1
                self.state = 1
            if self.y - self.juel.y < 0:
                self.y += distance
                self.position = 1
            if self.y - self.juel.y > 0:
                self.y -= distance
                self.position = 1
        elif self.trace_lave == True:
            if self.x - self.lave.x < 0:
                self.x += distance
                self.position = 1
                self.state = 0
            if self.x - self.lave.x > 0:
                self.x -= distance
                self.position = 1
                self.state = 1
            if self.y - self.lave.y < 0:
                self.y += distance
                self.position = 1
            if self.y - self.lave.y > 0:
                self.y -= distance
                self.position = 1

class Fireball(Monster):

    image = None

    def __init__(self):
        self.x, self.y = random.randint(100, 2300), random.randint(100, 1040)
        self.frame = 0
        self.state = random.randint(0, 1)
        self.running_time = 0
        self.total_frames = 0
        if Fireball.image == None:
            self.image = load_image('fireball.png')

    def set_background(self, bg):
        self.bg = bg

    def draw(self):
        sx = self.x - self.bg.window_left
        sy = self.y - self.bg.window_bottom
        self.image.clip_draw(self.frame * 38, self.state * 33, 38, 33, sx, sy)

    def get_bb(self):
        sx = self.x - self.bg.window_left
        sy = self.y - self.bg.window_bottom
        return sx - 19, sy - 16, sx + 19, sy + 16

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        distance = Monster.RUN_SPEED_PPS * frame_time
        self.total_frames += Monster.FRAMES_PER_ACTION * Monster.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 6
        if self.state == 0:
            self.x += distance
            if self.x > 2381:
                self.state = 1
        if self.state == 1:
            self.x -= distance
            if self.x < 19:
                self.state = 0