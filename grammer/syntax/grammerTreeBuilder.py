from . import tree

class SyntaxTreeBuilder:
    @staticmethod
    def createTree(grammer, symbol):
        all_symbols = [symbol]
        tree = SyntaxTree(symbol)

        symbol.symbol = symbol.symbol.replace(' ', '')

        all_symbols = SyntaxTreeBuilder.splitBrackets(symbol, tree)
 

        for k in sorted(grammer.operations):
            o = grammer.operations[k].symbol
            p = (SyntaxTreeBuilder.splitSymbol(s, o, tree) for s in all_symbols)
            all_symbols = sum(p, [])
        return tree

    @staticmethod
    def splitSymbol(symbol, operation, tree):
        split = symbol.splitSymbol(operation, True)
        for s in split:
            tree.add(s, symbol)
        #print(split)
        return split

    @staticmethod
    def splitBrackets(symbol, tree):
        split_left = symbol.splitSymbol("(", True)
        split = {}
        for s in split_left:
            split_right = s.splitSymbol(")", True)
            for a in split_right:
                split[a.symbol] = a

        for s in split.values():
            tree.add(s, symbol)
        print(tree)
        return list(split.values())