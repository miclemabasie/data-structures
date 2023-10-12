class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def insert_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        if node.next_node == None:
            self.last_node = node
        

    def insert_end(self, data):
        if self.head == None:
            self.insert_beginning(data)
            return
        node = Node(data)
        self.last_node.next_node = node
        self.last_node = node



    def print_linked_list(self):
        if self.head == None:
            return "None"
        output = ""
        node = self.head
        while node:
            output += f"{node.data} ->"
            if node.next_node == None:
                output += "None"
            node = node.next_node

        return output
    
    def to_list(self):
        l = []
        if self.head == None:
            return l

        node = self.head
        while node:
            l.append(node.data)
            node = node.next_node
        return l

    def get_user_by_id(self, user_id):
        user = None
        if self.head == None:
            return user
        node = self.head
        while node:
            if node.data["id"] == int(user_id):
                user = node.data
                return user
            node = node.next_node
        return "No user found"