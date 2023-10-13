class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None


    def enqueue(self, data):
        if self.head == None:
            self.head = Node(data, Node)
            self.tail = self.head
        else:
            self.tail.next_node = Node(data, None)
            self.tail = self.tail.next_node

        return 

    def dequeue(self):
        if self.head is None:
            return None
        removed = self.head
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None
        return removed
    
    def print_queue(self):
        if self.head is None:
            print("None")
            return
        node = self.head
        queue_string = ""
        while node:
            print(node.data)
            queue_string += f"{node.data} --> "
            node = node.next_node
        queue_string += "None"

        return queue_string

