# Nested Function and Nonlocal Keyword

def calculate_average():

    try:
        num1 = int(input("Enter Value of num1 : "))
        num2 = int(input("Enter Value of num2 : "))
        num3 = int(input("Enter Value of num2 : "))
        average_of_variable = 0

        def get_sum():
            nonlocal average_of_variable
            average_of_variable = num1 + num2 + num3
            print("The Sum of Three Number is : ",average_of_variable)

            def get_average():
                average = average_of_variable // 3
                print("The Average of Three Number is : ",average)

            get_average()

        get_sum()

    except ValueError:
        print("Invalid Input")
    
calculate_average()
