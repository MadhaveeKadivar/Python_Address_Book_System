'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-30 19:30:15
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-31 15:13:20
    @Title : Address Book System Testing
'''
from select import select
import unittest
from CreateContacts import *
from AddressBook import *
class TestArithmeticOperation(unittest.TestCase):
    person = Addressbook()
    def test_create_addressbook(self):
        """ 
        Description: 
            This function is testing create address book method
        Parameter:
            It takes self as argument
        Return:
            returns Nothing
        """ 
        ab_name , dict_ele = self.person.create_addressbook("MyBook")
        self.assertEqual(ab_name[0],'MyBook')
        self.assertEqual(len(dict_ele),1)
        
    def test_add_records(self):
        """ 
        Description: 
            This function is testing add records method of Addressbook Class
        Parameter:
            It takes self as argument
        Return:
            returns Nothing
        """
        self.person.create_addressbook("MyBook")
        self.person.add_records('MyBook','abc','xyz','pqr','kmn','uvw','123','1234567890','mk@gmail.com')
        ab_dict = self.person.add_records('MyBook','abc','xyz','pqr','kmn','uvw','123','1234567890','mk@gmail.com')
        self.assertEqual(len(ab_dict['MyBook']),1)

    def test_find_records(self):
        """ 
        Description: 
            This function is testing find records method of Addressbook Class
        Parameter:
            It takes self as argument
        Return:
            returns Nothing
        """
        self.assertTrue(self.person.find_records('MyBook','abc'))
        
    def test_update_records(self):
        """ 
        Description: 
            This function is testing update records method of Addressbook Class
        Parameter:
            It takes self as argument
        Return:
            returns Nothing
        """
        ab_dict = self.person.update_records('MyBook','abc','abc','Kadivar','pqr','kmn','uvw','123','1234567890','mk@gmail.com')
        self.assertEqual(ab_dict['MyBook'][0].fname, 'abc')
        self.assertEqual(len(ab_dict['MyBook']),1)

    def test_delete_records(self):
        """ 
        Description: 
            This function is testing delete records method of Addressbook Class
        Parameter:
            It takes self as argument
        Return:
            returns Nothing
        """ 
        ab_dict = self.person.delete_record('MyBook','abc')
        self.assertEqual(len(ab_dict['MyBook']),0)

if __name__ == "__main__":
    unittest.main()