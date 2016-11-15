from pico2d import*
import random

class Monster:

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None

    def __init__(self):
        self.x, self.y = random.randint(100, 700), 80
        self.frame1 = 0
        self.frame2 = 0
        self.state = random.randint(0,1)
        self.position = 0
        self.stand_time = 0
        self.running_time = 0
        self.total_frames = 0
        if Monster.image == None:
            self.image1 = load_image('monster_stand.png')
            self.image2 = load_image('monster_running.png')

    def draw(self):
        if self.position == 0:
            self.image1.clip_draw(self.frame1 * 86, self.state * 86, 86, 86, self.x, self.y)
        else:
            self.image2.clip_draw(self.frame2 * 130, self.state * 75, 130, 75, self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 43, self.x + 30, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        distance = Monster.RUN_SPEED_PPS * frame_time
        self.total_frames += Monster.FRAMES_PER_ACTION * Monster.ACTION_PER_TIME * frame_time
        self.frame1 = int(self.total_frames) % 6
        self.frame2 = int(self.total_frames) % 5
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

class Fireball(Monster):

    image = None

    def __init__(self):
        self.x, self.y = random.randint(100, 700), 160
        self.frame = 0
        self.state = random.randint(0, 1)
        self.running_time = 0
        self.total_frames = 0
        if Fireball.image == None:
            self.image = load_image('fireball.png')

    def draw(self):
        self.image.clip_draw(self.frame * 38, self.state * 33, 38, 33, self.x, self.y)

    def get_bb(self):
        return self.x - 19, self.y - 16, self.x + 19, self.y + 16

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self, frame_time):
        distance = Monster.RUN_SPEED_PPS * frame_time
        self.total_frames += Monster.FRAMES_PER_ACTION * Monster.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 6
        if self.state == 0:
            self.x += distance
            if self.x > 781:
                self.state = 1
        if self.state == 1:
            self.x -= distance
            if self.x < 19:
                self.state = 0