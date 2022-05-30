'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-30 19:10:07
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-30 19:10:15
    @Title : Address Book System
'''
class CreateContacts:
    def person_input(self): #Creating class method
        """ 
        Description: 
            This function is getting details from user and store it in variables
        Parameter:
            It takes one self argument
        Return:
            returns tuple of all details
        """           
        self.fname = input("Enter your First Name : ")
        self.lname = input("Enter your Last Name : ")
        self.address = input("Enter your Address : ")
        self.city = input("Enter your City Name : ")
        self.state = input("Enter your State Name : ")
        self.zip = int(input("Enter your Zip Code : "))
        self.phone_number = input("Enter your Phone Number : ")
        self.email = input("Enter your Email Address: ")
        return self.fname,self.lname,self.address,self.city,self.state,self.zip,self.phone_number,self.email 