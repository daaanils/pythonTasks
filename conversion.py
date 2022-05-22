#                                                                                 Danilo B. Pelaso Jr.
#                                                                                 BSIT 2-3
#                                                                                 Integrative Programming 
#                                                                                 Mr. Alfred Pagalilawan

# This program will ask the users which they want to convert depend on the 
# available unit of conversion

# using function
def feet():  #converting feet to meter and centimeter

    feet = float(input("Please enter the length in feet that you would want to convert: "))
    meter = feet * 0.9144 # meter to feet formula
    centimeter = feet * 30.48  #cm to meter formula

    print("the length in meter is")
    print(format(meter, '.2f'));  # expressed in 2 decimal places
    print("the length in centimeter is")
    print(format(centimeter, '.2f'));
    contin()  #  to call out the continue function


def inches():  # function that converting inches to cm to m

    inches = float(input("Please Enter the length in inches that you want to convert: "))
    centimeter = inches * 2.54  # inches to cm formula
    meter = inches * 0.0254  # m to cm formula

    print("The length in centimeter is")
    print(format(centimeter, '.2f'));  # expressed in 2 decimal places
    print("The length in meter is")
    print(format(meter, '.2f'));
    contin() #continue function


def yards():  # function that compute yards to meter and feet

    yards = float(input("Please enter the length in yards to convert: "))
    meter = yards * 0.9144 # celsius formula to convert fahrenheit to celsius
    feet = yards * 3   # fahrenheit formala to get the conversion of celsius to fahrenheit

    print("The length in meter is")
    print(format(meter, '.2f',));  # expressed in 2 decimal places
    print("The length in feet is", )
    print(format(feet, '.2f'));
    contin()


# will determine if the user will continue conversation or not
def contin():
    contin = input("Do you want to continue? Please select Y if Yes.")
    while contin == 'Y':  
        return main()
    else:
        print("end of program!")


# if-else statement for the choices of user
def main():  # call out the function
    menu()
    
    choice = (input("Enter your choice: "))

    if choice == "A" or choice == "a":
        feet()
    elif choice == "B" or choice == "b":
        inches()
    elif choice == "C" or choice == "c":
        yards()
    else:
        print("\nInvalid!\n")
        return main()


def menu():
    print("Please pick one of the choices below:\n")
    print("A = Feet")
    print("B = Inches")
    print("C = Yards")


print("         Unit of Conversion")

main()