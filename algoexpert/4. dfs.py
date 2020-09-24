from bst import BST

bs_tree = BST(8)

bs_tree.insert(5)
bs_tree.insert(12)
bs_tree.insert(10)
bs_tree.insert(14)
bs_tree.insert(3)
bs_tree.insert(7)


root = bs_tree


def dfs(node, dfs_list):
    if node is None:
        return
    dfs_list.append(node.value)
    dfs(node.left, dfs_list)
    dfs(node.right, dfs_list)

    return dfs_list


def dfs_iterative(node, dfs_list=[]):
    if node is None:
        return dfs_list
    visited = []
    visited.append(node)

    while visited:
        node = visited.pop()
        dfs_list.append(node)
        if node.left is not None:
            visited.append(node.left)
        if node.right is not None:
            visited.append(node.right)

    return dfs_list



dfs_value = dfs_iterative(root, dfs_list=[])

for element in dfs_value:
    print(element.value)
