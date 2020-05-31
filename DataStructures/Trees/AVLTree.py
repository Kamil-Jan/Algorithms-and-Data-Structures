import time
import random


class TreeNode:
    """
    A Node of AVLTree.
    Attributes: val, height, left, right, parent
    """
    def __init__(self, val=None):
        self.val = val
        self.left = None   # left child
        self.right = None  # right child
        self.parent = None # parent
        self.height = 1

    def display(self) -> str:
        """
        Returns string representation of a Tree.
        """
        lines, _, _, _ = self._display_aux()
        return '\n'.join(lines)

    def _display_aux(self):
        """
        Returns list of strings, width, height,
        and horizontal coordinate of the root.
        """
        # No child.
        if self.right is None and self.left is None:
            line = f"{self.val}"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = f"{self.val}"
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = f"{self.val}"
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = f"{self.val}"
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def __str__(self):
        string = f"Tree node: val={self.val}, height={self.height}"
        return string


class AVLTree:
    """
    AVL Tree Data Structure.
    Attributes: root
    Function: insert, delete, search,
              find_min, find_max,
              successor, predecessor
    """
    def __init__(self, root=None):
        if root:
            self.root = TreeNode(val=root)
        else:
            self.root = None

    def search(self, key: int, possible_parent=False) -> TreeNode:
        """
        Searches the key in a Tree.
        Returns: TreeNode
        """
        node = prev_node = self.root
        while node:
            if key > node.val:
                prev_node = node
                node = node.right
            elif key == node.val:
                return node
            else:
                prev_node = node
                node = node.left
        if possible_parent:
            return prev_node
        return None

    def find_min(self) -> TreeNode:
        """
        Finds a minimal key in a Tree.
        Returns: TreeNode
        """
        node = self.root
        while True:
            if not node.left:
                return node
            node = node.left

    def find_max(self) -> TreeNode:
        """
        Finds a maximum key in a Tree.
        Returns: TreeNode
        """
        node = self.root
        while True:
            if not node.right:
                return node
            node = node.right

    def successor(self, key: int) -> TreeNode:
        """
        Returns node with next-larger value of a given 'key'.
        """
        tree_node = self.search(key, possible_parent=True)
        if tree_node:
            if tree_node.right and tree_node.val <= key:
                right_subtree = tree_node.right
                while right_subtree.left:
                    right_subtree = right_subtree.left
                return right_subtree
            else:
                while tree_node:
                    if tree_node.val > key:
                        return tree_node
                    tree_node = tree_node.parent
                return

    def predecessor(self, key: int) -> TreeNode:
        """
        Returns node with next-smaller value of a given 'key'.
        """
        tree_node = self.search(key, possible_parent=True)
        if tree_node:
            if tree_node.left and tree_node.val >= key:
                left_subtree = tree_node.left
                while left_subtree.right:
                    left_subtree = left_subtree.right
                return left_subtree
            else:
                while tree_node:
                    if tree_node.val < key:
                        return tree_node
                    tree_node = tree_node.parent
                return

    def insert(self, key: int) -> None:
        """
        Inserts a given key into a Tree.
        """
        if not self.root:
            self.root = TreeNode(val=key)
            return
        node = self._insert(key)
        self._inspect_changes(node)

    def _insert(self, key: int) -> TreeNode:
        """
        Helper function for insertion.
        """
        node = self.root
        while True:
            # Check if a key is greater than node.
            if key == node.val:
                # print(f"{key}: already in a Tree.")
                return
            elif key > node.val:
                if not node.right:
                    # node.right is a leaf
                    node.right = TreeNode(val=key)
                    node.right.parent = node
                    return node
                node = node.right
            else:
                if not node.left:
                    # node.left is a leaf
                    node.left = TreeNode(val=key)
                    node.left.parent = node
                    return node
                node = node.left

    def delete(self, key: int) -> None:
        """
        Deletes a node with 'key' value from a Tree.
        """
        node = self.search(key)
        if node:
            self._delete(node)

    def _delete(self, node: TreeNode) -> None:
        """
        Helper function for deletion.
        """
        if node.height == 1: # node has no children
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
            else:
                self.root = None
            new_node = node.parent
            node = None
        elif node.left == None: # node has only right child
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
            else:
                self.root = node.right
            node.right.parent = node.parent
            new_node = node.parent
            node = None
        elif node.right == None: # node has only left child
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
            else:
                self.root = node.left
            node.left.parent = node.parent
            new_node = node.parent
            node = None
        else: # node has 2 children
            next_larger = self.successor(node.val)
            node.val = next_larger.val
            return self._delete(next_larger)
        self._inspect_changes(new_node)

    def _inspect_changes(self, node: TreeNode) -> None:
        """
        Updates heights and checks imbalanced nodes.
        """
        if not node:
            return
        if abs(self.get_bf(node)) > 1:
            self._balance(node)
            return
        new_height = self.count_height(node)
        if new_height != node.height:
            node.height = new_height
            self._inspect_changes(node.parent)

    def get_height(self, node: TreeNode) -> int:
        """
        Returns node's height
        """
        if not node:
            return 0
        return node.height

    def count_height(self, node: TreeNode) -> int:
        """
        Counts height of a given node.
        """
        if node.left == None or node.right == None:
            if node.left == node.right:
                return 1
            if node.left and not node.right:
                return node.left.height + 1
            if not node.left and node.right:
                return node.right.height + 1
        return max(node.left.height, node.right.height) + 1

    def get_bf(self, node: TreeNode) -> int:
        """
        Counts balance factor of a given node.
        """
        return self.get_height(node.left) - self.get_height(node.right)

    def _balance(self, node: TreeNode) -> None:
        """
        Decides how subtree should be rotated.
        """
        if self.get_bf(node) == 2: # Left-heavy
            if self.get_bf(node.left) >= 0:
                self._LL_rotate(node) # Left-Left heavy
            else: # Left-Right heavy
                self._LR_rotate(node)
        elif self.get_bf(node) == -2: # Right-heavy
            if self.get_bf(node.right) <= 0: # Right-Right heavy
                self._RR_rotate(node)
            else: # Right-Left heavy
                self._RL_rotate(node)

    def _LL_rotate(self, node: TreeNode) -> None:
        """
        Left-Left rotation.

            A       B
          B   ==> C   A
        C
        """
        A = node
        B = A.left
        # Update parents
        if A.parent:
            if A.parent.left == A:
                A.parent.left = B
            else:
                A.parent.right = B
        else:
            self.root = B

        if B.right:
            B.right.parent = A
        B.parent, A.parent = A.parent, B

        # Rotation
        A.left, B.right = B.right, A

        A.height = self.count_height(A)
        B.height = self.count_height(B)
        self._inspect_changes(B.parent)

    def _RR_rotate(self, node: TreeNode) -> None:
        """
        Right-Right rotation.

        A           B
          B   ==> A   C
            C
        """
        A = node
        B = A.right
        # Update parents
        if A.parent:
            if A.parent.left == A:
                A.parent.left = B
            else:
                A.parent.right = B
        else:
            self.root = B

        if B.left:
            B.left.parent = A
        B.parent, A.parent = A.parent, B

        # Rotation
        A.right, B.left = B.left, A

        A.height = self.count_height(A)
        B.height = self.count_height(B)
        self._inspect_changes(B.parent)

    def _LR_rotate(self, node: TreeNode) -> None:
        """
        Left-Right rotation.

          A        C
        B    ==> B   A
          C
        """
        A = node
        B = A.left
        C = B.right
        # Update parents
        if A.parent:
            if A.parent.left == A:
                A.parent.left = C
            else:
                A.parent.right = C
        else:
            self.root = C

        if C.right:
            C.right.parent = A
        if C.left:
            C.left.parent = B
        B.parent, A.parent, C.parent = C, C, A.parent

        # Rotation
        A.left, B.right, C.right, C.left = C.right, C.left, A, B

        A.height = self.count_height(A)
        B.height = self.count_height(B)
        C.height = self.count_height(C)

        self._inspect_changes(C.parent)

    def _RL_rotate(self, node: TreeNode) -> None:
        """
        Right-Left rotation.

        A          C
          B  ==> A   B
        C
        """
        A = node
        B = A.right
        C = B.left
        # Update parents
        if A.parent:
            if A.parent.left == A:
                A.parent.left = C
            else:
                A.parent.right = C
        else:
            self.root = C

        if C.right:
            C.right.parent = B
        if C.left:
            C.left.parent = A
        B.parent, A.parent, C.parent = C, C, A.parent

        # Rotation
        A.right, B.left, C.right, C.left = C.left, C.right, B, A

        A.height = self.count_height(A)
        B.height = self.count_height(B)
        C.height = self.count_height(C)

        self._inspect_changes(C.parent)

    def __str__(self):
        return self.root.display()


def timer(func):
    """
    Print running time of a function.
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        print(f"Running time: {time.time() - start}")
        return value
    return wrapper

@timer
def main():
    keys = list(range(1, 10_000))
    random.shuffle(keys)

    t = AVLTree()
    # insertion
    for num in keys:
        t.insert(num)
    print(t.find_max())
    print(t.find_min())

    number = random.randint(1, 10_000)
    # searching
    print(t.search(number))
    # successor / predecessor
    print(t.successor(number))
    print(t.predecessor(number))

    random.shuffle(keys)
    # deletion
    for num in keys:
        t.delete(num)
    print(t.root) # None

if __name__ == "__main__":
    main()
