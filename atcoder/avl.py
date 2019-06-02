# http://www.geocities.jp/m_hiroi/light/pyalgo03.html

class AVLTree:

    def __init__(self):
        self.root = None

    def search(self, value):
        while node:
            v = node[0]
            if v == value:
                return True
            if value < v:
                node = node[1]
            else:
                node = node[2]
        return False

    def add(self, value):
        v = node[0]
        if node is None:
            node[0] = value
        elif value == v:
            pass
        elif value < v:
            node[1] = avl_add(node[1], value)
        else:
            node[2] = avl_add(node[2], value)
        return node

if __name__ == '__main__':
    root = AVLTree()
    avl.add(1)
    avl.add(2)
    avl.add(3)
    print(root)
