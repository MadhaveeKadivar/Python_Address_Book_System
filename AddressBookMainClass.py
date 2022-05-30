'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-30 19:13:07
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-30 19:13:15
    @Title : Address Book System
'''
# Import 
from CreateContacts import *
print("Welcome to Address Book System")

p1 = CreateContacts() # Creating object of CreateContacts Class
p1.person_input() # Calling Method of class
print(p1.fname)