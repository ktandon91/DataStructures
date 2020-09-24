class BST:
    def __init__(self, value):
        self.value= value
        self.right = None
        self.left = None

    # Avg. O(log(n)) and Space O(1)
    # Worst O(n) and Space O(1)
    def insert(self, value):
        current_node = self

        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    current_node=current_node.left

            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:
                    current_node = current_node.right
        return self

    #Avg. O(logn) and space O(1)
    def contains(self, value):
        current_node = self

        while current_node is not None:
            if value == current_node.value:
                return True

            elif value < current_node.value:
                current_node = current_node.left

            else:
                current_node = current_node.left

        return False


    def remove(self, value, parentnode = None):
        current_node = self

        while current_node is not None:
            if value < current_node.value:
                parentnode = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parentnode = current_node
                current_node = current_node.right
            else:
                # both children cases
                if current_node.left is not None and current_node.right is not None:
                    current_node.value = current_node.right.getMinValue()
                    current_node.right.remove(current_node.value, current_node)
                #root node case
                elif parentnode is None:
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                    else:
                        current_node.value = None
                elif parentnode.left == current_node:
                    parentnode.left = current_node.left if current_node.left is not None else current_node.right

                elif parentnode.right == current_node:
                    parentnode.right = current_node.left if current_node.left is not None else current_node.right

                break
        return self

    def getMinValue(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def pre_order(self):
        while self.left is not None or self.right is not None:
            print(self.value)
            self.left.pre_order()
            self.right.pre_order()
        return



    def __str__(self):
        return str(self.value)


# if __name__ == '__main__':
#     a = BST(8)
#     a.insert(5)
#     a.insert(12)
#     a.insert(10)
#     a.insert(14)
#     a.insert(3)
#     a.insert(7)
#     # a.remove(8)
#
#     # print(a.value)
#     # print(a.left)
#     # print(a.right)
#     # a = BST(1)
#     # for i in range(2,11):
#     #     a.insert(i)
#     # for i in range(1,11):
#     #     a.remove(i)
#     # print(a)
#     a.pre_order()