
from string import ascii_lowercase

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

    def display(self):
        mut = [list(s) for s in self.lines[:]]
        mut[self.y][self.x] = '∎'
        for array in mut:
            print(''.join(array), end='')


class State:
    def __init__(self):
        self.quoted = False
        self.stack = Switch()


class Switch:
    def __init__(self):
        self.i = 'a'
        self.registers = {l:list() for l in ascii_lowercase}

    def __repr__(self):
        return self.i.upper() + ': ' + ''.join(self.registers[self.i])

    def __str__(self):
        return ''.join(self.registers[self.i])

    def switch(self, char):
        self.i = char

    def empty(self):
        return bool(len(self.registers[self.i]) > 0)

    def push(self, value):
        self.registers[self.i].append(value)

    def extend(self, value):
        self.registers[self.i].extend(value)

    def peek(self):
        if len(self.registers[self.i]) > 0:
            return self.registers[self.i][-1]
        else:
            return ''

    def pop(self):
        if len(self.registers[self.i]) > 0:
            self.registers.pop()

    def clear(self):
        self.registers[self.i] = []
