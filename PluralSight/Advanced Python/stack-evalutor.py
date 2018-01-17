# A simple stack based lanuguage to show the use case of while..else
import operator


def is_comment(item):
    return isinstance(item, str) and item.startswith("#")


def execute(program):
    """
    Execute a stack program

    Args:
        program: Any stack-like containing where each item in the stack
        is a callable operators or non-callable operands. The top-most items
        on the stack may be strings beginning with '#' for the purpose of 
        documentation. Stack-like means support for:
            
            item = stack.pop()  # Remove and return the top item
            stack.append(item)  # Push an item to the top
            if stack:           # False in a boolean context when empty
    """
    # Find the start of the 'program' by skipping and item which is comment
    while program:
        item = program.pop()
        if not is_comment(item):
            program.append(item)
            break
    else:  # nobreak
        print("NO program!")
        return

    # Evaluate the program
    pending = []
    while program:
        item = program.pop()
        if callable(item):
            try:
                result = item(*pending)
            except Exception as e:
                print("Error:", e)
                break
            program.append(result)
            pending.clear()
        else:
            pending.append(item)
    else:
        print("Program successful")
        print("Result", pending)
    
    print("Finished")


if __name__ == '__main__':
    program = list(reversed((
        "# A short stack program to add",
        "# and multiply some contents",
        5,
        2,
        operator.add,
        3,
        operator.mul)))
    execute(program)

