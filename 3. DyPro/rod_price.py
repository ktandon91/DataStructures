"""
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n.
Determine the maximum value obtainable by cutting up the rod and selling the pieces.
For example, if length of the rod is 8 and the values of different pieces are given as following,
then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

"""

list2 = [
        [1,1],
        [2,5],
        [3,8],
        [4,9],
        [5,10],
        [6,17],
        [7,17],
        [8,20]
        ]

# list2 = [
#
#     [1,5],
#     [2,5],
#     [3,7]
# ]


def recursive_cost(length_of_list):
    #Base Case
    if length_of_list == 0 :
        return 0

    cost = list2[length_of_list-1][1] + list2[len(list2)-length_of_list-1][1]

    return max(cost,recursive_cost(length_of_list-1))


length_of_list = len(list2)

print(recursive_cost(length_of_list))