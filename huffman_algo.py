class TreeNode:
    def __init__(self, value=0, char='', zero=None, one=None):
        self.value = value
        self.char = char
        self.zero = zero
        self.one = one

    def __lt__(self, other):
        return self.value < other.value

    def swap(self, other):
        self.value, other.value = other.value, self.value
        self.char, other.char = other.char, self.char
        self.zero, other.zero = other.zero, self.zero
        self.one, other.one = other.one, self.one


def count_characters(msg):
    dico = {}
    for char in msg:
        if char not in dico.keys():
            dico[char] = 1
        else:
            dico[char] += 1
    return dico


def construct_tree(map):
    nodes = [TreeNode(value, key) for key, value in map.items()]

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


def compresser_bits(message):
    # Step 1: Construire un dico qui contient les caracteres par order d'apparition avec le total d'occurences
    char_map = count_characters(message)
    # Step 2: Sort the dictionary from the lowest value to the highest one
    sorted_char_map = {k: char_map[k] for k in sorted(char_map, key=lambda v: char_map[v])}
    # Step 3: Create the Binary Tree Leafs
    tree = construct_tree(sorted_char_map)
