import grammar.grammarTxtParser as parser

import grammar.semantics.functionList as fList
import grammar.semantics.variableList as vList
import grammar.semantics.semanticList as sList
import grammar.semantics.a as a
import grammar.semantics.add as add
import grammar.semantics.sub as sub
import grammar.semantics.mult as mult
import grammar.semantics.div as div
import grammar.semantics.default as default



p = parser.GrammarTxtParser

# g = p.parseTxt("data/testGrammar.txt")
# print(g)
#
# f = fList.FunctionList({'+':add.Add(), '-':sub.Sub(), '*':mult.Mult(), '/':div.Div(), 'a':a.A()})
# v = vList.VariableList({"h":5, "i":90})
# s = sList.SemanticList({"func1":f, "operation":f, "variable": v})
# g.semanticList = s
# #g.buildTree("30*2+7/35*2+4")
# print(g.calcSymbol("32*2+6/3*2+4"))
# print(g.calcSymbol("(2+6)"))
# print(g.calcSymbol("32*(2+6)+4"))
# print(g.calcSymbol("32*(2+6)/3*2+4"))



g = p.parseTxt("data\mathGrammer.txt")
print(g)

f = fList.FunctionList({'+':add.Add(), '-':sub.Sub(), '*':mult.Mult(), '/':div.Div()})
s = sList.SemanticList({"operation":f})
g.semanticList = s
#g.buildTree("30*2+7/35*2+4")
print(g.calcSymbol("32*2+6/3*2+4"))
print(g.calcSymbol("(2+6)"))
print(g.calcSymbol("32*(2+6)+4"))
print(g.calcSymbol("32*(2+6)/3*2+4"))
