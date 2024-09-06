from TreeNode import TreeNode

char_coding_mapping = {}


def count_characters(msg):
    dico = {}
    for char in msg:
        if char not in dico.keys():
            dico[char] = 1
        else:
            dico[char] += 1
    return dico


def construct_tree(mapping):
    nodes = [TreeNode(value, key) for key, value in mapping.items()]

    while len(nodes) > 1:
        next_level = []
        for i in range(0, len(nodes), 2):
            zero = nodes[i]
            one = nodes[i + 1] if i + 1 < len(nodes) else None
            if one and one < zero:
                zero.swap(one)

            parent = TreeNode(zero.value + (one.value if one else 0), '' if one else zero.char, zero, one)
            next_level.append(parent)
        nodes = next_level

    return nodes[0] if nodes else None


def convert_char(bin_tree, bin_str):
    global char_coding_mapping
    if bin_tree.one is None or bin_tree.zero is None:
        char_coding_mapping[bin_tree.char] = bin_str
        return
    convert_char(bin_tree.zero, bin_str + '0')
    convert_char(bin_tree.one, bin_str + '1')


def process(msg):
    global char_coding_mapping
    res = ''
    for char in msg:
        res += char_coding_mapping[char]
    return res


def compresser_bits(message):
    # Step 1: Construire un dico qui contient les caracteres par order d'apparition avec le total d'occurences
    char_map = count_characters(message)
    # Step 2: Sort the dictionary from the lowest value to the highest one
    sorted_char_map = {k: char_map[k] for k in sorted(char_map, key=lambda v: char_map[v])}
    # Step 3: Create the Binary Tree from leaves
    tree = construct_tree(sorted_char_map)
    # Step 4: Create a map between character and raw binary
    convert_char(tree, '')
    # Step 5: Process the message and replace each character
    return process(message)
