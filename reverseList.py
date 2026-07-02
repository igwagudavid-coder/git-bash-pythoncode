def reverseList(arr):
    reverse = []
    source_id = -1
     
    for i in range(0, len(arr)):
        reverse.append(arr[source_id])
        source_id-=1
        i+=1
    return reverse    
name = list(input("Enter list to be reversed"))
print(reverseList(name))
