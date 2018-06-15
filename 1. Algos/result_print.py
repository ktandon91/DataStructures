
def max_in_subject(arra):
        return max(arra[1:4])

a = [
    ['A', 1,2,3],
    ['B',2,2,2],
    ['C',3,2,2],
    ['D',1,1,1]
]

for result in a:
    result.append(sum(result[1:4]))

b= list(map(lambda k : (k, k+1), [1,3,4]))

print(b)

sorted_a = sorted(a, key= lambda k : k[4] if k[4] else max_in_subject(k))
print(sorted_a)
# #b = lambda k : [[ k[i][4] for i in range(0,3)] ]
# #print(b(a))
# print("BEFORE")
# print(a)
# b = sorted(a, key=lambda k: k[4])
# print("AFTER SORT 1")
# print(b)
#
# b = sorted(b, key = lambda  k: max_in_subject(k))
#
# print("AFTER SORT 2")
# print(b)
#
# b = sorted(b, key = lambda k : k[0])
#
# print("AFTER SORT 3")
# print(b)
# # mylist = [3,6,3,2,4,8,23]
# # sorted(mylist, key=lambda x: x%2==0)