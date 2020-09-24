# index 0, children will be at
# left 2*i+1, right 2*i+2
# parent node, floor(i-1)/2

class MinHeap:

    def __init__(self, arr):
        self.heap = self.build_heap(arr)

    def build_heap(self, arr):
        first_parent_idx = (len(arr)-2)//2

        for parent_idx in reversed(range(first_parent_idx)):
            self.sift_down(parent_idx, len(arr)-1)

        return arr

    def sift_down(self,current_idx, end_idx):
        child_one_idx = current_idx*2 + 1

        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx*2+ 2 <= end_idx else -1

            if child_two_idx != -1 and self.head[child_two_idx] < self.heap[child_one_idx]:
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx

            if self.heap[idx_to_swap] < self.heap[current_idx]:
                self.swap(idx_to_swap, current_idx)
                current_idx = idx_to_swap
                child_one_idx = current_idx*2 + 1

            else:
                break

    def sift_up(self, current_idx):
        parent_idx = (current_idx - 1) // 2

        while current_idx > 0 \
                and self.head[current_idx] < self.heap[parent_idx]:
            self.swap(current_idx, parent_idx)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2


    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0,len(self.heap)-1)
        value_to_remove = self.heap.pop()
        self.sift_down(0, len(self.heap)-1)
        return value_to_remove

    def insert(self,value):
        self.heap.append(value)
        self.sift_up(len(self.heap)-1)
        pass

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
























# import math
#
# a = [8,12,23,17,31,30,44,102,18]
#
# def sift_up(a, num=9):
#     a.append(num)
#     # parentNode = math.floor((len(a)-2)/2)
#     parent_node = a[math.floor((a.index(num)-1)/2)]
#     parent_index = a.index(parent_node)
#     while parent_node > num and parent_index > 0:
#         num_index = a.index(num)
#         a[parent_index], a[num_index] = num, parent_node
#         num = parent_node
#         parent_node = a[math.floor((a.index(num)-1)/2)]
#         parent_index = a.index(parent_node)
#
#     return a
#
# print(a)
# print(sift_up(a))

