import re


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


def convert_number(n):
    try:
        num = int(n)
    except ValueError:
        num = float(n)
    return num


def seek_operation(data):
    ope = re.search('[-+*/](?=\s|$)', data)
    if not ope:
        print(data)
        return
    else:
        sliced_data = data[:ope.end()].split(' ')

        # Convert string into number
        x = convert_number(sliced_data[-3])
        y = convert_number(sliced_data[-2])
        result = process(x, y, sliced_data[-1])

        # Find the first occurrence of a space from the right
        first_space_index = data[:ope.end()].rfind(' ')

        if first_space_index == -1:
            return -1

        # Find the second occurrence of a space from the right by slicing the string
        second_space_index = data[:ope.end()].rfind(' ', 0, first_space_index)

        new_data = data.replace(data[second_space_index - 1:ope.end()], str(result))
        # Recursive Method
        seek_operation(new_data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    input_str = input('Veuillez rentrer une chaine representant un calcul:')

    seek_operation(input_str)
