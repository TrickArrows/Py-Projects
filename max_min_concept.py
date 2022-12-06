import random

n = ['a','b','c','d','e','f','g','h','i','j','k','l','m'];
print(n);

loc = random.randint(0, 12);
print(n[loc],"\n");


print([    n[i] for i in range(max(0,loc+1))    ]);
print("\n");

print([    n[i] for i in range(min(12,loc+1))    ]);
print("\n");

print([    n[i] for i in range(max(0,loc-1)  , min(12,loc+1)+1)  ]);
print("\n");
