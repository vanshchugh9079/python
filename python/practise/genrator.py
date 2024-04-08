number=int(input("enter a number:-"))
def table(num):
    for i in range(1,11):
        yield num * i
for x in table(number):
    print(x)
