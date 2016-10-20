from pico2d import*

class Background01:

    image = None

    def __init__(self):
        if Background01.image == None:
            self.x, self.y = 400, 300
            self.image = load_image('Background_01.png')

    def draw(self):
        self.image.draw(self.x, self.y)