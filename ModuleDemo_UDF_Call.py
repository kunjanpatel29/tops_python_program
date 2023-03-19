import UDF

while True:

    print("*"*50)
    print("1. OddEven")
    print("2. MaxofTwo")
    print("3. MaxofThree")
    print("4. Fibonacci")
    print("5. Prime")
    print("6. Exit")
    print("*"*50)

    choice = int(input("Enter your choice: "))
    print("*"*50)

    if choice == 1:
        n = int(input("Enter a Value: "))
        UDF.oddeven(n)
        print("*"*50)

    elif choice == 2:
        a = int(input("Enter a Value: "))
        b = int(input("Enter a Value: "))
        UDF.maxoftwo(a,b)
        print("*"*50)
        
    elif choice == 3:
        a = int(input("Enter a Value: "))
        b = int(input("Enter a Value: "))
        c = int(input("Enter a Value: "))
        UDF.maxofthree(a,b,c)
        print("*"*50)
    
    elif choice == 4:
        c = int(input("Enter a Value: "))
        UDF.fibonacci(c)
        print("*"*50)
    
    elif choice == 5:
        c = int(input("Enter a Value: "))
        UDF.prime(c)
        print("*"*50)
    
    else:
        print("Good Bye.")
        break        



