from bst import BST

bs_tree = BST(8)

bs_tree.insert(5)
bs_tree.insert(12)
bs_tree.insert(10)
bs_tree.insert(14)
bs_tree.insert(3)
bs_tree.insert(7)

root = bs_tree


def bfs(root, bfs_list=[]):
    if root is None:
        return bfs_list
    node = root
    bfs_list.append(node)
    while bfs_list:
        element = bfs_list.pop(0)
        print(element.value)
        if element.left is not None:
            bfs_list.append(element.left)
        if element.right is not None:
            bfs_list.append(element.right)


bfs(root)