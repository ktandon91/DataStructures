#a = [-45, 42,7,5,-4,-3,49,-30, -12, 4,2]
a= [1, 2, 3, 4, 5]
sum = 10

b = sorted(a)
len_a= len(a)
list_subset = []

for i in range(0,len_a):
    for j in range(i+1, len_a):
        sum_in = b[i]
        if sum_in == sum:
            print("subset exists")

        for k in range(j, len_a):
            sum_in = sum_in + b[k]
            if sum == sum_in:
                print("subset exists")

            if sum_in > sum:
                sum_in = sum_in - b[k-1]
                if sum_in == sum:
                     print("subset exists")
                     sum_in = b[i]
                else:
                    sum_in = b[i]
                break