class employee:
    def putdata(self):
        self.id=int(input("enter your id:-"))
        self.name=input("enter your name :-")
    def display(self):
        print(self.id)
        print(self.name)
vansh=employee()
vansh.putdata()
gamer=employee()
gamer.putdata()
vansh.display()
