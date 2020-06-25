import pygame
import random

# Model of the Classic Lorentz Equations
class Attractor:
    def __init__(self):
        self.xMin, self.xMax = -50, 50
        self.yMin, self.yMax = -50, 50
        self.zMin, self.zMax = 0, 60
        self.x, self.y, self.z = 0.1, 0, 0
        self.oX, self.oY, self.oZ = self.x, self.y, self.z
        self.dt = 0.01
        self.a, self.b, self.c = 10, 25, 5
        self.pixelColour = {255, 0, 0}

    def step(self):
        self.oX, self.oY, self.oY = self.x, self.y, self.z
        self.x = self.x + (self.dt * self.a * (self.y - self.x))
        self.y = self.y + (self.dt * (self.x * (self.b - self.z) - self.y))
        self.z = self.z + (self.dt * (self.x * self.y - self.c * self.z))

    def draw(self, display):
        width, height = display.get_size()
        p1 = self.generate(self.oX, self.oY, self.xMin, self.xMax, self.yMin, self.yMax, width, height)
        p2 = self.generate(self.x, self.y, self.xMin, self.xMax, self.yMin, self.yMax, width, height)

        pattern = pygame.draw.line(display, self.pixelColour, p1, p2, 2)

        return pattern

    def generate(self, x, y, xMin, xMax, yMin, yMax, width, height):
        new_x = width * ((x - xMin) / (xMax - xMin))
        new_y = height * ((y - yMin) / (yMax - yMin))
        return round(new_x), round(new_y)


    class Application:
        def __init__(self):
            self.isRunning = True
            self.generate = None
            self.fps_timer = None
            self.attractors = {}
            self.size = self.width, self.height = 1920, 1080
            self.count = 0
            self.output_count = 1

        def on_init(self):
            pygame.init()
            pygame.display.set_caption("Butterfly Effect")
            self.generate = pygame.display.set_mode(self.size)
            self.isRunning = True
            self.fps_timer = pygame.time.Clock()

            self.attractors = Attractor()

        def on_event(self, event):
            if event.type == pygame.QUIT:
                self.isRunning = False

        def on_loop(self):
            self.attractors.step()

        def on_render(self):
            pattern = self.attractors.draw(self.generate)
            pygame.display.update(pattern)

        def on_execute(self):
            if self.on_init() == False:
                self.isRunning = False

            while self.isRunning:
                for event in pygame.event.get():
                    self.on_event()

                self.on_loop()
                self.on_render()

                self.fps_timer()
                self.count += 1

            pygame.quit()

    if __name__ == '__main__':
         app = Application()
         app.on_execute()







