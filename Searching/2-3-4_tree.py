class Node:
    def __init__(self, key):
        self.val = key
        self.child = [None, None, None, None]
        self.parent = None


class TwoThreeFourTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if len(node.child) == 4:
            if node.parent is None:
                new_root = Node(node.child[1].val)
                new_root.child[0] = node
                node.parent = new_root
                self.root = new_root
                self._split(new_root, node, key)
            else:
                self._split(node.parent, node, key)
        else:
            if node.child[0] is None:
                node.child[0] = Node(key)
                node.child[0].parent = node
            else:
                if key < node.child[0].val:
                    self._insert(node.child[0], key)
                elif key > node.child[0].val and (
                    node.child[1] is None or key < node.child[1].val
                ):
                    self._insert(node.child[1], key)
                elif key > node.child[0].val and (
                    node.child[1] is None or key > node.child[1].val
                ):
                    self._insert(node.child[2], key)

    def _split(self, parent, node, key):
        if parent.child[0] == node:
            parent.child[0] = Node(node.child[0].val)
            parent.child[0].parent = parent
            parent.child[1] = Node(node.child[2].val)
            parent.child[1].parent = parent
            parent.child[0].child[0] = node.child[0]
            parent.child[0].child[1] = node.child[1]
            parent.child[1].child[0] = node.child[2]
            parent.child[1].child[1] = node.child[3]
            if key < parent.val:
                parent.child[0].child[2] = Node(key)
                parent.child[0].child[2].parent = parent.child[0]
            else:
                parent.child[1].child[2] = Node(key)
                parent.child[1].child[2].parent = parent.child[1]
        elif parent.child[1] == node:
            parent.child[1] = Node
