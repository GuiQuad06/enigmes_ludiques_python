def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def process(a, b, ope):
    if ope == '+':
        return a + b
    elif ope == '-':
        return a - b
    elif ope == '*':
        return a * b
    elif ope == '/':
        return a / b
    else:
        print('No supported operator')


def operation(data):
    stack = []
    for char in data:
        if char.isnumeric():
            stack.append(int(char))
        elif char in ['+', '-', '*', '/']:
            b = stack.pop()
            a = stack.pop()
            stack.append(process(a, b, char))
        else:
            raise ValueError(f'The element {char} is not valid...')
    return stack[0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    input_str = input('Veuillez rentrer une chaine representant un calcul:')

    sequence = input_str.split(' ')
    print(operation(sequence))
