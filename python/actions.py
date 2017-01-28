

def dump_stack(code, state):
    print(''.join(state.stack))
    state.stack = []


def flip_back(code, state):
    """
    Redirect code execution using a backslash mirror \ .
    """
    change = {
        'up':'left',
        'down':'right',
        'left':'up',
        'right':'down',
    }
    if state.active:
        code.d = change[code.d]


def flip_forward(code, state):
    """
    Redirect code execution using a forward slash mirror / .
    """
    change = {
        'up':'right',
        'down':'left',
        'left':'down',
        'right':'up',
    }
    if state.active:
        code.d = change[code.d]


def toggle_junctions(code, state):
    """
    Activate or deactivate junctions.
    """
    state.active = not state.active
