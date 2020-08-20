

#Node({"1" : "I was born"}, 2)
#Node({"3" : "I started walking"}, 4)
#Node({"7" : "First day of school"}, 8)




'''
def displayLife(age):

    for i in range(0, age):
        y.append(Node(i, i+2)
'''


class Node:

    def __init__(self, year, highlight=None, next_year=None):
        self.year = year
        self.highlight = highlight
        self.next_year = next_year

    def __str__(self):
        msg = (f"{self.year} : {self.highlight} : {self.next_year}")
        return msg

    def get_year(self):
        return self.year

    def set_highight(self,highlight):
        self.highlight = highlight

    def get_highight(self):
        return self.highlight


    def get_next_year(self):
        return self.next_year

    def set_link(self, next_year):
        self.next_year = next_year


class Lifelist:
    def __init__(self, age, highlight=None):
        self.head_node = Node(0, "I was born")
        for i in range(1,age+1):
            new_node = Node(i, None, self.head_node )
            self.head_node = new_node


    def set_highight(self, highlight):
        return Node.get_highight()
    '''
    def get_head_node(self):
        return self.head_node

    def get_year(self):
        year = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_year() != None:
                year += str(current_node.get_year()) + "\n"
            current_node = current_node.get_next_year()
        return year

    def addToHead(self, next_year, highlight_n):
        New_node = Node(next_year, highlight_n)
        New_node.set_link(self.head_node)
        New_node = self.head_node
    '''

    def print_life(self):
        for i in range(1,age+1):
            print( Node(i))






age = int(input("Please enter your age: "))
h = input("What was special is that year? ")

bob = Lifelist(age)
for i in range(1,age+1):
    if Node(i).get_highight()==None:
        h = input(f"in year {i}, what was special? ")
        Node(i).set_highight(h)

bob.print_life()
