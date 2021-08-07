# https://www.algoexpert.io/questions/Breadth-first%20Search
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        visit = set()
        while queue:
            node = queue.pop(0)
            visit.add(node)
            array.append(node.name)
            for child in node.children:
                if not child in visit:
                    queue.append(child)
        return array
        