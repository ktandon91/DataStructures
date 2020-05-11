# Given a sum, find if it exists in the list.
# Naive solution would be to use for loops that would require n^2 time
# Second solution is to store list elements in dictionary and use them
# seond approach will run in 2n time, and would require extra memory.

arr_l = [10,3,3,-4,-2,1,3,9]
required_sum = 5

dict_arr_l = {}

for i in arr_l:
    dict_arr_l[i]=i


found_sum = 0

for key in dict_arr_l:
    first_number = dict_arr_l[key]
    second_number = required_sum - first_number

    if second_number in dict_arr_l:
        found_sum=1
        print("({},{}) are present and their sum is equal to required sum {}"
              .format(first_number, second_number,required_sum))


if not found_sum:
    print("No pair exists")