import grammer.grammerTxtParser as parser

import grammer.semantics.functionList as fList
import grammer.semantics.variableList as vList
import grammer.semantics.semanticList as sList
import grammer.semantics.a as a
import grammer.semantics.add as add
import grammer.semantics.sub as sub
import grammer.semantics.mult as mult
import grammer.semantics.div as div
import grammer.semantics.default as default



p = parser.GrammerTxtParser

g = p.parseTxt("data/testGrammer.txt")
print(g)

f = fList.FunctionList({'+':add.Add(), '-':sub.Sub(), '*':mult.Mult(), '/':div.Div(), 'a':a.A(), "DEFAULT":default.CombineStrings()})
v = vList.VariableList({"h":5, "i":90})
s = sList.SemanticList({"func1":f, "operation":f, "variable": v, "default":f})
g.semanticList = s
#g.buildTree("30*2+7/35*2+4")
print(g.calcSymbol("3*2+6/3*2+4"))
