class DrawAPI:
    def draw_circle(self, x, y, radius):
        pass

class RedCircle(DrawAPI):
    def draw_circle(self, x, y, radius):
        print("Drawing red circle at ({}, {}) with radius {}".format(x, y, radius))

class GreenCircle(DrawAPI):
    def draw_circle(self, x, y, radius):
        print("Drawing green circle at ({}, {}) with radius {}".format(x, y, radius))

class Shape:
    def __init__(self, draw_api):
        self.draw_api = draw_api

    def draw(self):
        self.draw_api.draw_circle(self.x, self.y, self.radius)

class Circle(Shape):
    def __init__(self, x, y, radius, draw_api):
        super().__init__(draw_api)
        self.x = x
        self.y = y
        self.radius = radius

def main():
    red_circle = Circle(100, 100, 50, RedCircle())
    green_circle = Circle(200, 200, 75, GreenCircle())

    red_circle.draw()
    green_circle.draw()

if __name__ == "__main__":
    main()