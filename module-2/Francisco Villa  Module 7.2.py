# Francisco Villa       Module 7.2          09/16/2026
# This program will take a persons name and convert it to initials.
# User will input thier first, middle and last name.
# The program will output their first, middle, and last initials.

def fullInitials():                                                             # process to change name to initials
    firstName = str(input("What is your first name?: "))                        # get user first name
    middleName = str(input("What is your middle name?: "))                      # get user middle name
    lastName = str(input("What is your last name?: "))                          # get user last name

    print(f"Your initials are: {firstName[0]}.{middleName[0]}.{lastName[0]}.")  # output user initials

try:
    fullInitials()

except Exception as error:
    print(f"An unexpected error has occured: {error}")