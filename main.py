from hamming_conversion import bin2int_big_endian, bin2int_little_endian


def decoder_boutisme(char, endian):
    string = ''
    for i in range(0, len(char), 8):
        bloc = char[i: i + 8]
        if endian == 'big-endian':
            c = chr(bin2int_big_endian(bloc))
        elif endian == 'little-endian':
            c = chr(bin2int_little_endian(bloc))
        else:
            raise ValueError(f'Le boutisme en question {endian} n''existe pas...')
        string += c
    return string


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    res = ''
    msg = []
    index = 0
    with open('inputs/enigme8_1.txt', mode='r', encoding='utf-8') as fd:
        message = fd.read().replace('\n', '')

    print(decoder_boutisme(message, 'big-endian'))
    # Message is not in little-endian
    # print(decoder_boutisme(message, 'little-endian'))
