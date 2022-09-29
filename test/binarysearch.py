array = [i for i in range(300_000_000)]

value = 1
def linearSearch(array,value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return False
            
# array = [1, 5, 7, 8, 9 ,10]   - len() = 6 index of the highest value is 5 

def binarySearch(array , value , lo , hi):
    if hi < lo:
        return -1
    mid = (hi + lo) //2
    if array[mid] == value:
        return mid
    elif array[mid] < value:
        return binarySearch(array,value,mid+1,hi)
    elif array[mid] > value:
        return binarySearch(array,value,lo,mid-1)

def binarySearchWhile(array,value):
    lo , hi = 0 , len(array) -1
    while(lo < hi):
        mid = (hi + lo)//2
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            lo = mid +1
        elif array[mid] > value:
            hi = mid -1
    return -1

print(linearSearch(array,value))
#print(binarySearch(array,value,0,len(array) -1))
#print(binarySearchWhile(array,value))
