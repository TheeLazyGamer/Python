        # This program calculates the users age using a calendar. 

#******************************************************************************
            # Imports Tkinter for graphical user interface.     
        # Imports TkCalendar for use of calendar and date entry.            
                # Imports the date from datetime module.

from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from datetime import date

#******************************************************************************
                    # Creates the window, title and size.

top = Tk()
top.title("Age Calculator GUI")
top.geometry("300x300")

#******************************************************************************
        # Creates the calendar in the window and allows for expansion.

cal = Calendar()
cal.pack(fill = "both", expand = True)   

#******************************************************************************
            # Creates buttons underneath the calendar on the sides

selectBtn = Button(top, text = "OK", command =lambda: calculateAge())
selectBtn.pack(side=LEFT, padx=5, pady=5, expand = True)
closeBtn = Button(top, text = "Close", command = top.destroy)
closeBtn.pack(side=RIGHT, padx=5, pady=5, expand = True)

#******************************************************************************
# Calculates the difference between the current date and the users birth date.
                    # Outputs the results in a message box.   

def calculateAge(): 
    dob = cal.selection_get()
    today = date.today()
    if (today.month - dob.month >= 0 and today.day - dob.day >= 0):
        messagebox.showinfo("Age", (today.year - dob.year))
    else:
        messagebox.showinfo("Age", ((today.year - dob.year) - 1))     

top.mainloop()