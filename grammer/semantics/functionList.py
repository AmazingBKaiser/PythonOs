class FunctionList:
    funcs = {}

    def __init__(self, funcs):
        self.funcs = funcs

    def call(self, a, p):
        return self.funcs[a].call(p)

