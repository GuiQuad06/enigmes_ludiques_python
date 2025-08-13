import argparse
import json
import hashlib
import itertools
import time

dico = {}

USAGE = "python main.py [-f]"
DESCRIPTION = "Enigme 4 Hash table, -f option is to provide full letters choice"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def generate_pwd(full):
    global dico
    # Define the set of characters (lowercase letters)
    characters = 'abcdefghijklmnopqrstuvwxyz' if full else 'abc'
    # Generate all possible 5-character combinations
    passwords = itertools.product(characters, repeat=5)

    # Iterate over the passwords
    for password in passwords:
        h = hashlib.sha256(bytes(''.join(password), 'utf-8'))
        dico[h.hexdigest()] = ''.join(password)


def write_in_file(file_name):
    global dico
    with open(file_name, mode='w', encoding='utf-8') as fd:
        json.dump(dico, fd)

def read_from_file(file_name):
    with open('hash.json', mode='r', encoding='utf-8') as fd:
        received_dico = json.load(fd)

    print(received_dico.get('9e69e7e29351ad837503c44a5971edebc9b7e6d8601c89c284b1b59bf37afa80'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage=USAGE, description=DESCRIPTION)
    parser.add_argument("-f", dest="full_alpha", action='store_true', default=False)
    arg = parser.parse_args()

    print_hi('PyCharm')

    start = time.time()

    generate_pwd(arg.full_alpha)
    write_in_file('hash.json')

    stop = time.time()
    print(f'program ended in {stop - start} seconds')

    start = time.time()
    read_from_file('hash.json')

    stop = time.time()
    print(f'password found in {stop - start} seconds')
