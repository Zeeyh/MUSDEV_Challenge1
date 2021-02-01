# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 10:55:05 2021

@author: Zainab
"""

contacts = []

isRunning = True

while isRunning:
    

    print("\n")
    print("Welcome to your Phone Directory!")
    print(">>>>Press \"1\" to add a new contact<<<<")
    print(">>>>Press \"2\" to edit your contact<<<<")
    print(">>>>Press \"3\" to delete an entry<<<<")
    print(">>>>Press \"4\" for total entries in your phonebook<<<<")
    print(">>>>Press \"5\" to search for a contact<<<<")
    print(">>>>Press \"6\" to Quit<<<<")
    
    entry = input("Please input your selection number!: ") 
    entry
    
    
    if entry == "1":
        person = []
        
        
        name = input("Name: ")
        person.append(name)
        
        phoneNumber = input("Phone Number: ")
        person.append(phoneNumber)
            
        contacts.append(person)
        
        print("\n")
        print("Contact saved successfully!")
        
    elif entry == "3":
       # for idx, val in enumerate(contacts, start=1):
         #   print(idx)
          #  print(val)
          #  print("\n")
        print("All entries in your phonebook >>>>")
        print("Select ID number (1, 2, 3...) to delete>>>>>")
    
        def list_contacts():
            count = 1
            for i in contacts:
                print(count)
                print("Name: ", i[0])
                print("Phone Number: ",  i[1])
        
                count = count+1
            return

        list_contacts()
            
                   
        d = int(input("ID number: "))
        d = d-1
        
        deleted = contacts.pop(d)
        
        print("\n")
        print("Contact successfuly deleted!")
       
        print("\n")
        print("Your updated contact list is >>>>>>")

        list_contacts()
    
    elif entry == "4":
        count = 1
        for x in contacts:
            count = count+1
            
        print("You have ", count, "entries in total")
        
    elif entry == "5":
        search = input("Enter name of contact to search: ")
        
        for i in contacts:
                if search not in person:
                    break;
                    print(name,"\'s", " contact exists in phonebook" )
                else:
                    print("Not found! \n Go back to the main menu to save this contact")
                    
    elif entry == "2":
        print("This Phonebook is a work in progress! Please select another option")
        
    elif entry == "6":
        isRunning = False
                
            
            
        
            