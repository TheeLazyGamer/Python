                    # This program calculates the users age. 

#******************************************************************************
                  # Imports the date from datetime module.
            # Imports the exit function from the system module

from datetime import date
from sys import exit

#******************************************************************************
              # Creates a string variable containing users name.

yourName = input("Please enter your name: ")

#******************************************************************************
               # Requires user input for birth month (integer)

            # Handles the error occured with invalid data type. 
while True:
    try:
        month = int(input("Please enter your month of birth (mm): "))
        break
    except ValueError:
            print("\n Invalid Input. Please try again.")
            
        
while month < 1 or month > 12:
    print("\n Outside range - Please try again.")
    month = int(input("Please enter your month of birth (mm): "))
    
#******************************************************************************  
               # Requires user input for birth day (integer)
    
            # Handles the error occured with invalid data type. 
while True:
    try:
        day = int(input("Please enter your day of birth (dd): "))
        break
    except ValueError:
            print("\n Invalid Input. Please try again.")
        
while day < 1 or day > 31:
    print("\n Outside range - Please try again.")
    day = int(input("Please enter your day of birth (dd): "))    
while (month == [1, 3, 5, 7, 8, 10, 12] and day < 1):
    print("\n Outside range - Please try again.")
    day = int(input("Please enter your day of birth (dd): "))
while (month == [1, 3, 5, 7, 8, 10, 12] and day > 31):
    print("\n Outside range - Please try again.")
    day = int(input("Please enter your day of birth (dd): "))
while (month == [4, 6, 9, 11] and day < 1):
    print("\n Outside range - Please try again.")
    day = int(input("Please enter your day of birth (dd): "))
while (month == [4, 6, 9, 11] and day > 30):
    print("\n Outside range - Please try again.")
    day = int(input("Please enter your day of birth (dd): "))
while (month == 2 and day < 1):
    print("\n Outside range - Please try again.")
    day = int(input("Please enter your day of birth (dd): "))
while (month == 2 and day > 29):
    print("\n Outside range - Please try again.")
    day = int(input("Please enter your day of birth (dd): "))
    
#******************************************************************************
               # Requires user input for birth year (integer)
    
currentDate = date.today()
currentYear = currentDate.year

            # Handles the error occured with invalid data type. 
while True:
    try:
        year = int(input("Please enter your year of birth (yyyy): "))
        break
    except ValueError:
            print("\n Invalid Input. Please try again.")
            
while year < 0 or year > currentYear:
    print("\n Outside range - Please try again.")
    year = int(input("Please enter your year of birth (yyyy): "))
    
#******************************************************************************
  # Calculates the difference between the current date and users birth date.
    
def calculateAge(born): 
    today = date.today() 
    try:  
        birthday = born.replace(year = today.year) 
        
#******************************************************************************
              # Handles the error occured during a leap year. 
        
    except ValueError:  
        birthday = born.replace(year = today.year, 
                  month = born.month + 1, day = 1)
  
    if birthday > today: 
        return today.year - born.year - 1
    else: 
        return today.year - born.year 
    
#******************************************************************************   
                          # Outputs the results.
    
print("\n")
print("Hello " + yourName + "!")
print("You are ", calculateAge(date(year, month, day)), "years old.")
exit()
