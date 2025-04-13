def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b
while True:
    print("/n SIMPLE CALCULATOR")
    print("1.addition")
    print("2. subtraction")
    print("3.multiplication")   
    print("4.divison")
    print("5.exit")
    choice =input("choose operation (1 2 3 4 5):")
    if choice=='5':
        print("exiting bye bye!")
        break
    if choice in('1','2','3','4'):
        try:
            num1=float(input("enter first number:"))
            num2=float(input("enter second number:"))
            if choice == '1':
                print(num1,"+",num2,add(num1,num2))
            elif choice =='2':
                print(num1,"-",num2,add(num1,num2))
            elif choice == '3':
                print(num1,"*",num2,add(num1,num2))
            elif choice == '4':
                print(num1,"/",num2,add(num1,num2))
            else:
                print("Input number not found!")
        except ValueError:
            print("Invalid input")
                
                