class Node:
    def __init__(self, data=None, next_node=None):
        self.data =data
        self.next_node = next_node


class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def custom_hash(self, key):
        hash_value = 0
        for i in key:
            hash_value += ord(i)
            hash_value = (hash_value * ord(i)) % self.table_size

        return hash_value

    def add_key_value(self, key, value):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:
            # add hash to this location
            self.hash_table[hashed_key] = Node(Data(key, value), None)
        else:
            node = self.hash_table[hashed_key]
            while node.next_node:
                node = node.next_node
            node.next_node = Node(Data(key, value), None)

    def get_value(self, key):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is not None:
            node = self.hash_table[hashed_key]
            if node.next_node is None:
                return node.data.value
            while node.next_node:
                if key == node.data.key:
                    return node.data.value
                node = node.next_node
            if key == node.data.key:
                return node.data.value
        return None

    
    def print_hash_table(self):
        print("{")
        for index, value in enumerate(self.hash_table):
            if value is not None:
                llist_string = ""
                node = value
                if node.next_node:
                    while node.next_node:
                        llist_string += f"{str(node.data.key)} : {str(node.data.value)} --> "
                        node = node.next_node
                    llist_string += f"{str(node.data.key)} : {str(node.data.value)} --> None"

                    print(f"   [{index}] {llist_string}")
                else:
                    # just a single element at that index
                    print(f"   [{index}] {str(value.data.key)} : {str(value.data.value)} --> None")
            else:
                print(f"   [{index}] {str(value)}")
        print("}")

# ht = HashTable(4)         
# ht.add_key_value("hi", "there")
# ht.add_key_value("dog", "there")
# ht.add_key_value("hi", "there")
# ht.add_key_value("tar", "there")
# ht.add_key_value("hi", "there")
# ht.add_key_value("guy", "there")
# ht.add_key_value("tom", "there")

# ht.print_hash_table()