class LeafNode:
    def __init__(self, value=None):
        self.value = value
        self.split = None
        self.left = None
        self.right = None

class DecisionTree:
    def __init__(self):
        self.root = None
    
    def add_split(self, leaf, signal_name, constant):
        if leaf is None:
            leaf = LeafNode()
            self.root = leaf
        
        leaf.split = (signal_name, constant)
        leaf.left = LeafNode()
        leaf.right = LeafNode()
        
        return [leaf.left, leaf.right]
    
    def set_leaf_value(self, leaf, value):
        leaf.value = value
    
    def evaluate(self, signals):
        current_node = self.root
        
        while current_node.split is not None:
            signal_name, constant = current_node.split
            if signals.get(signal_name) is None:
                return None
            if signals[signal_name] < constant:
                current_node = current_node.left
            else:
                current_node = current_node.right
        
        return current_node.value

# Example Usage
dt = DecisionTree()

# Initial split
leaves = dt.add_split(None, "X1", 3)

# Adding more splits
left_leaf = leaves[0]
right_leaf = leaves[1]
leaves = dt.add_split(left_leaf, "X2", 1)
dt.add_split(right_leaf, "X1", 6)

# Setting leaf values
dt.set_leaf_value(leaves[0], "N")
dt.set_leaf_value(leaves[1], "Y")
dt.set_leaf_value(right_leaf.left, "N")
leaves = dt.add_split(right_leaf.right, "X3", 2)
dt.set_leaf_value(leaves[0], "Y")
dt.set_leaf_value(leaves[1], "N")

# Evaluating the tree
signals = {"X1": 2, "X2": 11, "X3": 1}
print(dt.evaluate(signals))  # Output: "Y"

signals = {"X1": 4, "X3": 1, "X2": 11}
print(dt.evaluate(signals))  # Output: "Y"
