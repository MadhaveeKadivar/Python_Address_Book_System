'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-30 19:30:15
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-01 19:30:20
    @Title : Address Book System Testing
'''
from select import select
import unittest
from CreateContacts import *
from AddressBook import *
class TestArithmeticOperation(unittest.TestCase):
    person = Addressbook()
    # def test_create_addressbook(self):
    #     """ 
    #     Description: 
    #         This function is testing create address book method
    #     Parameter:
    #         It takes self as argument
    #     Return:
    #         returns Nothing
    #     """ 
    #     ab_name , dict_ele = self.person.create_addressbook("MyBook")
    #     self.assertEqual(ab_name[0],'MyBook')
    #     self.assertEqual(len(dict_ele),1)
        
    # def test_add_records(self):
    #     """ 
    #     Description: 
    #         This function is testing add records method of Addressbook Class
    #     Parameter:
    #         It takes self as argument
    #     Return:
    #         returns Nothing
    #     """
    #     self.person.create_addressbook("MyBook")
    #     self.person.add_records('MyBook','abc','xyz','pqr','kmn','uvw','123','1234567890','mk@gmail.com')
    #     ab_dict = self.person.add_records('MyBook','abc','xyz','pqr','kmn','uvw','123','1234567890','mk@gmail.com')
    #     self.assertEqual(len(ab_dict['MyBook']),1)

    # def test_find_records(self):
    #     """ 
    #     Description: 
    #         This function is testing find records method of Addressbook Class
    #     Parameter:
    #         It takes self as argument
    #     Return:
    #         returns Nothing
    #     """
    #     self.assertTrue(self.person.find_records('MyBook','abc'))
        
    # def test_update_records(self):
    #     """ 
    #     Description: 
    #         This function is testing update records method of Addressbook Class
    #     Parameter:
    #         It takes self as argument
    #     Return:
    #         returns Nothing
    #     """
    #     ab_dict = self.person.update_records('MyBook','abc','abc','Kadivar','pqr','kmn','uvw','123','1234567890','mk@gmail.com')
    #     self.assertEqual(ab_dict['MyBook'][0].fname, 'abc')
    #     self.assertEqual(len(ab_dict['MyBook']),1)

    # def test_delete_records(self):
    #     """ 
    #     Description: 
    #         This function is testing delete records method of Addressbook Class
    #     Parameter:
    #         It takes self as argument
    #     Return:
    #         returns Nothing
    #     """ 
    #     ab_dict = self.person.delete_record('MyBook','abc')
    #     self.assertEqual(len(ab_dict['MyBook']),0)

    # def test_display_persons_by_city(self):
    #     """ 
    #     Description: 
    #         This function is testing count the records display by city 
    #     Parameter:
    #         It takes self as argument
    #     Return:
    #         returns Nothing
    #     """ 
    #     self.person.create_addressbook("MyBook")
    #     ab_dict = self.person.add_records('MyBook','abc','Kadivar','pqr','kmn','uvw','123','1234567890','mk@gmail.com')
    #     ab_dict = self.person.add_records('MyBook','Madhavee','Kadivar','pqr','kmn','uvw','123','8451238945','mk@gmail.com')
    #     result = self.person.display_persons_by_city('kmn')
    #     self.assertEqual(result,2)

    # def test_display_persons_by_state(self):
    #     """ 
    #     Description: 
    #         This function is testing count the records display by state
    #     Parameter:
    #         It takes self as argument
    #     Return:
    #         returns Nothing
    #     """ 
    #     self.person.create_addressbook("MyBook")
    #     ab_dict = self.person.add_records('MyBook','abc','Kadivar','pqr','kmn','uvw','123','1234567890','mk@gmail.com')
    #     ab_dict = self.person.add_records('MyBook','Madhavee','Kadivar','pqr','kmn','uvw','123','8451238945','mk@gmail.com')
    #     result = self.person.display_persons_by_state('uvw')
    #     self.assertEqual(result,2)

    # def test_add_persons_in_dictionary_by_city_name(self):
    #     """ 
    #     Description: 
    #         This function is testing add_persons_in_dictionary_by_city_name method
    #     Parameter:
    #         It takes self as argument
    #     Return:
    #         returns Nothing
    #     """
    #     self.person.create_addressbook("MyBook")
    #     ab_dict = self.person.add_records('MyBook','abc','Kadivar','pqr','kmn','uvw','123','1234567890','mk@gmail.com')
    #     ab_dict = self.person.add_records('MyBook','Madhavee','Kadivar','pqr','abc','uvw','123','8451238945','mk@gmail.com')
    #     city_dict = self.person.add_persons_in_dictionary_by_city_name()
    #     self.assertEqual(len(city_dict),2)

    # def test_add_persons_in_dictionary_by_state_name(self):
    #     """ 
    #     Description: 
    #         This function is testing add_persons_in_dictionary_by_state_name method
    #     Parameter:
    #         It takes self as argument
    #     Return:
    #         returns Nothing
    #     """
    #     self.person.create_addressbook("MyBook")
    #     ab_dict = self.person.add_records('MyBook','abc','Kadivar','pqr','kmn','uvw','123','1234567890','mk@gmail.com')
    #     ab_dict = self.person.add_records('MyBook','Madhavee','Kadivar','pqr','abc','mno','123','8451238945','mk@gmail.com')
    #     state_dict = self.person.add_persons_in_dictionary_by_city_name()
    #     self.assertEqual(len(state_dict),2)

    # def test_sort_method(self):
    #     """ 
    #     Description: 
    #         This function is testing all sort  method
    #     Parameter:
    #         It takes self as argument
    #     Return:
    #         returns Nothing
    #     """
    #     self.person.create_addressbook("MyBook")
    #     ab_dict = self.person.add_records('MyBook','zbc','Kadivar','pqr','kmn','uvw',321,12345678,'mk@gmail.com')
    #     ab_dict = self.person.add_records('MyBook','madhavee','Kadivar','pqr','abc','mno',123,845123895,'mk@gmail.com')
    #     ab_dict_by_fname = self.person.sort_by_person_name()
    #     ab_dict_by_city = self.person.sort_by_city()
    #     ab_dict_by_state = self.person.sort_by_state()
    #     ab_dict_by_zip = self.person.sort_by_zip()
    #     self.assertEqual(ab_dict_by_fname['MyBook'][0].fname , 'madhavee')
    #     self.assertEqual(ab_dict_by_fname['MyBook'][0].city , 'abc')
    #     self.assertEqual(ab_dict_by_fname['MyBook'][0].state , 'mno')
    #     self.assertEqual(ab_dict_by_fname['MyBook'][0].zip ,123 )

    # def test_txt_file_write(self):
    #     """ 
    #     Description: 
    #         This function is testing that text file write operation is working properly or not 
    #     Parameter:
    #         It takes one self as argument
    #     Return:
    #         returns Nothing
    #     """
    #     self.person.create_addressbook("MyBook")
    #     ab_dict = self.person.add_records('MyBook','zbc','Kadivar','pqr','kmn','uvw',321,12345678,'mk@gmail.com')
    #     self.person.txt_file_write()
    #     with open("txt_test_file.txt") as myfile:
    #         line=myfile.readlines()[5]
    #     self.assertEqual(line,'First Name : zbc\n')

    # def test_csv_file_write(self):
    #     """ 
    #     Description: 
    #         This function is testing that csv file write operation is working properly or not 
    #     Parameter:
    #         It takes one self as argument
    #     Return:
    #         returns Nothing
    #     """
    #     self.person.create_addressbook("book")
    #     ab_dict = self.person.add_records('book','zbc','Kadivar','pqr','kmn','uvw',321,12345678,'mk@gmail.com')
    #     self.person.csv_file_write()
    #     result = self.person.csv_file_read()
    #     self.assertEqual(result,3) # Testing number of rows of csv file

    def test_json_file_write(self):
        """ 
        Description: 
            This function is testing that json file write operation is working properly or not 
        Parameter:
            It takes one self as argument
        Return:
            returns Nothing
        """
        self.person.create_addressbook("book")
        ab_dict = self.person.add_records('book','zbc','Kadivar','pqr','kmn','uvw',321,12345678,'mk@gmail.com')
        self.person.create_addressbook("Mybook")
        ab_dict = self.person.add_records('Mybook','zbc','Kadivar','pqr','kmn','uvw',321,12345678,'mk@gmail.com')
        self.person.json_file_write()
        result = self.person.json_file_read()
        self.assertEqual(result,2) # Testing number of records of json file
        
if __name__ == "__main__":
    unittest.main()