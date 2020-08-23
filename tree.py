class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


    def add_child(self, node):
        #appends node to children
        self.children.append(node)

    def remove_child(self, node):
        #removes node from children
        self.children = [child for child in self.children if child is not node]

    def traverse(self):
        nodes = [self]
        while len(nodes) > 0:
            current_node = nodes.pop()
            print(current_node.data)
            nodes += current_node.children
            print(nodes.data)



Batarfi = TreeNode("Batarfi")
Batarfi.add_child(TreeNode("Nisreen"))

Nisreen = TreeNode("Nisreen")
Nisreen.add_child(TreeNode("Heba"))
Nisreen.add_child(TreeNode("Anmar"))

#Batarfi.traverse()
print(Batarfi.children.data)
