
class Code:
    def __init__(self, filename):
        self.x = 0
        self.y = 0
        self.d = "right"
        with open(filename, 'r') as f:
            self.lines = f.readlines();

    def at(self, x, y):
        return self.lines[y][x]  # raises IndexError if out of bounds

    def step(self):
        if   self.d == "right":
            self.x += 1;
        elif self.d == "left":
            self.x -= 1;
        elif self.d == "up":
            self.y -= 1;
        elif self.d == "down":
            self.y += 1;

    def get(self):
        return self.at(self.x, self.y)

    def jump(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        while True:
            try:
                yield self.get()
            except IndexError:
                break
            self.step()


class State:
    def __init__(self):
        self.stack = []
        self.quoted = False
        self.active = True
