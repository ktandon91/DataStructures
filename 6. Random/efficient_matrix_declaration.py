import time
import copy

N = 500
# Declaring columns
M = 400

# using list comprehension
# to initializing matrix
starttime = time.time()
res = [[0 for i in range(M)] for j in range(N)]
print("Took {} seconds".format(time.time()-starttime))

starttime = time.time()
res = [ [0 for i in range(M)]] * N
print("Took {} seconds".format(time.time()-starttime))
# printing result



res = [ [ 0 for i in range(M) ] for j in range(N) ]
#
res[3][1] = 2
#
print(res)