import grammer.syntax.grammerTreeBuilder as builder
import grammer.syntax.treeNode as snode
import grammer.syntax.tree as tree
import grammer.grammerSymbol as gsymbol

class Grammer:
    rules = []
    start = ""
    semmanticList = None
    semantic_rules = []

    def __init__(self, start, semanticList=None):
        i = 0
        self.rules = []
        self.start = start
        self.semanticList = semanticList
        self.semantic_rules = []

    def addSemanticRule(self, rule):
        self.semantic_rules.append(rule)

    def addRule(self, rule):
        self.rules.append(rule)

    def getSemanticRuleWithSymbol(self, str_parent, str_child):
        for rule in self.semantic_rules:
            if str_parent == rule.symbol:
                return (rule, str_child)
        return (None, None)

    def getSymbolRule(self, symbol):
        for r in reversed(self.rules):
            for s in r.nextSymbols:
                if s.symbol in symbol:
                    return (r.symbol, s.symbol)
        return (None, None)

    def calcSymbol(self, symbol):
        tree = self.buildTree(symbol)
        print(symbol)
        return self.calc(tree.root, [])[0]

    def calc(self, node, stack):
        symbol = "DEFAULT"
        op, tmp = self.getSemanticRuleWithSymbol(symbol, symbol)

        for a in node.children:
            if a.children == []:
                stack.append(a.value.symbol)
            else:
                o, s = self.getSemanticRuleWithSymbol(a.value.symbol, a.children[0].value.symbol)
                if o !=  None:
                    op = o
                    symbol = s
                else:
                    stack = self.calc(a, stack)

        operands = stack[-op.operands:]
        stack = stack[:-op.operands]
        r = self.semanticList.call(op.func, symbol, operands)
        print(stack, operands, r)
        stack.append(r)
        return stack


    def buildTree(self, str_symbol):
        t = tree.SyntaxTree(str_symbol)
        node_list = []

        i = 0

        while i < len(str_symbol):
            i += 1
            str_result, symbol_replaced = self.getSymbolRule(str_symbol[:i])
            if str_result != None:
                node_list.append(snode.SyntaxTreeNode(gsymbol.GrammerSymbol(symbol_replaced)))
                str_symbol = str_symbol[i:]
                i = 0
        if str_symbol != "":
            return None

        str_line = ""
        while self.start != str_line:
            #print(str_list_tree[-1])
            str_line = "".join([n.value.symbol for n in node_list])
            #print(str_line)
            str_result, str_replaced = self.getSymbolRule(str_line)
            if str_replaced == None:
                break

            l, result, str_text = Grammer.findAllSubStrings(str_line, str_replaced, str_result)

            for r in result:
                l2 = -1
                r2 = 0
                node = None
                for n in node_list:
                    if r2 == r:
                        node = snode.SyntaxTreeNode(gsymbol.GrammerSymbol(str_result))
                        l2 = l
                    if l2 > 0:
                        node.children.append(n)
                    l2 -= len(n.value.symbol)
                    if l2 == 0:
                        index = node_list.index(node.children[0])
                        node_list[index] = node
                        [node_list.remove(n2) for n2 in node.children[1:]]
                        break
                    r2 += len(n.value.symbol)
        t = tree.SyntaxTree(node_list[0])
        print(t)
        return t

    @staticmethod
    def findAllSubStrings(str_text, str_find, str_replacer):
        l = len(str_find)
        result = []
        for i in range(0, len(str_text)-l+1):
            if i > len(str_text)-l+1:
                break
            #print(i, str_text[i:i+l] + "==" + str_find)
            if str_text[i:i+l] == str_find:
                result.append(i)
                str_new = str_text[:i]
                str_new += str_replacer
                if i <= len(str_text)-l:
                    str_new += str_text[i+l:]
                str_text = str_new
                #str_text[i:i+l] = [s for s in str_replacer]
        return (l, result, str_text)

    def __str__(self):
        s = ""

        for r in self.rules:
            s += str(r) + "\n"

        s += "\n"

        for r in self.semantic_rules:
            s += str(r) + "\n"

        return s
