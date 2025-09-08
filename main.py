TRUCHET_VALUES = [0, 1, 2, 3]
CONVERSION_MAP = [0, 0, 1, 1]

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def parse_input(path):
    with open(path) as f:
        message = f.read().splitlines()
        # The map can cast str to int
        message = [ list(map(int, line.split(' '))) for line in message ]
    return message

def convert_2_ascii(byte):
    res = 0
    for i in range(7, -1, -1):
        res += pow(2, i) * byte[7 - i]
    return res

def process(data):
    res = ''
    for character in data:
        ascii = []
        for elt in character:
            if elt not in TRUCHET_VALUES:
                continue
            else:
                ascii.append(CONVERSION_MAP[elt])
        res += chr(convert_2_ascii(ascii))
    return res


if __name__ == '__main__':
    print_hi('PyCharm')
    toto = parse_input('inputs//enigme11.txt')
    print(process(toto))
