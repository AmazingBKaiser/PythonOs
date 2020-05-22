class GrammarSymbol:
    symbol = ""
    isFinal = True

    def __init__(self, symbol, isFinal=False):
        self.symbol = symbol
        self.isFinal = isFinal

    def get(self):
        return (self.symbol, self.isFinal)

    def splitSymbol(self, operation, addOp = False):
        if self.isFinal:
            return [self]

        symbols = []
        symbol_txt = ""
        for cur_char in self.symbol:
            if cur_char == operation:
                symbols.append(GrammarSymbol(symbol_txt))
                if addOp:
                    symbols.append(GrammarSymbol(operation, True))
                symbol_txt = ""
            else:
                symbol_txt += cur_char
        if symbol_txt == "":
            symbol_txt = self.symbol
        symbols.append(GrammarSymbol(symbol_txt))
        return symbols

    def splitAll(self, operations, addOp = False):
        allSymbols = [self.symbol]
        for k in operations:
            s = GrammarSymbol(".".join([str(element) for element in allSymbols]))
            allSymbols = s.splitSymbol(k, addOp)
        s = GrammarSymbol(".".join([str(element) for element in allSymbols]))
        return s.splitSymbol(".")

    def __str__(self):
        return self.symbol
