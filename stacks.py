from random import randrange
from random import choice


class Node:
    def __init__(self, data1, data2=None, next=None):
        self.data1 = data1
        self.data2 = data2
        self.next = next

    def __str__(self):
        return f"{self.data1} {self.data2} "


class Stack:
    def __init__(self, limit):
        self.limit = limit
        self.top = None
        self.length = 0

    def is_empty(self):
        return self.length==0

    def is_full(self):
        return self.length == self.limit


    def push(self, *args):
        if self.is_full():
            print ("Stack is full!")
        else:
            new_node = Node(*args, self.top)
            self.top = new_node
            self.length += 1

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            out = self.top
            self.top = out.next
            self.length -=1
            return out


    def peak(self):
        if self.is_empty() == True:
            print("Stack is empty")
        else:
            return self.top


    def get_data(self):
        current_node = self.top
        while current_node:
            if current_node.data1 != None:
                print (f"{str(current_node.data1)} {str(current_node.data2)} ")
            current_node = current_node.next


colors = ["red", "blue", "green", "yellow"]
deck = Stack(20)

for i in range (20):
    deck.push(choice(colors), randrange(10))

print("--"*50)
print("Deck:", deck.length)
print("--"*50)
deck.get_data()

player1 = Stack(5)
player2 = Stack(5)

for i in range(5):
     x = deck.pop()
     player1.push(x.data1, x.data2)
     y = deck.pop()
     player2.push(deck.pop())

print("--"*50)
print("First player cards:", player1.length)
print("--"*50)
player1.get_data()

print("--"*50)
print("Second player cards: " , player2.length)
print("--"*50)
player2.get_data()

print("--"*50)
print("peak: ", deck.length )
print("--"*50)
print(deck.peak())
