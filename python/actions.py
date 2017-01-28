

def clear(code, state):
    state.stack.clear()

def pop(code, state):
    state.stack.pop()

def show(code, state):
    print(str(state.stack))

def peek(code, state):
    print(state.peek())

def bflip(code, state):
    change = { 'up':'left', 'down':'right', 'left':'up', 'right':'down' }
    code.d = change[code.d]

def fflip(code, state):
    change = { 'up':'right', 'down':'left', 'left':'down', 'right':'up' }
    code.d = change[code.d]

def skip(code, state):
    code.step()

def skip_if_stack(code, state):
    if not state.stack.empty():
        code.step()

def get_input(code, state):
    txt = input("> ").strip()
    if txt:
        state.stack.push(txt)
