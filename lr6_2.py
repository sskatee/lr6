class RedBlackNode:
    def __init__(self, key, color='red'):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

def rotate_left_rbt(tree, x):
    y = x.right
    x.right = y.left
    if y.left:
        y.left.parent = x
    y.parent = x.parent
    if not x.parent:
        tree['root'] = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y

def rotate_right_rbt(tree, y):
    x = y.left
    y.left = x.right
    if x.right:
        x.right.parent = y
    x.parent = y.parent
    if not y.parent:
        tree['root'] = x
    elif y == y.parent.right:
        y.parent.right = x
    else:
        y.parent.left = x
    x.right = y
    y.parent = x

def insert_rbt(tree, key):
    new_node = RedBlackNode(key)
    y = None
    x = tree['root']
    while x:
        y = x
        if new_node.key < x.key:
            x = x.left
        else:
            x = x.right
    new_node.parent = y
    if not y:
        tree['root'] = new_node
    elif new_node.key < y.key:
        y.left = new_node
    else:
        y.right = new_node
    insert_fixup(tree, new_node)

def insert_fixup(tree, z):
    while z.parent and z.parent.color == 'red':
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right
            if y and y.color == 'red':
                z.parent.color = 'black'
                y.color = 'black'
                z.parent.parent.color = 'red'
                z = z.parent.parent
            else:
                if z == z.parent.right:
                    z = z.parent
                    rotate_left_rbt(tree, z)
                z.parent.color = 'black'
                z.parent.parent.color = 'red'
                rotate_right_rbt(tree, z.parent.parent)
        else:
            y = z.parent.parent.left
            if y and y.color == 'red':
                z.parent.color = 'black'
                y.color = 'black'
                z.parent.parent.color = 'red'
                z = z.parent.parent
            else:
                if z == z.parent.left:
                    z = z.parent
                    rotate_right_rbt(tree, z)
                z.parent.color = 'black'
                z.parent.parent.color = 'red'
                rotate_left_rbt(tree, z.parent.parent)
    tree['root'].color = 'black'

def print_rbtree(node, indent="", last=True):
    if node:
        print(indent, "-" if last else "-- ", f"{node.key} ({node.color})", sep="")
        indent += "   " if last else "  "
        print_rbtree(node.left, indent, False)
        print_rbtree(node.right, indent, True)


if __name__ == "__main__":
    tree = {'root': None}
    insert_rbt(tree, 10)
    insert_rbt(tree, 18)
    insert_rbt(tree, 7)
    insert_rbt(tree, 15)
    insert_rbt(tree, 16)

    print("КЧД после вставки:")
    print_rbtree(tree['root'])
