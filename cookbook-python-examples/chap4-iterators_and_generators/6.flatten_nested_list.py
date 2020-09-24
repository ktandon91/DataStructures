items = [1,2,[3,4,[5,6],7],8]

a = []

def flatten_items(items):
   for item in items:
       if type(item) == list:
           flatten_items(item)
       else:
           a.append(item)
   return a


print(flatten_items(items))