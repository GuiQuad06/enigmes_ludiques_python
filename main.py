from huffman_algo import compresser_bits
from huffman_secret import SECRET


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def oracle(msg):
    msg_compresse = compresser_bits(SECRET + msg)
    #return len(msg_compresse)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    message = input("Entrez un message:")
    print(oracle(message))
