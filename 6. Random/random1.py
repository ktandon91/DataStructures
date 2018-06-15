from copy import deepcopy

def get_variables():
    dic1 = {
        'a':1,
        'b':2,
    }
    return deepcopy(dic1)

a=get_variables()
b=get_variables()
b.update({'c':3})
print(a,b)

# from copy import deepcopy
#
#
# a = False
#
# if a :
#     print("a")
#
# if not a:
#     print("not")


# def function2(a):
#     print(id(a))
#     b=a
#     b.append(3)
#     print(id(a))
#
# a= [1,2]
# print(id(a))
# function2(a)
# print(a)
#



# def function1(a):
#     print(id(a))
#     a = 2
#     print(id(a))
#
#
# a=1
# print(id(a))
# function1(a)
# print(a)
# if a==1:
#     b=123
# print(b)








# a = [1,2,[3,4]]
# b = a[:]
# #b[2][0]=5
# c=deepcopy(a)
# b[2][0]=2
# c[2][0]=5
# print(id(a), id(b))
#
# print(a,b,c)
#
# a=42
# #b=42
# b=a
# print(id(a),id(b))
#
# b=82
#
# print(id(a),id(b))
#
#
# c=[1,2,3,5,6,7]
#
# #d = [1,2,3,4,5,6,7]
# d=c
# print(id(c),id(d))


