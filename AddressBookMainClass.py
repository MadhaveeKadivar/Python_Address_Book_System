'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-30 19:13:07
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-01 19:30:20
    @Title : Address Book System
'''
# Import 
from numpy import rec
from AddressBook import *
     
print("\nWelcome to Address Book System")

records = Addressbook()
while True:
    print("\n1.Add a new Record\n2.Update Records\n3.Delete Records\n4.Display By City")
    print("5.Display By State\n6.FileIOOperation\n7.Exit")
    ch = int(input("\nEnter your choice : "))
    if ch == 1:
        ans = input("\nDo you want to add records in new Address Book ? If yes then press 1 : ")
        if (ans == "1"):
            name_of_ab = input("\nEnter name of address book which you want to create : ")
            records.create_addressbook(name_of_ab) # Calling a method to Create a new Address Book 
            num = int(input("\nHow many contacts you want to add in address book : "))
            for i in range(num):
                print(f"\nEnter details for contact {i+1} : \n")
                fname = input("\nEnter your First Name : ")
                lname = input("Enter your Last Name : ")
                address = input("Enter your Address : ")
                city = input("Enter your City Name : ")
                state = input("Enter your State Name : ")
                zip = int(input("Enter your Zip Code : "))
                phone_number = int(input("Enter your Phone Number : "))
                email = input("Enter your Email : ")
                records.add_records(name_of_ab,fname,lname,address,city,state,zip,phone_number,email)
            records.print_records()
        else:
            records.diplay_list_of_addressBook() # Displaying existing address book name
            if (records.temp == 1): # Checking that address book is empty or not
                print("\nPlease Add Address Book First by entering choice 1")
            else:
                name_of_ab = input("\nSelect any one address book from above list : ")
                num = int(input("\nHow many contacts you want to add in address book : "))
                for i in range(num):
                    print(f"\nEnter details for contact {i+1} : \n")
                    fname = input("\nEnter your First Name : ")
                    lname = input("Enter your Last Name : ")
                    address = input("Enter your Address : ")
                    city = input("Enter your City Name : ")
                    state = input("Enter your State Name : ")
                    zip = int(input("Enter your Zip Code : "))
                    phone_number = int(input("Enter your Phone Number : "))
                    email = input("Enter your Email : ")
                    records.add_records(name_of_ab,fname,lname,address,city,state,zip,phone_number,email)
            records.print_records()
    elif ch == 2:
        records.diplay_list_of_addressBook() # Displaying existing address book name
        if (records.temp == 1): # Checking that address book is empty or not
            print("\nPlease Add Address Book First by entering choice 1")
        else:
            name_of_ab = input("\nSelect any one address book from above list : ")
            old_fname = input("\nEnter your First Name : ")
            check = records.find_records(name_of_ab,old_fname)
            if check:
                new_fname = input("\nEnter your new First Name : ")
                lname = input("Enter your new Last Name : ")
                address = input("Enter your new Address : ")
                city = input("Enter your new City Name : ")
                state = input("Enter your new State Name : ")
                zip = input("Enter your new Zip Code : ")
                phone_number = input("Enter your new Phone Number : ")
                email = input("Enter your new Email : ")
                records.update_records(name_of_ab,old_fname,new_fname,lname,address,city,state,zip,phone_number,email)
        records.print_records()
    elif ch == 3 :
        records.diplay_list_of_addressBook() # Displaying existing address book name
        if (records.temp == 1): # Checking that address book is empty or not
            print("\nPlease Add Address Book First by entering choice 1")
        else:
            name_of_ab = input("\nSelect any one address book from above list : ")
            fname = input("\nEnter your First Name : ")
            check = records.find_records(name_of_ab,fname)
            if check:
                records.delete_record(fname)
        records.print_records() 
    elif ch == 4 :
        cname = input("\nEnter city name : ")
        total_records = records.display_persons_by_city(cname)
        print(f"\nTotal records present where city is {cname}  : {total_records}")
    elif ch == 5 :
        sname = input("\nEnter state name : ")
        total_records =records.display_persons_by_state(sname)
        print(f"\nTotal records present where state is {sname} : {total_records}")
    elif ch == 6:
        records.txt_file_write()
        records.txt_file_read()
        records.csv_file_write()
        records.csv_file_read()
        records.json_file_write()
        records.json_file_read()
    elif ch == 7 :
        break
    else:
        print("Choice is invalid")     