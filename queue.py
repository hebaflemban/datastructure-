from random import randint


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self, limit=None, front=None, back=None):
        self.front = front
        self.back = back
        self.limit = limit
        self.length = 0


    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.limit


    def enqueue (self, data):
        if self.is_full():
            print("Sorry line is closed")
        else:
            if self.is_empty():
                new_node = Node(data)
                self.front = new_node
            else:
                new_node = Node(data, next=self.back)
            self.back = new_node
            self.length +=1


    def dequeue (self):
        if self.is_empty():
            print("No one in line")
        else:
            out = self.front
            self.front = out.next
            self.length -= 1
            return out.data

    def peek(self):
        return f"You'll be waiting for {(self.length*30)/60} minutes if you got in line now \n {self.length} groups ahead of you"


medusa_q = Queue(limit=20)
print(medusa_q.peek())

for i in range(4):
    grp = randint(1,20)
    print(grp)
    if grp <= 12:
        medusa_q.enqueue(grp)
    else:
        medusa_q.enqueue(12)
        medusa_q.enqueue(grp-12)



print(medusa_q.peek())
print("Group size:", medusa_q.dequeue())
print(medusa_q.peek())
