
#Catching an exception

num_tickets=input("enter the qty: ");

try:
    num_tickets = int(num_tickets);

except ValueError:
    print("try again");

else:
    print("tickets are printing");
