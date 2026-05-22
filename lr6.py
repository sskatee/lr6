class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    return node.height if node else 0

def update_height(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def rotate_right(z):
    y = z.left
    t3 = y.right

    y.right = z
    z.left = t3

    update_height(z)
    update_height(y)
    return y

def rotate_left(z):
    y = z.right
    t2 = y.left

    y.left = z
    z.right = t2

    update_height(z)
    update_height(y)
    return y

def avl_insert(node, key):
    if not node:
        return AVLNode(key)
    elif key < node.key:
        node.left = avl_insert(node.left, key)
    else:
        node.right = avl_insert(node.right, key)

    update_height(node)
    balance = get_balance(node)

    if balance > 1 and key < node.left.key:
        return rotate_right(node)

    if balance < -1 and key > node.right.key:
        return rotate_left(node)

    if balance > 1 and key > node.left.key:
        node.left = rotate_left(node.left)
        return rotate_right(node)

    if balance < -1 and key < node.right.key:
        node.right = rotate_right(node.right)
        return rotate_left(node)

    return node

def get_min_value(node):
    current = node
    while current.left:
        current = current.left
    return current

def avl_delete(node, key):
    if not node:
        return node

    if key < node.key:
        node.left = avl_delete(node.left, key)
    elif key > node.key:
        node.right = avl_delete(node.right, key)
    else:
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        temp = get_min_value(node.right)
        node.key = temp.key
        node.right = avl_delete(node.right, temp.key)

    update_height(node)
    balance = get_balance(node)

    if balance > 1 and get_balance(node.left) >= 0:
        return rotate_right(node)

    if balance > 1 and get_balance(node.left) < 0:
        node.left = rotate_left(node.left)
        return rotate_right(node)

    if balance < -1 and get_balance(node.right) <= 0:
        return rotate_left(node)

    if balance < -1 and get_balance(node.right) > 0:
        node.right = rotate_right(node.right)
        return rotate_left(node)

    return node

def print_tree(node, level=0, prefix="Root:"):
    if node is not None:
        print(" " * (level * 4) + prefix + f" {node.key}")
        print_tree(node.left, level + 1, prefix="Left:")
        print_tree(node.right, level + 1, prefix="Right:")


if __name__ == "__main__":
    root = None
    root = avl_insert(root, 20)
    root = avl_insert(root, 4)
    root = avl_insert(root, 15)
    root = avl_insert(root, 13)
    root = avl_insert(root, 33)
    root = avl_insert(root, 5)

    print("Вставляем числа:")
    print_tree(root)

    root = avl_delete(root, 15)
    root = avl_delete(root, 33)
    print("Удалим два числа:")
    print_tree(root)