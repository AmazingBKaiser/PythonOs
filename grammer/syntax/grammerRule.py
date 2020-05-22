class GrammerRule:
    nextSymbols = []
    symbol = ""

    def __init__(self, symbol, nextSymbols):
        self.symbol = symbol
        self.nextSymbols = nextSymbols

    def getNext(self):
        return nextSymbols

    def __str__(self):
        s = self.symbol + " = "
        for symbol in self.nextSymbols:
            s += str(symbol) + " | "

        return s[:-3]
