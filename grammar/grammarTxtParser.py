from grammar.grammarSymbol import *
from grammar.grammar import *

import grammar.syntax.grammarRule as syntaxRule
import grammar.semantics.semanticRule as semanticRule


class GrammarTxtParser:
    @staticmethod
    def parseTxt(file_path):
        dict_modes = {"syntax":0, "semantics":1}

        file = open(file_path, "r")
        file_lines = file.readlines()
        grammar = Grammar("")
        first = True
        int_mode = -1 #-1 is None, 0 is Syntax, 1 is Semantics
        for line in file_lines:
            if line[0] == '@' or line == '\n':
                continue

            if line[0] == '#':
                int_mode = dict_modes[line[1:-1]]
                continue

            line = line.replace(' ', '')
            line = line.replace('.', '')

            if int_mode == 0:  
                if first:
                    grammar.start = line
                    first = False  
                else:
                    r = GrammarTxtParser.parseSyntaxLine(line[:-1])
                    grammar.addRule(r)

            elif int_mode == 1:
                r = GrammarTxtParser.parseSemanticLine(line[:-1])
                grammar.addSemanticRule(r)
            else:
                return None

        file.close()
        return grammar

    @staticmethod
    def parseSyntaxLine(line):
        next_symbols = []
        symbol_txt = ""
        rule_symbol = ""

        for cur_char in line:
            if cur_char == '|':
                next_symbols.append(GrammarTxtParser.createSymbol(symbol_txt))
                symbol_txt = ""
            elif cur_char == '=':
                rule_symbol = symbol_txt
                symbol_txt = ""
            else:
                symbol_txt += cur_char
        next_symbols.append(GrammarTxtParser.createSymbol(symbol_txt))
        return syntaxRule.GrammarRule(rule_symbol, next_symbols)

    @staticmethod
    def parseSemanticLine(line):
        str_func = ""
        symbol_txt = ""
        rule_symbol = ""
        int_operands = -1

        for i in range(0, len(line)):
            cur_char = line[i]
            if cur_char == '=':
                rule_symbol = symbol_txt
                symbol_txt = ""
            elif cur_char == '(':
                str_func = symbol_txt
                int_operands = int(line[i+1:-1])
            else:
                symbol_txt += cur_char
        return semanticRule.SemanticRule(rule_symbol, str_func, int_operands)

    @staticmethod
    def createSymbol(symbol):
        final = False
        if symbol[0] == "'":
            final = True
            symbol = symbol[1:-1]
        return GrammarSymbol(symbol, final)

