
import actions
from structures import Code, State

mappings = {
    '\\':actions.flip_back,
    '/': actions.flip_forward,
    '*': actions.toggle_junctions,
    '!': actions.dump_stack,
}

def execute(code):
    state = State()
    for c in code:
        if c == '"':
            state.quoted = not state.quoted
            continue
        if state.quoted:
            state.stack.append(c)
        else:
            if c == ' ':
                continue
            try:
                mappings[c](code, state)
            except KeyError:
                pass


def main(filename):
    try:
        code = Code(filename)
    except IOError:
        print("File not found.")
        return
    try:
        execute(code)
    except IndexError:
        print("Execution complete.")
        return


if __name__ == '__main__':
    import sys
    main(sys.argv[1])
