#!/usr/bin/env python
# shebang line

def toseconds(hours, minutes, seconds):
  return hours*3600+minutes*60+seconds

print("\nWelcome to Seconds Converter\n")

cont = "y"
while(cont.lower() == "y"):
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))

    print("\nThat is {} seconds!".format(toseconds(hours, minutes, seconds)))
    print()
    cont = input("Would you like to do another conversion? [y or n] ")

print("\nThank you for using the Seconds Converter, Good bye!\n")