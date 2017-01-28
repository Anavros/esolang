

def empty(code, state):
    state.stack = []

def pop(code, state):
    if state.stack:
        state.stack.pop()

def show(code, state):
    print(''.join(state.stack))

def peek(code, state):
    if state.stack:
        print(state.stack[-1])

def bflip(code, state):
    change = { 'up':'left', 'down':'right', 'left':'up', 'right':'down' }
    code.d = change[code.d]

def fflip(code, state):
    change = { 'up':'right', 'down':'left', 'left':'down', 'right':'up' }
    code.d = change[code.d]

def skip(code, state):
    state.skip = True

def skip_if_stack(code, state):
    if len(state.stack) < 1:
        state.skip = True

def get_input(code, state):
    txt = input("> ").strip()
    if txt:
        state.stack.append(txt)
