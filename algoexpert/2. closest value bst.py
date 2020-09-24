from bst import BST

bs_tree = BST(8)

bs_tree.insert(5)
bs_tree.insert(12)
bs_tree.insert(10)
bs_tree.insert(14)
bs_tree.insert(3)
bs_tree.insert(7)

root = bs_tree
#initialize closest value to infinity

def closest_value_search(root, target_value):
    closest_value = float('inf')

    if root.value == target_value:
        closest_value = target_value

    else:
        while root is not None:
            if abs(root.value - target_value) < abs(closest_value - root.value):
                closest_value = root.value

            if root.value < target_value:
                root = root.right
            else:
                root = root.left

    return closest_value

print(closest_value_search(root, 1))
