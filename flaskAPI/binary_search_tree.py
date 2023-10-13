class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def _insert_recursive(self, data, node):
        if int(data["id"]) < int(node.data["id"]):
            if node.left is None:
                node.left = Node(data)
            else:
                # Call the same function with defferent args
                self._insert_recursive(data, node.left)
        elif int(data["id"]) > int(node.data["id"]):
            if node.right is None:
                node.right = Node(data)
            else:
                # call the same function with diff args
                self._insert_recursive(data, node.right)
        
        return
        
        

    def insert(self, data):
        # In case where the tree is empty
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)


    # def _search_recursive(self, blog_post_id, node):
    #     if int(node.data["id"]) == blog_post_id:
    #         post = node.data
    #         print("true is returned here: ", post)
    #         return node.data
    #     elif blog_post_id < int(node.data["id"]): 
    #         if node.left:
    #             self._search_recursive(blog_post_id, node.left)
    #         else:
    #             return False
    #     elif blog_post_id > int(node.data["id"]):
    #         if node.right:
    #             self._search_recursive(blog_post_id, node.right)
    #         else:
    #             return False
    #     return post

    def _search_recursive(self, blog_post_id, node):
        if int(node.data["id"]) == blog_post_id:
            post = node.data
            print("true is returned here: ", post)
            return post
        elif blog_post_id < int(node.data["id"]):
            if node.left:
                return self._search_recursive(blog_post_id, node.left)
        elif blog_post_id > int(node.data["id"]):
            if node.right:
                return self._search_recursive(blog_post_id, node.right)


    def search(self, blog_post_id):
        blog_post_id = int(blog_post_id)
        if self.root is None:
            return False
        return self._search_recursive(blog_post_id, self.root)
