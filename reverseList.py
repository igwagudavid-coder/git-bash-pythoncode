import random
def reverseList(arr):
    reverse = []
    source_id = -1
     
    for i in range(0, len(arr)):
        reverse.append(arr[source_id])
        source_id-=1
        i+=1
    return reverse    
name = []
for i in range(0,1000000):
    new = random.randint(0,100000)
    name.append(new)
print(name)
print(reverseList(name))

