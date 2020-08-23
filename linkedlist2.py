class Node:
  def __init__(self, data1, data2=None, next=None):
      self.data1 = data1
      self.data2 = data2
      self.next = next

  def get_year(self):
      return self.data1

  def get_highlight(self):
      return self.data2

  def get_next(self):
      return self.next

  def set_next(self, next ):
      self.next = next



class Linkedlist:
    def __init__(self,age , data1=None, data2=None, next=None ):
        self.head = Node(data1, data2, next)

    def get_head(self):
        return self.head

    def add_node(self, year, highlight=None, next=None ):
        new_node = Node(year, highlight, self.head)
        self.head = new_node

    def get_data(self):
        current_node = self.get_head()
        while current_node:
            if current_node.get_year() != None:
                print(f"{current_node.get_year()} - {current_node.get_highlight()}")
            current_node = current_node.get_next()





age = int(input("Please enter your age: "))

bob = Linkedlist(7,"I turned seven" )

bob.add_node(3,"I started walking")
bob.add_node(1, "I was born" )

current_node = bob.get_head()

while current_node.get_year() < age:
    current_age = current_node.get_year()+1
    if current_node.get_next().get_year() == current_age:
        current_node = current_node.get_next()
    else:
        #current_node.set_next(current_age+1)
        h = input(f"in year {current_age}, what was special? ")
        new_node = Node(current_age, h, current_node.get_next())
        current_node.set_next(new_node) 
        #current_node.set_next(current_node)



bob.get_data()
