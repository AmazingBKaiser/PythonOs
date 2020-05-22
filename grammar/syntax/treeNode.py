class SyntaxTreeNode:
    children = []

    def __init__(self, value):
        self.value =  value
        self.children = []

    def get(self, node):
        if str(node) == str(self.value):
            return self
        for a in self.children:
            n = a.get(node)
            if n != None:
                return n
        return None

    def add(self, child):
        self.children.append(SyntaxTreeNode(child))

    def remove(self, child):
        for a in self.children:
            if a.value == child:
                self.children.remove(a)

    def toString(self, i):
        return "\n" + (i * "\t") + str(self.value) + "".join([element.toString(i+1) for element in self.children])
