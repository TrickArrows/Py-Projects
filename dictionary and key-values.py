
# a simple dictionary
alien = {'name':'eric','age':15};

#adding new key value
alien['color'] = 'green';

print("dictionary");
print(alien);
print("\n");


    #items()
print("items\n");
for x,y in alien.items():
    print(x,y);
print("\n");


    #keys()
print("keys\n");    
for x in alien.keys():
    print(x);
print("\n");


    #values
print("values\n");
for x in alien.values():
    print(x);
print("\n");
