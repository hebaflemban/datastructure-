class Node:
  def __init__(self, data1, data2, next=None):
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


  #if i want to set highlight, I should just edit it in the initialization or define a setter

class Linkedlist:
    def __init__(self,data1, data2, next=None ):
        self.head = Node(data1, data2, next)

    def get_head(self):
        return self.head

    def add_node(self, year, highlight):
        new_node = Node(year, highlight)
        new_node.next(self.head)
        self.head = new_node
