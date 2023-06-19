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

    @staticmethod
    def recursive_seeking(x, y, x2, y2, s, count):
        if x == x2 and y == y2:
            return count
        if x2 > x:
            return Turtle.recursive_seeking(x + s, y, x2, y2, s, count + 1)
        elif x2 < x:
            return Turtle.recursive_seeking(x - s, y, x2, y2, s, count + 1)
        elif y2 > y:
            return Turtle.recursive_seeking(x, y + s, x2, y2, s, count + 1)
        elif y2 < y:
            return Turtle.recursive_seeking(x, y - s, x2, y2, s, count + 1)

    def count_moves(self, x2, y2):
        try:
            return self.recursive_seeking(self.x, self.y, x2, y2, self.s, 0)
        except RecursionError:
            return "Невозможно добраться до цели"

    def print_coords(self):
        print(f"X: {self.x}", f"Y: {self.y}")

turtle = Turtle(0, 0, 1)
turtle.evolve()
turtle.go_up()
turtle.print_coords()
print(turtle.count_moves(6, 10))
