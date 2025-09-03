import string

ALPHA = list(string.ascii_lowercase)

def from_letter_to_index(char):
    for i, letter in enumerate(ALPHA):
        if char.lower() == letter:
            return i
    return None

def from_index_to_letter(index):
    for i, letter in enumerate(ALPHA):
        if index == i:
            return letter
    return None

def process_key(cipher, msg):
    _key = []
    for i in range(len(cipher)):
        a = from_letter_to_index(cipher[i])
        b = from_letter_to_index(msg[i])
        _key.append(from_index_to_letter((a - b) % 26))
    return _key

def decrypt(cipher, key, file_path):
    msg = []
    shift_key = 0
    for i in range(len(cipher)):
        if cipher[i] not in list(string.ascii_lowercase) and cipher[i] not in list(string.ascii_uppercase):
            msg.append(cipher[i])
            shift_key += 1
        else:
            a = from_letter_to_index(cipher[i])
            b = from_letter_to_index(key[i - shift_key])
            msg.append(from_index_to_letter((a - b) % 26))
    with open(file_path, 'w') as f:
        f.write(''.join(msg))

def parse_input(file_path):
    with open(file_path, 'r') as f:
        cipher = f.read()
    return cipher

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')

    key = []
    secretMessage = parse_input('inputs//enigme9.txt')
    shortKey = 'python'
    for i in range( len(secretMessage)):
        key.append(shortKey[i % (len(shortKey))])

    decrypt(secretMessage, key, 'output.txt')
