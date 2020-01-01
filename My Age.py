# This program calculates my age. 
#*************************************************************************
# Imports the datetime module.
from datetime import date 
#*************************************************************************
# Creates a string variable containing my name.
myName = "Solomon Keizer"
#*************************************************************************
# Calculates the difference between the current date and my birth date.
def calculateAge(born): 
    today = date.today() 
    try:  
        birthday = born.replace(year = today.year) 
#*************************************************************************
# Handles the error occured during a leap year. 
    except ValueError:  
        birthday = born.replace(year = today.year, 
                  month = born.month + 1, day = 1) 
  
    if birthday > today: 
        return today.year - born.year - 1
    else: 
        return today.year - born.year 
#*************************************************************************        
# Outputs the results. 
print("Hello Github!") 
print("My name is " + myName + ".")
print("I am ", calculateAge(date(1995, 11, 26)), "years old.")
# END ********************************************************************