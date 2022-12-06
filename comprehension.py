#for loop
for num in range(1,21):
    print(num, end =', ')
print("\n")

#list [ ]
li = list(range(0,21));     print(li);
print(li[:5]);
print(li[11:]);

#making a copy of list  li[ : ]
li2 = li[:]; print(li2,"\n");


#min, max, sum
ages =[23,55,64,18,27]
del ages[0];  #del function
print(ages);  # [55,64,18,27]


youngest = min(ages)  #minimum value
oldest = max(ages)      #maximum value
print("young: ",youngest, "\noldest: ",oldest)
print("sum:",sum(ages)); #sum

#Using a comprehension
""" sq = [];
        for x in range(1,11):
            square = x**2;
            sq.append(square)  """
sq = [x**2 for x in range(1,11)]
print("squares: ",sq);

#tuples() : You can overwrite an entire tuple, but you can't change the individual elements in a tuple
price = (150,450)
price = (200,400) # only can change entire tuple, can't change individual value like price[0]
print(price);
