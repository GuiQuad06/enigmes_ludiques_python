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

