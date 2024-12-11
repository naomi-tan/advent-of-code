class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    def add_child(self, child):
        self.children.append(child)
        child.add_parent(self)
    def child_count(self):
        return len(self.children)
    def add_parent(self, parent):
        self.parent = parent