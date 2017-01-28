
import actions
from structures import Code, State
import time

delay = 0.01

mappings = {
    '\\':actions.bflip,
    '/': actions.fflip,
    '!': actions.show,
    '#': actions.empty,
    "'": actions.pop,
    '@': actions.get_input,
    '*': actions.skip,
    '?': actions.skip_if_stack,
}

def execute(code, debug=False):
    state = State()
    for c in code:
        if debug:
            input()
            print('\n'*50)
            print("Stack:", ''.join(state.stack))
            print("Skipping:", state.skip)
            code.display()
        time.sleep(delay)
        if state.skip:
            state.skip = False
            continue
        if c == '"':
            state.quoted = not state.quoted
            continue
        if state.quoted:
            state.stack.append(c)
        else:
            if c in ' .':
                continue
            try:
                mappings[c](code, state)
            except KeyError:
                pass


def main(args):
    try:
        code = Code(args[1])
    except IOError:
        print("File not found.")
        return
    try:
        execute(code, bool(len(args) > 2))
    except IndexError:
        print("Execution complete.")
        return


if __name__ == '__main__':
    import sys
    try:
        main(sys.argv)
    except (EOFError, KeyboardInterrupt):
        pass
