from huffman_algo import compresser_bits
from huffman_secret import SECRET
import string


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def oracle(msg):
    msg_compresse = compresser_bits(SECRET + msg)
    return len(msg_compresse)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    char = []
    dico = {}
    print_hi('PyCharm')
    print('Craquage du Secret !!!')

    # When we concatenate a new character after the SECRET, the len returned by the oracle
    # (the length of a compressed message) can take 2 values, and the value closer to
    # the original oracle message, represent a character already contained in the secret
    # Step 1: Process the two oracle values and identify the minimum one
    for c in string.ascii_lowercase:
        dico[c] = oracle(c)
    contained_char_oracle = min(dico.values())

    # Step 2: Generate a list with the characters contained in the secret message
    for key, value in dico.items():
        char.append(key) if value == contained_char_oracle else None

    print(char)