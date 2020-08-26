
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


    def add_child(self, node):
        #appends node to children
        #new_node = TreeNode(node)
        if len(self.children)< 2:
            self.children.append(node)
            print(f"{node.data} added to the {self.data} family")
        else:
            print("Tree is full")
        #return new_node

    def remove_child(self, node):
        #removes node from children
        self.children = [child for child in self.children if child is not node]

    def traverse(self):
        nodes = [self]
        while len(nodes) != 0:
            current_node = nodes.pop()
            print(current_node.data)
            nodes += current_node.children

    def lookup(self, name):
        for child in self.children:
            if name == child.data:
                return child
        return None


entry = input("Enter child full name (done if finished): ")
coded = TreeNode("coded")
roots = [coded]

while entry != "done":
    roots_names=[root.data for root in roots ]
    entry = entry.split()[::-1]
    first_name = entry.pop()
    last_name = entry.pop(0)
    print(f"first_name, {first_name} || last_name: {last_name} || len(entry): {len(entry)}")
    print(f"{ roots_names}")

    if last_name in roots_names:
        #family exists
        current_node = roots[roots_names.index(last_name)]
        print("#family exists")
        if len(entry)>0 :
            print("there is a middle name")
            for name in entry:
                child = current_node.lookup(name) #what if i had more than one name in entry
                if child:
                    print("father is in tree, adding last leaf")
                    new_node = TreeNode(first_name)
                    child.add_child(new_node)
                else:
                    print("adding father and last leaf")
                    new_node = TreeNode(name)
                    current_node.add_child(new_node)
                    current_node = new_node
                    new_node.add_child(TreeNode(first_name))

        else:
            print("no father")
            if current_node.lookup(first_name):
                print(f"{first_name} is already there")
            else:
                new_node = TreeNode(first_name)
                current_node.add_child(new_node)

    elif last_name not in roots_names: #adding new family
        print("creating new root")
        new_root = TreeNode(last_name)
        roots.append(new_root)
        current_node = new_root

        if len(entry)>0  :
            for name in entry:
                new_child = TreeNode(name)
                current_node.add_child(new_child)
                current_node = new_child

        current_node.add_child(TreeNode(first_name))


    print("--"*50 )
    entry = input("Enter child full name (done if finished): ")

for root in roots:
    print(f"The {root.data} family tree:")
    root.traverse()


'''
root = TreeNode("P")
Q = root.add_child("Q")
R = root.add_child("R")
A = Q.add_child("A")
Q.add_child("B")
L = A.add_child("L")
L.add_child("E")
L.add_child("F")
L.add_child("G")

R.add_child("C")
R.add_child("D")

root.traverse()
'''
