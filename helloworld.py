#phrase = "jaycel is attractive"
#print(phrase.replace("jaycel", "danilo"))   

#phrase = "the ball is round"
#print(len(phrase))

#num = 7
#print(str(num) + " is my favorite number")

#num = -7
#print(abs(num))

#from math import *

#num = 6.6
#print(round(num))
#from math import *

#num = 16
#print(sqrt(num))
#name = input("please enter your name: ")
#age = input("please enter your age: ")
#print("Hello " + name + ", you're " + age +" years old!")

#num1 = int (input("Please enter A number: "))
#num2 = int (input("Please enter Another number: "))

#answer = num1 + num2

#print(answer)

#friends = ["Vince", "Mike", "Jek", "do", "Enan"]
#print(friends[2:])

#color = input("Please enter a color: ")
#plural_noun = input("Please enter a plural noun: ")
#celebrity = input("Please enter a celebrity: ")

#print("\nRoses are "+ color)
#print(plural_noun+" are blue ")
#print("I love "+ celebrity)
 
#def my_function():
  #print ("Hello from a function")

#my_function()\


def main():

  name = input("Please enter your name: ")
  inches = float (input("Please enter your height in inches: "))
  lbs = float(input("Please enter your weight in lbs: "))

  bmi = (lbs / (inches * inches)) * 703

  print("hello ", name)
  print("you're bmi is ", (format(bmi, '.2f')));

  if bmi <= 18.5:
    print("You're underweight!\n")
  elif bmi <= 24.9:
    print("You're in normal weight!\n")
  elif bmi <= 30:
    print("You're Overweight!\n")
  elif bmi <= 50: 
    print("You're Obese!\n")
  else:
    print("Sorry Invalid Input\n")

  Repeat = input("Would you like to run again? Type Y or y to continue: ")
  if Repeat == "Y" | "y":
    print("\nHello again!\n\n")
    main()
  else:
    print("END OF PROGRAM")

main()


    




