
l = [1,3,5,-3,2,-1,4]
#l = [-3, 2, 3, 1, 6]
sum = 0
d = {}

for i in l:
    sum = i + sum
    if sum in d.keys():
        print("Subset exists")
    else:
        d[sum]=sum
        sum = sum + i

if 0 in d.keys():
    print("subset exists")
else :
    print("Subset doesn't exist")

# l = [3, 34, 4, 12, 5, 2]
# sum = 9
# sort_l = sorted(l)
# # sort_l = [2,3,4,5,12,34]
# sum_find = ''
# for idx, i in enumerate(sort_l):
#     if i == 0:
#         print("subset exists")
#         break
#     for j in sort_l[idx:]:
#         if i+j == sum:
#             pass
#         else