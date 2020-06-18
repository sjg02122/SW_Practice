class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree(object):
    """implement the Binary Search Tree Data Structure

    When a reward is nonzero,
    the game has been reset ("Pong" specific)

    Args:
        object : it contain data value(root) , right leaf, left leaf
        * it implemented by Class Node

    Example:
        array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]
        bst = BinarySearchTree()
        for x in array:
            bst.insert(x)
        # Find
        print(bst.find(15)) # True
        print(bst.find(17)) # False
        # Delete
        print(bst.delete(55)) # True
        print(bst.delete(14)) # True
        print(bst.delete(11)) # False

    reference: https://geonlee.tistory.com/72 [빠리의 택시 운전사]
    """


    def __init__(self):
        self.root = None

    def insert(self,data):
        self.root = self._insert_value(self.root,data)
        return self.root is not None

    def _insert_value(self,node,data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left,data)
            else:
                node.right =self._insert_value(node.right,data)
        return node

    def find(self,key):
        return self._find_value(self.root,key)

    def _find_value(self,root,key):
        if root is None or root.data==key:
            return root is not None
        elif key<root.data:
            return self._find_value(root.letf,key)
        else:
            return self._find_value(root.right,key)

    def delete(self,key):
        self.root,deleted = self._delete_value(self.root,key)
        return deleted

    def _delete_value(self,node,key):

        if node is None:
            return node,False

        deleted = False

        if key == node.data:
            deleted = True
            if node.right and node.left :
                parent , child = node,node.right

                while child.left is not None:
                    parent , child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right :
                node = node.left or node.right
            else:
                node = None
        elif key <node.data:
            node.left,deleted = self._delete_value(node.left,key)
        else:
            node.right,deleted = self._delete_value(node.right,key)

        return node,deleted
