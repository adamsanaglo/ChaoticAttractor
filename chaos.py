import pygame
import random
from random import randint


col1 = randint(1, 255)
col2 = randint(1, 255)
col3 = randint(1, 255)
col4 = randint(1, 255)
col5 = randint(1, 255)
col6 = randint(1, 255)
col7 = randint(1, 255)
col8 = randint(1, 255)
col9 = randint(1, 255)

'''
def color_gen():

    col1 = randint(1, 255)
    col2 = randint(1, 255)
    col3 = randint(1, 255)
    col4 = randint(1, 255)
    col5 = randint(1, 255)
    col6 = randint(1, 255)
    col7 = randint(1, 255)
    col8 = randint(1, 255)
    col9 = randint(1, 255)

    return col1, col2, col3, col4, col5, col6, col7, col8, col9
'''

# Model of the Classic Lorenz Equations

class Attractor:
    def __init__(self):
        self.xMin, self.xMax = -40, 60
        self.yMin, self.yMax = -40, 60
        self.zMin, self.zMax = 0, 30
        self.x, self.y, self.z = 0.1, 0.0, 0.0
        self.oX, self.oY, self.oZ = self.x, self.y, self.z
        self.dt = 0.0001
        self.a, self.b, self.c = 10, 28, 8/3
        self.pixelColour = (255, 0, 0)

    def step(self):
        self.oX, self.oY, self.oZ = self.x, self.y, self.z
        self.x = self.x + (self.dt * self.a * (self.y - self.x))
        self.y = self.y + (self.dt * (self.x * (self.b - self.z) - self.y))
        self.z = self.z + (self.dt * (self.x * self.y - self.c * self.z))

    def generate(self, x, y, xMin, xMax, yMin, yMax, width, height):
        new_x = width * ((x - xMin) / (xMax - xMin))
        new_y = height * ((y - yMin) / (yMax - yMin))
        return round(new_x), round(new_y)


    def draw(self, display):
        width, height = display.get_size()
        p1 = self.generate(self.oX, self.oY, self.xMin, self.xMax, self.yMin, self.yMax, width, height)
        p2 = self.generate(self.x, self.y, self.xMin, self.xMax, self.yMin, self.yMax, width, height)

        pattern = pygame.draw.line(display, self.pixelColour, p1, p2, 2)

        return pattern


class Application:
    def __init__(self):
        self.isRunning = True
        self.generate = None
        self.fps_timer = None
        self.attractors = []
        self.size = self.width, self.height = 1300, 600
        self.count = 0
        self.output_count = 1

    def on_init(self):
        pygame.init()
        pygame.display.set_caption("Butterfly Effect")
        self.generate = pygame.display.set_mode(self.size)
        self.isRunning = True
        self.fps_timer = pygame.time.Clock()

        colour = []
        colour.append([col1, col2, col3])
        colour.append([col4, col5, col6])
        colour.append([col7, col8, col9])

        for i in range(0, 3):
            self.attractors.append(Attractor())
            self.attractors[i].x = random.uniform(-0.1, 0.1)
            self.attractors[i].pixelColour = colour[i]

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.isRunning = False

    def on_loop(self):
        for x in self.attractors:
            x.step()

    def on_render(self):
        for x in self.attractors:
            pattern = x.draw(self.generate)
            pygame.display.update(pattern)

    def on_execute(self):
        if self.on_init() == False:
            self.isRunning = False

        while self.isRunning:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()

            self.fps_timer.tick()
            self.count += 1

        pygame.quit()


if __name__ == '__main__':
    app = Application()
    app.on_execute()







