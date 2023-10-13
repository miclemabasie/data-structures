class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.head = None
        

    def push(self, data):
        if self.head == None:
            self.head = Node(data, None)
        else:
            node = Node(data, self.head)
            self.head = node

    def peek(self):
        return self.head


    def remove_from_stack(self):
        if self.head == None:
            return None
        if self.head.next_node:
            returned = self.head
            self.head = self.head.next_node
            return returned
        else:
            return self.head
    
    def print_stack(self):
        if self.head == None:
            print("None")
            return
        print("-----------------")
        node = self.head
        while node:
            print(node.data)
            node = node.next_node
        print("-----------------")
        return 
        
        