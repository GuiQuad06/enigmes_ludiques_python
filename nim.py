from graph import Graph

class Nim:
    def __init__(self, n, p, bot=False):
        self.n = n
        self.p = p
        self.cpt = n
        self.bot = bot
        self.possibilities = self.process_p()
        self.graph = Graph(self.n, self.p)

    def process_p(self):
        tmp = []
        for i in range (self.p):
            tmp.append(i + 1)
        return tmp

    def __repr__(self):
        res = ''
        for _ in range(self.cpt):
            res += '| '
        return res

    def play(self, m):
        if m not in self.possibilities:
            raise Exception(f'Value should be in this range :{self.possibilities}')
        if self.cpt:
            self.cpt -= m

    def bot_play(self):
        if self.cpt:
            for i in range(self.cpt - 1, self.cpt - (self.p + 1), -1):
                if i in self.graph.kernel:
                    self.cpt = i
                    return
