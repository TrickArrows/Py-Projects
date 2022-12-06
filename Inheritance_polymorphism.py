class animal:

    def __init__(self,name,colour,status):

        self.name=name;
        self.colour=colour;
        self.status=status;

    #default function in class
    def speed(self):
        return ("fast");
    

class wild(animal):

    def __init__(self,name,colour,status):
        super().__init__(name,colour,status);

    #Polymorphism function is used to change the default
    def speed(self):
        return ("Super Fast");






t=wild('tiger','orange','killer');

print(t.name);
print(t.colour);
print(t.status);
print(t.speed());




