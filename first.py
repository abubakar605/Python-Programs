import math
ans = 0
ch = "y"
while ch == "y":
    c = eval(input("Enter Your Choice: :"))
    if c == 1:
        print("\t\tCalculator")
        no1 = eval(input("Enter no1: :"))
        no2 = eval(input("Enter no2: :"))
        op =  eval(input("Enter choice: :"))  
        if op == 1:
            ans=no1+no2
            print(no1,"+",no2,"=",ans) 
        elif op == 2:
            ans=no1-no2
            print(no1,"-",no2,"=",ans)
        elif op == 3:
            ans=no1/no2
            print(no1,"/",no2,"=",ans)
        elif op == 1:
            ans=no1*no2
            print(no1,"*",no2,"=",ans) 
    elif c == 2:
        print("\t\tArea Of Circle")
        radius = eval(input("Enter The Radius: :"))
        area = math.pow(radius,2.0)*3.142
        print("area = ",area)  
    elif c == 3:
        print("\t\tMarkSheet") 
        sub1 = eval(input("Enter Marks of Subject1: :"))
        sub2 = eval(input("Enter Marks of Subject2: :"))
        sub3 = eval(input("Enter Marks of Subject3: :"))
        sub4 = eval(input("Enter Marks of Subject4: :"))
        sub5 = eval(input("Enter Marks of Subject5: :"))
        add = sub1+sub2+sub3+sub4+sub5
        percentage = (add/500)*100
        print("Total Marks Obtained: :",add)
        print("Percentage: :",percentage)
    elif c == 4:
        print("\t\tAdd or Even")
        number = eval(input("Enter A Number: :"))
        if number%2 == 0:
            print("The",number,"Is Even Number")    
        else:
            print("The",number,"Is Odd Number")
    elif c == 5:
        print("\t\tLeap Year")
        year = eval(input("Enter A Number: :"))
        if year % 4 == 0:
            print(year,"Is Leap Year")
        else:
            print(year,"Is Not Leap Year")            
    ch = input("press y to continue")            
