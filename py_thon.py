"""
Age and Basic Calculator
"""
print("Welcome to Calculator".center(50,"_"))

while True :
    calculator_choice = input("Please choose calculator type (Age/Basic). ").strip().upper()
    
    if calculator_choice == "BASIC" :

        def Addition(num1,num2):
            return num1 + num2

        def Subtraction(num1,num2):
            return num1 - num2

        def Multiplication(num1,num2):
            return num1 * num2

        def Division(num1,num2):
            return num1 / num2

        def Modulus(num1,num2):
            return num1 % num2

        def Exponentiation(num1,num2):
            return num1 ** num2

        def Floor_division(num1,num2):
            return num1 // num2

        print("Basic Calculator".center(50,"_"))
        print("Please enter operation's number.")

        operation_list = ["Addition","Subtraction","Multiplication","Division","Modulus","Exponentiation","Floor division"]
        for i,j in enumerate(operation_list,1):
            print(f"({i}){j}")

        operation_choice = input(("=> ").strip())        
        num1 = float(input()) ; num2 = float(input())

        print("-"*10)

        if operation_choice == "1":
            print(f"{num1} + {num2} ={Addition(num1,num2)}")

        elif operation_choice == "2":
            print(f"{num1} - {num2} ={Subtraction(num1,num2)}")

        elif operation_choice == "3":
            print(f"{num1} * {num2} ={Multiplication(num1,num2)}")

        elif operation_choice == "4":
            print(f"{num1} / {num2} ={Division(num1,num2)}")

        elif operation_choice == "5":
            print(f"{num1} % {num2} ={Modulus(num1,num2)}")

        elif operation_choice == "6":
            print(f"{num1} ** {num2} ={Exponentiation(num1,num2)}")

        elif operation_choice == "7":
            print(f"{num1} // {num2} ={Floor_division(num1,num2)}")

        Again = input("Next calculation? (yes/no): ")
        if Again in ["no","NO","n","N"]:
            break

    if calculator_choice == "AGE":
        import datetime
        
        print("Basic Calculator".center(50,"_"))
        try:
            day,month,year = map(int,input("Please enter your birth date (dd/mm/yyyy). ").strip().split("/"))
        except ValueError:
            print(" ")

        my_birthdate = datetime.date(year,month,day)
        current_date = datetime.datetime.now().date()

        months_lived = (current_date.year - my_birthdate.year) * 12
        hours_lived = ((current_date - my_birthdate).days) * 24
        minutes_lived = hours_lived * 60
        seconds_lived = minutes_lived * 60
        
        print("You lived for:")
        print(f"{(current_date.year - my_birthdate.year)} Years.")
        print(f"{months_lived} Months.")        
        print(f"{(current_date - my_birthdate).days} Days.")
        print(f"{minutes_lived} Minutes.")  
        print(f"{seconds_lived} Seconds.")  


        Again = input("Next calculation? (yes/no): ")
        if Again in ["no","NO","n","N"]:
            break

    else:
        print("Wrong Choice!")   
        break 
    



