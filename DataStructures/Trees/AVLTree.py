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

    def __str__(self):
        string = f"Tree node: val={self.val}, height={self.height}"
        return string

    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
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


class AVLTree:
    """
    AVL Tree Data Structure.
    Attributes: root
    Function: insert, search, find_min, find_max
    """
    def __init__(self, root):
        self.root = TreeNode(val=root)

    def search(self, number):
        """
        Searches the number in a Tree.
        Returns: TreeNode
        """
        node = self.root
        while node:
            if number > node.val:
                node = node.right
            elif number == node.val:
                return node
            else:
                node = node.left
        return None

    def find_min(self):
        """
        Finds a minimal number in a Tree.
        Returns: TreeNode
        """
        node = self.root
        while True:
            if not node.left:
                return node
            node = node.left

    def find_max(self):
        """
        Finds a maximum number in a Tree.
        Returns: TreeNode
        """
        node = self.root
        while True:
            if not node.right:
                return node
            node = node.right

    def insert(self, number):
        """
        Inserts a given number into a Tree.
        """
        node = self._insert(number)
        self._inspect_insert(node)

    def _insert(self, number):
        """
        Inserts a given number into a Tree.

        Check the root of the tree. If the number
        is greater than the root, we look at the right subtree.
        If less - left. Repeat the operation until the number falls
        into place of the leaf.
        """
        node = self.root
        while True:
            # Check if a number is greater than node.
            if number == node.val:
                # print(f"{number}: already in a Tree.")
                return
            elif number > node.val:
                # Check if a node.right is None
                if not node.right:
                    # node.right is a leaf
                    node.right = TreeNode(val=number)
                    node.right.parent = node
                    return node
                node = node.right
            else:
                # Check if a node.left is None
                if not node.left:
                    # node.left is a leaf
                    node.left = TreeNode(val=number)
                    node.left.parent = node
                    return node
                node = node.left

    def _inspect_insert(self, node):
        """
        Updates heights after insertion and
        checks imbalanced nodes.
        """
        if not node:
            return
        if abs(self.get_bf(node)) > 1:
            self._balance(node)
            return
        node.height = self.count_height(node)
        self._inspect_insert(node.parent)

    def get_height(self, node):
        """
        Returns node's height
        """
        if not node:
            return 0
        return node.height

    def count_height(self, node):
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

    def get_bf(self, node):
        """
        Counts _balance factor of a given node.
        """
        return self.get_height(node.left) - self.get_height(node.right)

    def _balance(self, node):
        """
        Decides how subtree should be rotated.
        """
        if self.get_bf(node) == 2: # Left-heavy
            if self.get_bf(node.left) == 1:
                self._LL_rotate(node) # Left-Left heavy
            else: # Left-Right heavy
                self._LR_rotate(node)
        elif self.get_bf(node) == -2: # Right-heavy
            if self.get_bf(node.right) == -1: # Right-Right heavy
                self._RR_rotate(node)
            else: # Right-Left heavy
                self._RL_rotate(node)

    def _LL_rotate(self, node):
        """
        Left-Left rotation.

            A       B
          B   ==> C   A
        C
        """
        A = node
        B = A.left
        # Update children
        if A.parent:
            if A.parent.left == A:
                A.parent.left = B
            else:
                A.parent.right = B
        else:
            self.root = B

        if B.right:
            B.right.parent = A

        A.left, B.right = B.right, A

        # Update parents
        B.parent, A.parent = A.parent, B

        A.height = self.count_height(A)
        B.height = self.count_height(B)
        self._inspect_insert(B.parent)

    def _RR_rotate(self, node):
        """
        Right-Right rotation.

        A           B
          B   ==> A   C
            C
        """
        A = node
        B = A.right
        # Update children
        if A.parent:
            if A.parent.left == A:
                A.parent.left = B
            else:
                A.parent.right = B
        else:
            self.root = B

        if B.left:
            B.left.parent = A

        A.right, B.left = B.left, A

        # Update parents
        B.parent, A.parent = A.parent, B

        A.height = self.count_height(A)
        B.height = self.count_height(B)
        self._inspect_insert(B.parent)

    def _LR_rotate(self, node):
        """
        Left-Right rotation.

          A         A       C
        B    ==>  C   ==> B   A
          C     B
        """
        A = node
        B = A.left
        C = B.right
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
        A.left, B.right, C.right, C.left = C.right, C.left, A, B

        # Update parents
        B.parent, A.parent, C.parent = C, C, A.parent

        A.height = self.count_height(A)
        B.height = self.count_height(B)
        C.height = self.count_height(C)

        self._inspect_insert(C.parent)

    def _RL_rotate(self, node):
        """
        Right-Left rotation.

        A        A           C
          B  ==>   C   ==> A   B
        C            B
        """
        A = node
        B = A.right
        C = B.left
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

        A.right, B.left, C.right, C.left = C.left, C.right, B, A

        # Update parents
        B.parent, A.parent, C.parent = C, C, A.parent

        A.height = self.count_height(A)
        B.height = self.count_height(B)
        C.height = self.count_height(C)

        self._inspect_insert(C.parent)


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

def average_time(func=None, *, num_times=3):
    """
    Prints average running time of a function.
    """
    def decorator_repeat(func):
        def wrapper_repeat(*args, **kwargs):
            start = time.time()
            for _ in range(num_times):
                value = func(*args, **kwargs)
            print(f"Average running time: {(time.time() - start) / num_times}")
            return value
        return wrapper_repeat

    if not func:
        return decorator_repeat
    return decorator_repeat(func)

@average_time(num_times=10)
@timer
def main():
    t = AVLTree(random.randint(1, 100_000))
    for i in range(1, 10_000):
        i = random.randint(1, 100_000)
        t.insert(i)


if __name__ == "__main__":
    main()
