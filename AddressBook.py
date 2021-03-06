'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-30 20:09:07
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-01 19:44:46
    @Title : Address Book System
'''
from CreateContacts import CreateContacts
import csv
import json
import logging

logging.basicConfig(filename = 'file.log',format = '%(asctime)s | %(levelname)s | %(lineno)d: %(message)s')
logger = logging.getLogger("addressbook")
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
log_format = '%(message)s'
console_handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(console_handler)


class Addressbook:
    
    addressbook_name= [] # Creating List having CreateContacts Class Object Datatype
    addressbook_dict = {}
    city_dictionary = {}
    state_dictionary = {}
    def create_addressbook(self,name):
        """ 
        Description: 
            This function is creating address book
        Parameter:
            It takes self and adressbook name as argument
        Return:
            returns list of address book and dictionary
        """
        self.addressbook_name.append(name) # Add address book name which is provided by user  in address book list
        if len(self.addressbook_dict) == 0 : # Checking that dictionary is empty or not
            self.addressbook_dict[name] = [] # creating key value pair where address book name is key and all the redord of address book as value
        else:
            if name in self.addressbook_dict.keys(): # Checking that address book given by user is already present in dictionary or not
                logger.warning("This AddressBook is also present")
            else:
                self.addressbook_dict[name] = [] # creating key value pair where address book name is key and all the redord of address book as value
        return self.addressbook_name , self.addressbook_dict
    
    temp = 0
    def diplay_list_of_addressBook(self):
        """ 
        Description: 
            This function is displaying only list of address book avilable
        Parameter:
            It takes self as argument
        Return:
            returns Nothing
        """
        if len(self.addressbook_name) == 0: # Checking that address book list is empty or not
            logger.warning("\nThere is no address book avilable")
            self.temp = 1
        else:
            for name in self.addressbook_name: # Accessing all the names in address book
                logger.info("\n\nList of existing Address Book Are : ")
                logger.info(name)

                
    def add_records(self,ab_name,fname,lname,address,city,state,zip,phone_number,email):
        """ 
        Description: 
            This function is getting user input and store it in list 
        Parameter:
            It takes self and all the details with book name as argument
        Return:
            returns list of address book
        """
        person = CreateContacts() # Creating a object of CreateContacts Class
        person.fname = fname
        person.lname = lname
        person.address = address
        person.city = city
        person.state = state
        person.zip = zip
        person.phone_number = phone_number
        person.email = email
        for content in self.addressbook_dict.keys() : # Accessing all the address book name of dictionary
            if (content == ab_name): # Checking that address book name provided by user is matching with dictionary address book or not
                if (len(self.addressbook_dict[content]) == 0):
                    self.addressbook_dict[ab_name].append(person) # Adding person record in Address book 
                    logger.info("\nRecord Added successfully in Address Book")
                else:
                    for records in self.addressbook_dict[ab_name]: # Accessing all the record of address book by dictionary key
                        if (records.phone_number != person.phone_number and records.fname != person.fname): # Checking that phone number provided by user is matching with Existing Reord or not
                            self.addressbook_dict[ab_name].append(person) # Adding person record in Address book 
                            logger.info("\nRecord Added successfully in Address Book")
                        else:
                            logger.info(f"\nThis Record is already present in {content} Address Book") 
            else:
                logger.debug(f"\n{content} Address Book not found")
        return self.addressbook_dict
    
    def print_records(self):
        """ 
        Description: 
            This function is logger.infoing address book records
        Parameter:
            It takes self argument
        Return:
            returns none
        """
        logger.info("\n\nRecords Present in Multiple Address Book : ")
        
        for ab_name in self.addressbook_dict.keys(): # Accessing all the address book name of dictionary
            logger.info(f"\n\nAddress Book : "+ab_name)
            i = 1
            for record in self.addressbook_dict[ab_name]: # Accessing all the records of list one by one using foreach loop
                logger.info(f"\n\nRecord - {i}")
                logger.info(f"First Name : {record.fname}")
                logger.info(f"Last Name : {record.lname}")
                logger.info(f"Address : {record.address}")
                logger.info(f"City : {record.city}")
                logger.info(f"State : {record.state}")
                logger.info(f"Email : {record.email}")
                logger.info(f"Zip code : {record.zip}")
                logger.info(f"Phone Number : {record.phone_number}")
                i += 1

    def find_records(self,ab_name,fname):
        """ 
        Description: 
            This function is finding address book records based on first name
        Parameter:
            It takes self and first name as argument
        Return:
            returns True or False
        """
        for content in self.addressbook_dict.keys() : 
            if (content == ab_name):
                for record in self.addressbook_dict[ab_name]:
                    if (record.fname == fname):
                        return True
                    else:
                        logger.info("\nRecord Not Found")
            else:
                logger.info("Address book not found")
        return False
    
    def update_records(self,ab_name,old_fname,new_fname,lname,address,city,state,zip,phone_number,email): 
        """ 
        Description: 
            This function is updating address book records
        Parameter:
            It takes self and first name as argument
        Return:
            returns list of records
        """
        for content in self.addressbook_dict.keys() : # Accessing all the address book name of dictionary
            if (content == ab_name): # Checking that address book name provied by user is matching with dictionary address book or not
                for record in self.addressbook_dict[ab_name]:
                    if (record.fname == old_fname): # Checking that first name provided by user is matching with Existing Reord or not
                        record.fname = new_fname
                        record.lname = lname 
                        record.address = address 
                        record.city = city 
                        record.state = state 
                        record.zip = zip 
                        record.phone_number = phone_number
                        record.email = email
                        logger.info("\nRecord Updated Successfully !!")
                        
        return self.addressbook_dict

    def delete_record(self,ab_name ,fname):  
        """ 
        Description: 
            This function is deleting address book record by first name
        Parameter:
            It takes self first name as argument
        Return:
            returns none
        """
        for content in self.addressbook_dict.keys() : 
            if (content == ab_name):
                for record in self.addressbook_dict[ab_name]:
                    if (record.fname == fname): 
                        self.addressbook_dict[ab_name].remove(record) # Deleting all the details of one user in Address Book
                        logger.info("\nRecord Deleted Successfully")
        return self.addressbook_dict


    def display_persons_by_city(self,city): 
        """ 
        Description: 
            This function is logger.infoing address book records by city name
        Parameter:
            It takes self and city name as argument
        Return:
            returns number of records
        """
        count = 0
        logger.debug(f"\nAll records present in multiple address books where city name \"{city}\" are : ")
        for ab_name in self.addressbook_dict.keys(): # Accessing all the address book name of dictionary
            logger.info(f"\n\nAddress Book : "+ab_name)
            i = 1
            for record in self.addressbook_dict[ab_name]:
                if record.city == city:
                    logger.info(f"\n\nRecord - {i}")
                    logger.info(f"First Name : {record.fname}")
                    logger.info(f"Last Name : {record.lname}")
                    logger.info(f"Address : {record.address}")
                    logger.info(f"City : {record.city}")
                    logger.info(f"State : {record.state}")
                    logger.info(f"Email : {record.email}")
                    logger.info(f"Zip code : {record.zip}")
                    logger.info(f"Phone Number : {record.phone_number}")
                    i += 1
                    count += 1
        return count

    def display_persons_by_state(self,state): 
        """ 
        Description: 
            This function is logger.infoing address book records by state name
        Parameter:
            It takes self and state name as argument
        Return:
            returns number of records
        """
        count = 0
        logger.info(f"\nAll records present in multiple address books where state name \"{state}\" are : ")
        for ab_name in self.addressbook_dict.keys(): # Accessing all the address book name of dictionary
            logger.info(f"\n\nAddress Book : "+ab_name)
            i = 1
            for record in self.addressbook_dict[ab_name]:
                if record.state == state:
                    logger.info(f"\n\nRecord - {i}")
                    logger.info(f"First Name : {record.fname}")
                    logger.info(f"Last Name : {record.lname}")
                    logger.info(f"Address : {record.address}")
                    logger.info(f"City : {record.city}")
                    logger.info(f"State : {record.state}")
                    logger.info(f"Email : {record.email}")
                    logger.info(f"Zip code : {record.zip}")
                    logger.info(f"Phone Number : {record.phone_number}")
                    i += 1
                    count += 1
        return count

    def add_persons_in_dictionary_by_city_name(self):
        """ 
        Description: 
            This function is storing address book records in dictionary by city name
        Parameter:
            It takes self as argument
        Return:
            returns city dictionary
        """
        for ab_name in self.addressbook_dict.keys(): # Accessing all the address book name of dictionary
            for record in self.addressbook_dict[ab_name]:
                if record.city in self.city_dictionary.keys():
                    self.city_dictionary[record.city].append(record)
                else:
                    self.city_dictionary[record.city] = []
                    self.city_dictionary[record.city].append(record)
        return self.city_dictionary

    def add_persons_in_dictionary_by_state_name(self):
        """ 
        Description: 
            This function is storing address book records in dictionary by state name
        Parameter:
            It takes self as argument
        Return:
            returns state dictionary
        """
        for ab_name in self.addressbook_dict.keys(): # Accessing all the address book name of dictionary
            for record in self.addressbook_dict[ab_name]:
                if record.state in self.city_dictionary.keys():
                    self.state_dictionary[record.state].append(record)
                else:
                    self.state_dictionary[record.state] = []
                    self.state_dictionary[record.state].append(record)
        return self.state_dictionary

    def sort_by_person_name(self):
        """ 
        Description: 
            This function is sorting address book records in dictionary by person first name
        Parameter:
            It takes self as argument
        Return:
            returns address book dictionary
        """
        for content in self.addressbook_dict.keys():
            self.addressbook_dict[content] = sorted(self.addressbook_dict[content], key=lambda x: x.fname)
        return self.addressbook_dict
    
    def sort_by_city(self):
        """ 
        Description: 
            This function is sorting address book records in dictionary by city
        Parameter:
            It takes self as argument
        Return:
            returns address book dictionary
        """
        for content in self.addressbook_dict.keys():
            self.addressbook_dict[content] = sorted(self.addressbook_dict[content], key=lambda x: x.city)
        return self.addressbook_dict
    
    def sort_by_state(self):
        """ 
        Description: 
            This function is sorting address book records in dictionary by person first name
        Parameter:
            It takes self as argument
        Return:
            returns address book dictionary
        """
        for content in self.addressbook_dict.keys():
            self.addressbook_dict[content] = sorted(self.addressbook_dict[content], key=lambda x: x.state)
        return self.addressbook_dict

    def sort_by_zip(self):
        """ 
        Description: 
            This function is sorting address book records in dictionary by zip
        Parameter:
            It takes self as argument
        Return:
            returns address book dictionary
        """
        for content in self.addressbook_dict.keys():
            self.addressbook_dict[content] = sorted(self.addressbook_dict[content], key=lambda x: x.zip)
        return self.addressbook_dict

    def txt_file_write(self):
        """ 
        Description: 
            This function is writing all records in txt file 
        Parameter:
            It takes self as argument
        Return:
            returns nothing
        """
        with open('txt_test_file.txt', 'a') as f:
            for ab_name in self.addressbook_dict.keys():
                f.writelines(f"\n\nAddress Book : "+ab_name)
                i = 1
                for record in self.addressbook_dict[ab_name]:
                    f.writelines(f"\n\nRecord - {i}")
                    f.writelines(f"\nFirst Name : {record.fname}")
                    f.writelines(f"\nLast Name : {record.lname}")
                    f.writelines(f"\nAddress : {record.address}")
                    f.writelines(f"\nCity : {record.city}")
                    f.writelines(f"\nState : {record.state}")
                    f.writelines(f"\nEmail : {record.email}")
                    f.writelines(f"\nZip code : {record.zip}")
                    f.writelines(f"\nPhone Number : {record.phone_number}")
                    i += 1
        logger.info("\nRecord added succesfully in text file")

    def txt_file_read(self):
        """ 
        Description: 
            This function is reading all records from txt file and logger.info it on console
        Parameter:
            It takes self as argument
        Return:
            returns nothing
        """
        with open('txt_test_file.txt', 'r') as f:
            result = f.readlines()
            for i in result:
                logger.info(i)
            logger.info(f"\nTotal no. of rows: {len(result)}")
            
    def csv_file_write(self):
        """ 
        Description: 
            This function is writing all records in csv file 
        Parameter:
            It takes self as argument
        Return:
            returns nothing
        """
        with open('csv_test_file.csv', 'a',newline='') as cf:
            header = ['Addressbook','First_Name','Last_Name','Address','City','State','ZipCode','Phone_Number','Email']
            writer = csv.DictWriter(cf, fieldnames = header)
            for ab_name in self.addressbook_dict.keys():
                for record in self.addressbook_dict[ab_name]:
                    writer.writerow({'Addressbook' : ab_name,'First_Name':record.fname,'Last_Name':record.lname,'Address' : record.address,'City':record.city,'State':record.state,'ZipCode':record.zip,'Phone_Number':record.phone_number,'Email':record.email})
            logger.info("\nRecord added succesfully in csv file")
    def csv_file_read(self):
        """ 
        Description: 
            This function is reading all records from csv file and logger.info it on console
        Parameter:
            It takes self as argument
        Return:
            returns nothing
        """
        with open('csv_test_file.csv', 'r') as cf:    
            csvreader = csv.reader(cf) 
            next(csvreader)
            for row in csvreader:
                logger.info(f"\nAddress Book Name : {row[0]}")
                logger.info(f"\nFirst Name : {row[1]}")
                logger.info(f"\nLast Name : {row[2]}")
                logger.info(f"\nAddress : {row[3]}")
                logger.info(f"\nCity : {row[4]}")
                logger.info(f"\nState : {row[5]}")
                logger.info(f"\nZip code : {row[6]}")
                logger.info(f"\nPhone Number : {row[7]}")
                logger.info(f"\nEmail : {row[8]}")
                
            logger.info(f"\nTotal no. of rows: {csvreader.line_num}")
        return csvreader.line_num

    def json_file_write(self):
        """ 
        Description: 
            This function is writing all records in json file
        Parameter:
            It takes self as argument
        Return:
            returns nothing
        """
        list_ele = []  
        with open('json_test_file.json', 'r') as file:   
            list = json.load(file) 
            if len(list) != 0:           
                for record in list:
                    list_ele.append(record)
        with open('json_test_file.json', 'w') as file:              
            for ab_name in self.addressbook_dict.keys():
                for record in self.addressbook_dict[ab_name]:
                    dict_ele = {'Addressbook' : ab_name,'First_Name':record.fname,'Last_Name':record.lname,'Address' : record.address,'City':record.city,'State':record.state,'ZipCode':record.zip,'Phone_Number':record.phone_number,'Email':record.email}
                    list_ele.append(dict_ele)
            obj = json.dumps(list_ele,indent=4)
            file.write(obj)
            logger.info("\nRecord added succesfully in json file")

    def json_file_read(self):
        """ 
        Description: 
            This function is reading all records from json file and logger.infoing in console
        Parameter:
            It takes self as argument
        Return:
            returns nothing
        """
        with open('json_test_file.json', 'r') as file:   
            list = json.load(file)            
            for record in list:
                logger.info(f"\n\nAddress Book Name : {record['Addressbook']}")
                logger.info(f"\nFirst Name : {record['First_Name']}")
                logger.info(f"\nLast Name : {record['Addressbook']}")
                logger.info(f"\nAddress : {record['Address']}")
                logger.info(f"\nCity : {record['City']}")
                logger.info(f"\nState : {record['State']}")
                logger.info(f"\nZip code : {record['ZipCode']}")
                logger.info(f"\nPhone Number : {record['Phone_Number']}")
                logger.info(f"\nEmail : {record['Email']}")
            logger.info(f"\nTotal number of records in json file : {len(list)}")

        return len(list)