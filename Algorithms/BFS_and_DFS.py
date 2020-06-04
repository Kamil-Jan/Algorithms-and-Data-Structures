import random
import sys
sys.path.insert(1, "..\\DataStructures\\Trees")
from BST import BST
from collections import deque


def create_tree(nodes_number=15, range_start=1, range_end=100):
    tree = BST()
    for _ in range(nodes_number):
        tree.insert(random.randint(range_start, range_end))
    return tree

def BFS(tree):
    queue = deque([tree.root])
    while queue:
        cur_node = queue.popleft()
        if cur_node:
            queue.append(cur_node.left)
            queue.append(cur_node.right)

def DFS(tree):
    stack = deque([tree.root])
    while stack:
        cur_node = stack.pop()
        if cur_node:
            stack.append(cur_node.right)
            stack.append(cur_node.left)

