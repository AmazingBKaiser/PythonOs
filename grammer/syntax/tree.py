from . import treeNode as node

class SyntaxTree:
    root = None

    def __init__(self, root):
        self.root = root

    def get(self, node):
        return self.root.get(node)

    def add(self, child, parent):
        p = self.get(parent)
        if p != None:
            p.add(child)

    def remove(self, child, parent):
        p = self.get(parent)
        p.remove(child)

    def __str__(self):
        return self.root.toString(0)
