'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-30 19:30:15
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-30 08:45:34
    @Title : Address Book System Testing
'''
import unittest
from CreateContacts import *
from AddressBook import *
class TestArithmeticOperation(unittest.TestCase):
    person = Addressbook()
    # def test_create_contacts(self):        
    #     """ 
    #     Description: 
    #         This function is testing person_input method
    #     Parameter:
    #         It takes self as argument
    #     Return:
    #         returns Nothing
    #     """
    #     obj = CreateContacts()
    #     self.assertEquals(obj.person_input() ,(obj.fname,obj.lname,obj.address,obj.city,obj.state,obj.zip,obj.phone_number,obj.email ))

    def test_add_records(self):
        """ 
        Description: 
            This function is testing add records method of Addressbook Class
        Parameter:
            It takes self as argument
        Return:
            returns Nothing
        """
        #per = CreateContacts('abc','xyz','pqr','kmn','uvw','123','1234567890','mk@gmail.com')
        ab = self.person.add_records('abc','xyz','pqr','kmn','uvw','123','1234567890','mk@gmail.com')
        self.assertEqual(ab[0].fname, 'abc')
        self.assertEqual(ab[0].lname, 'xyz')
        self.assertEqual(ab[0].address, 'pqr')
        self.assertEqual(ab[0].city, 'kmn')
        self.assertEqual(ab[0].state, 'uvw')
        self.assertEqual(ab[0].zip, '123')
        self.assertEqual(ab[0].phone_number, '1234567890')
        self.assertEqual(ab[0].email, 'mk@gmail.com')
        #self.assertListEqual(list(ab[0]),per)

    def test_find_records(self):
        """ 
        Description: 
            This function is testing find records method of Addressbook Class
        Parameter:
            It takes self as argument
        Return:
            returns Nothing
        """
        self.assertTrue(self.person.find_records('abc'))
        
    def test_update_records(self):
        """ 
        Description: 
            This function is testing update records method of Addressbook Class
        Parameter:
            It takes self as argument
        Return:
            returns Nothing
        """
        ab = self.person.update_records('abc','abc','Kadivar','pqr','kmn','uvw','123','1234567890','mk@gmail.com')
        self.assertEqual(ab[0].fname, 'abc')
        self.assertEqual(ab[0].lname, 'Kadivar')
        self.assertEqual(ab[0].address, 'pqr')
        self.assertEqual(ab[0].city, 'kmn')
        self.assertEqual(ab[0].state, 'uvw')
        self.assertEqual(ab[0].zip, '123')
        self.assertEqual(ab[0].phone_number, '1234567890')
        self.assertEqual(ab[0].email, 'mk@gmail.com')
if __name__ == "__main__":
    unittest.main()