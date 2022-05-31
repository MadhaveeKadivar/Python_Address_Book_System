'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-30 19:13:07
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-30 19:13:15
    @Title : Address Book System
'''
# Import 
from AddressBook import *
print("\nWelcome to Address Book System")

records = Addressbook()
print("\n1. Add a new Record\n")
ch = int(input("\nEnter your choice : "))
if ch == 1:
        fname = input("\nEnter your First Name : ")
        lname = input("Enter your Last Name : ")
        address = input("Enter your Address : ")
        city = input("Enter your City Name : ")
        state = input("Enter your State Name : ")
        zip = input("Enter your Zip Code : ")
        phone_number = input("Enter your Phone Number : ")
        email = input("Enter your Email : ")
        records.add_records(fname,lname,address,city,state,zip,phone_number,email) # Calling a method of AddressBook class to add record in address book
        records.print_records() # Calling a method of AddressBook class to display records of address book
else:
    print("Choice is invalid")     