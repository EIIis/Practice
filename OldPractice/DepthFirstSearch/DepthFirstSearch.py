# https://www.algoexpert.io/questions/Depth-first%20Search

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        return self.dfsHelp(array, self, set())
    
    def dfsHelp(self, array, node, visit):
        visit.add(node)
        array.append(node.name)
        for child in node.children:
            if not child in visit:
                self.dfsHelp(array, child, visit)
        return array
