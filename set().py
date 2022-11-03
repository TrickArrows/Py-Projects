sorted_list = set()

#<append> not working
#use <add> function

sorted_list.add("hello");
sorted_list.add("hello");
sorted_list.add("welcome");
sorted_list.add("one");
sorted_list.add("two");
sorted_list.add("three");
sorted_list.add("four");

print(sorted_list,"\n");

#sort and changed to list[]
print("listed and sorted")
print(sorted(list(sorted_list)));
