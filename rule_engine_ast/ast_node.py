# class Node:
#     def __init__(self, type, left=None, right=None):
#         self.type = type
#         self.left = left
#         self.right = right

#     def to_dict(self):
#         return {
#             "type": self.type,
#             "left": self.left,
#             "right": self.right
#         }
#         # In your ast_node.py
class Node:
    def __init__(self, type, left=None, right=None):
        self.type = type
        self.left = left
        self.right = right

    def to_dict(self):
        # Convert the Node to a dictionary that can be serialized to JSON
        return {
            "type": self.type,
            "left": self.left.to_dict() if isinstance(self.left, Node) else self.left,
            "right": self.right.to_dict() if isinstance(self.right, Node) else self.right
        }
