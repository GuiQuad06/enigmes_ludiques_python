from hamming_conversion import *


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


def decode_hamming(bit):
    corrected_bits = ''
    error = None
    for i in range(0, len(bit), 7):
        bloc = bit[i: i + 7]
        bloc_list = list(map(int, list(bloc)))

        pos_err = detect_err(bloc_list)
        if pos_err != -1:
            error = (bloc, i//(7*2) + 1, pos_err)
            bloc_list = correct_err(bloc_list, pos_err)
            bloc = ''.join(map(str, bloc_list))
        corrected_bits += bloc[:4]
    return decoder_boutisme(corrected_bits, 'big-endian'), error


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    with open('inputs/enigme8_2.txt', mode='r', encoding='utf-8') as fd:
        bin = fd.read().replace('\n', '')
        msg, err = decode_hamming(bin)
        if err is not None:
            print(f'erreur sur le bloc {err[0]} (char {err[1]}) position {err[2]}')
        print(f'le message apres correction est: {msg}')
