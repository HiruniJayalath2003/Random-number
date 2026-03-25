#01- Interactive calculator menu-Hiruni

print("\n=====CALCULATOR=====")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")
print("======================")

while True :    
    choise= input("\n Choose an option (1-5):")

    if choise=="1":
        num1=int(input("\nEnter first number :"))
        num2=int(input("Enter second number :"))
        Result=num1+num2
        print(f"\n Result :{num1} + {num2} = {Result}")
        

    elif choise=="2":
        num1=int(input("\nEnter first number :"))
        num2=int(input("Enter second number :"))
        Result=num1-num2
        print(f"\n Result :{num1} - {num2} = {Result}")
        

    elif choise=="3":
        num1=int(input("\nEnter first number :"))
        num2=int(input("Enter second number :"))
        Result=num1*num2
        print(f"\n Result :{num1} * {num2} = {Result} ")
           

    elif choise=="4":
        
        num1=int(input("\nEnter first number :"))
        num2=int(input("Enter second number :"))
        if  num2==0:
            print(f"\n Error: Cannot divide by zero !")
        else:    
            Result=num1/num2
            print(f"\n Result :{num1} / {num2} = {Result} ") 
                

    elif choise=="5":
        print(f"\n Thank you for using the calculator. Goodbye !")

    else:
        print("\n Invalid choice !")
        continue    