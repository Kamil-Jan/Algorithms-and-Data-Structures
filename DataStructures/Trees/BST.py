import time


class TreeNode:
    """
    A node of Binary Search Tree.
    Attributes: val, left, right
    """
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        string = f"Tree node: val={self.val}"
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


class BST(object):
    """
    A Binary Search Tree.
    Functions: insert, search, find_min, find_max
    Attributes: root
    """
    def __init__(self, root):
        self.root = TreeNode(root)

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
        Inserts a given number into a BST.
        """
        self.__insert(number)

    def __insert(self, number):
        """
        Inserts a given number into a BST.

        Check the root of the tree. If the number
        is greater than the root, we look at the right subtree.
        If less - left. Repeat the operation until the number falls
        into place of the leaf.
        """
        node = self.root
        while True:
            # Check if a number is greater than node.
            if number >= node.val:
                # Check if a node.right is None
                if not node.right:
                    # node.right is a leaf
                    node.right = TreeNode(val=number)
                    break
                node = node.right
            else:
                # Check if a node.left is None
                if not node.left:
                    # node.left is a leaf
                    node.left = TreeNode(val=number)
                    break
                node = node.left

    def display(self):
        """
        Displays a Tree.
        """
        def levelOrderTraversal(node, level):
            if not node:
                return
            try:
                orderTraversal[level].append(node.val)
            except:
                orderTraversal.append([node.val])
            levelOrderTraversal(node.left, level + 1)
            levelOrderTraversal(node.right, level + 1)

        orderTraversal = [[self.root.val]]
        levelOrderTraversal(self.root.left, 1)
        levelOrderTraversal(self.root.right, 1)

        return orderTraversal


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        print(f"Running time: {time.time() - start}")
        return value
    return wrapper

@timer
def main():
    t = BST(0)
    [t.insert(i) for i in range(10)]

if __name__ == "__main__":
    main()

