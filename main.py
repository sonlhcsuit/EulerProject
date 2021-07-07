import random

length = 10
# sample_array: list = [random.randint(0, 100) for _ in range(length)]
sample_array: list = [59, 12, 37, 72, 23, 90, 9, 2, 58, 6]


def quick_sort(array, low, high):
    if low >= high:
        return

    pivot_value = array[high]
    pivot_index = low - 1
    for i in range(low, high - 1):
        if array[i] < pivot_value:
            pivot_index += 1
            array[i], array[pivot_index] = array[pivot_index], array[i]
    pivot_index = pivot_index + 1
    array[pivot_index], array[high] = array[high], array[pivot_index]
    quick_sort(array, low, pivot_index - 1)
    quick_sort(array, pivot_index + 1, high)


# print(sample_array)
#
# quick_sort(sample_array, 0, length - 1)
#
# print(sample_array)


def merge_sort(array, left, right):
    # print(array[left:right])
    if right - left == 0:
        return [array[left]]
    middle = (left + right) // 2

    L = merge_sort(array, middle + 1, right)
    R = merge_sort(array, left, middle)

    merged = []
    size = 0
    while not (len(L) == 0 and len(R) == 0):
        if len(L) == 0:
            merged.append(R[0])
            R.pop(0)
        elif len(R) == 0:
            merged.append(L[0])
            L.pop(0)
        elif L[0] < R[0]:
            merged.append(L[0])
            L.pop(0)
        else:
            merged.append(R[0])
            R.pop(0)
        size += 1

    return merged


# print(sample_array)
#
# t = merge_sort(sample_array, 0, length - 1)
#
# print(t)
# print(len(t))

class Node:
    def __init__(self, value):
        self.value = value
        self.left: Node = None
        self.right: Node = None
        self.h: int = 1


class Tree:
    def __init__(self):
        self.root: Node = None

    def insert(self, root: Node, node: Node) -> Node:

        if root is None:
            return node
        elif node.value < root.value:
            root.left = self.insert(root.left, node)
        else:
            root.right = self.insert(root.right, node)

        root.h = 1 + max(self.height_of(root.left), self.height_of(root.right))
        b = self.balance_value(root)

        # left left
        if b > 1 and node.value < root.left.value:
            return self.rotate_right(root)
        # left right
        elif b > 1 and node.value > root.left.value:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        # right right
        elif b < -1 and node.value > root.right.value:
            return self.rotate_left(root)
        # right left
        elif b < -1 and node.value < root.right.value:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def height_of(self, node: Node):
        if node is None:
            return 0
        return node.h

    def balance_value(self, node: Node):
        return self.height_of(node.left) - self.height_of(node.right)

    def rotate_right(self, root: Node) -> Node:
        z = root

        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.h = 1 + max(self.height_of(z.left), self.height_of(z.right))
        y.h = 1 + max(self.height_of(y.left), self.height_of(y.right))

        return y

    def rotate_left(self, root: Node) -> Node:
        z = root

        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.h = 1 + max(self.height_of(z.left), self.height_of(z.right))
        y.h = 1 + max(self.height_of(y.left), self.height_of(y.right))

        return y

    def find(self, value):
        pass

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.value), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)


myTree = Tree()

root = None

# root = myTree.insert(root, Node(10))
# root = myTree.insert(root, Node(20))
# root = myTree.insert(root, Node(30))
# root = myTree.insert(root, Node(40))
# root = myTree.insert(root, Node(50))
# root = myTree.insert(root, Node(25))
# root = myTree.insert(root, Node(35))
# root = myTree.insert(root, Node(27))
# root = myTree.insert(root, Node(28))
# root = myTree.insert(root, Node(26))

"""The constructed AVL Tree would be
            30
           /  \
         20   40
        /  \     \
       10  25    50"""

# Preorder Traversal
print("Preorder traversal of the",
      "constructed AVL tree is")
myTree.preOrder(root)
print()
