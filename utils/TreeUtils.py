class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
    def add_child(self, child):
        self.children.append(child)
    def child_count(self):
        return len(self.children)
    def get_child_values(self):
        vals = []
        for child in self.children:
            vals.append(str(child.data.value))
        return ','.join(vals)