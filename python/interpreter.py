
import actions
from structures import Code, State
import time
from string import ascii_lowercase

delay = 0.01

mappings = {
    '\\':actions.bflip,
    '/': actions.fflip,
    '!': actions.show,
    '#': actions.clear,
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
            print("Stack", repr(state.stack))
            code.display()
        time.sleep(delay)
        if c == '"':
            state.quoted = not state.quoted
            continue

        if state.quoted:
            state.stack.push(c)

        else:
            if c in ' .':
                continue
            if c in ascii_lowercase:
                state.stack.switch(c)
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
