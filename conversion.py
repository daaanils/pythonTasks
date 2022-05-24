# This program will ask the users which they want to convert depend on the 
# available unit of conversion

# using function
def feet():  #converting feet to meter and centimeter
    try: #this block is will accept the error and change the executed error were the user can understand it.
        feet = float(input("Please enter the length in feet that you would want to convert: "))
        meter = feet * 0.9144 # meter to feet formula
        centimeter = feet * 30.48  #cm to meter formula

        print("the length in meter is")
        print(format(meter, '.2f'));  # expressed in 2 decimal places
        print("the length in centimeter is")
        print(format(centimeter, '.2f'));
        contin()  #  to call out the continue function
    except ValueError: 
        print("Please provide the necessary input!")
    finally:
        print("Thank you for using my software!")


def inches():  # function that converting inches to cm to m
    try: 
        inches = float(input("Please Enter the length in inches that you want to convert: "))
        centimeter = inches * 2.54  # inches to cm formula
        meter = inches * 0.0254  # m to cm formula
    
        print("The length in centimeter is")
        print(format(centimeter, '.2f'));  # expressed in 2 decimal places
        print("The length in meter is")
        print(format(meter, '.2f'));
        contin() #continue function
    except ValueError:
        print("Please provide the necessary input!")
    finally:
        print("Thank you for using my software!")

def yards():  # function that compute yards to meter and feet
    try:
        yards = float(input("Please enter the length in yards to convert: "))
        meter = yards * 0.9144 # celsius formula to convert fahrenheit to celsius
        feet = yards * 3   # fahrenheit formala to get the conversion of celsius to fahrenheit

        print("The length in meter is")
        print(format(meter, '.2f',));  # expressed in 2 decimal places
        print("The length in feet is", )
        print(format(feet, '.2f'));
        contin()
    except ValueError:
        print("Please provide the necessary input!")
    finally:
        print("Thank you for using my software!")


# will determine if the user will continue conversation or not
def contin():
    while True:
        choice = input("Please enter Y if you still want to continue, otherwise select N. ")
        choice = choice.upper()
        if choice == "Y":
            main()
        elif choice == "N":
            break
        else:
            print("END OF PROGRAM")
            print("Thank you for using my software!")
            contin()


# if-else statement for the choices of user
def main():  # call out the function
    menu()
    
    choice = (input("Enter your choice: "))
    choice = choice.upper()

    if choice == "A":
        feet()
    elif choice == "B":
        inches()
    elif choice == "C":
        yards()
    else:
        print("\nInvalid input! Please pick between A-C, only capital letters\n")
        return main()


def menu():
    print("Please pick one of the choices below:\n")
    print("A = Feet")
    print("B = Inches")
    print("C = Yards")


print("         Unit of Conversion")

main()
