class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type          # "operator" or "operand"
        self.left = left          # Reference to left child Node
        self.right = right        # Reference to right child Node
        self.value = value        # Optional value for operand nodes

    def to_dict(self):        
        return {
            "type": self.type,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None,
            "value": self.value
        }