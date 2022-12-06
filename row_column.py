import random

value = [[None for i in range(5)] for j in range(5)];

point = [[(j,i) for i in range(5)] for j in range(5)];   # j represent row and
                                                                    # i represent column
                                                                    
loc =random.randint(0,5**2 -1 );
print(loc);
row = loc // 5;
col = loc % 5;

print("(row,col) -> ", row,col)

print("value -> ", value [row] [col]);
print("point j & i -> ",point [row] [col]);

print("\nPosition");

for i in [[(j,i) for i in range(5)] for j in range(5)]:
    print(i);
    
print("\nValue");

for i in [[(i+(5*j)) for i in range(5)] for j in range(5)]:
    print(i);
