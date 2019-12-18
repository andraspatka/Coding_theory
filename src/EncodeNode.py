
class EncodeNode(object):
    def __init__(self, symbol = '', count = 0, prob = 0, code = '', interval = (0,0)):
        self.symbol = symbol
        self.count = count
        self.prob = prob
        self.code = code
        self.interval = interval

    def __repr__(self):
        #return f"{self.symbol}: {self.count}, {self.prob}, {self.code}, ({self.interval[0], self.interval[1]})\n"
        return f"{self.symbol}: ({self.interval[0]}, {self.interval[1]});"