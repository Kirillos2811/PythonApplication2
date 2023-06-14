class Turtle:

    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
 
    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_right(self):
        self.x += self.s

    def go_left(self):
        self.x -= self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        self.s -= 1

    def count_moves(self, x2, y2):
        return abs(x2 - self.x) + abs(y2 - self.y)

    def print_coords(self):
        print(f"X: {self.x}", f"Y: {self.y}")

turtle = Turtle(0, 0, 1)
turtle.evolve()
turtle.go_up()
turtle.print_coords()
print(turtle.count_moves(5, 10))
