import Calculator_UDF

while True:

    print("*"*50)
    print("1. Addition")
    print("2. Multilplication")
    print("3. Substraction")
    print("4. Division")
    print("5. modulo")
    print("6. Exit")
    print("*"*50)

    choice = int(input("Enter Your Choice: "))
    
    if choice == 1:
        print("Choose Addition Operation")
        n1 = int(input("Enter a First Value: "))
        n2 = int(input("Enter a Second Value: "))
        Calculator_UDF.addition(n1,n2)
        print("*"*50)

    elif choice == 2:
        print("Choose Multiplication Operation")
        n1 = int(input("Enter a First Value: "))
        n2 = int(input("Enter a Second Value: "))
        Calculator_UDF.multiplication(n1,n2)
        print("*"*50)

    elif choice == 3:
        print("Choose Substraction Operation")
        a = int(input("Enter a First Value: "))
        b = int(input("Enter a Second Value: "))
        Calculator_UDF.substraction(a,b)
        print("*"*50)

    elif choice == 4:
        print("Choose Division Operation")
        a = int(input("Enter a First Value: "))
        b = int(input("Enter a Second Value: "))
        Calculator_UDF.division(a,b)
        print("*"*50)

    elif choice == 5:
        print("Choose Modulo Operation")
        a = int(input("Enter a First Value: "))
        b = int(input("Enter a Second Value: "))
        Calculator_UDF.modulo(a,b)
        print("*"*50)

    else:
        print("Good Bye, Thank You For Using Calculator Operation.")
        break
        
    answer = input("Do you want to continue? (yes/no):")
    answer = answer.lower()
    if answer !='yes':
        break
