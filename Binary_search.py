import random
import time


def native_search(l,target):
    for i in range(len(l)):
        if l[i]==target:
            return i

    return -1

def binary_search(l,target,low=None,high=None):
    if low is None:
        low = 0;
    if high is None:
        high = len(l) - 1;
    if high < low:
        return -1
    
    midpoint = (low+high) // 2;
    
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l,target,low,midpoint - 1)
    else:
        #target > l[midpoint]
        return binary_search(l,target,midpoint+1,high)
    

if __name__ == '__main__':
    
#   l=[2,5,10,12,15];
#   target=12;
#   print(native_search(l,target));
#   print(binary_search(l,target));


    length = 10000

    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))


    start = time.time()
    for target in sorted_list:
        native_search(sorted_list, target)
    end = time.time()
    print("Native Search: ",(end - start)/length, "seconds");

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary Search: ",(end - start)/length, "seconds");
    
