from bst import BST

bs_tree = BST(8)

bs_tree.insert(5)
bs_tree.insert(12)
bs_tree.insert(10)
bs_tree.insert(14)
bs_tree.insert(3)
bs_tree.insert(7)


root = bs_tree



def branch_sum_calculate(node, running_sum_list, running_sum =0):
    if node.left is None and node.right is None:
        running_sum = running_sum + node.value
        return running_sum_list.append(running_sum)
    if node.left is not None:
        branch_sum_calculate(node.left,running_sum_list, running_sum+node.value)
    if node.right is not None:
        branch_sum_calculate(node.right, running_sum_list, running_sum+node.value)

    return running_sum_list

def branch_sum(root):
    if root is None:
        return 0
    else:
        running_sum_list = []
        branch_sum_val = branch_sum_calculate(root, running_sum_list)

    print(branch_sum_val)

branch_sum(root)