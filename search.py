def native_search(l,target):
    for i in range(len(l)):
        if l[i]==target:
            return i,l[i]

    return -1

print(native_search(['abc','123','hello','welcome'],'welcome'));
print(native_search(['abc','123','hello','welcome'],'123'));        
