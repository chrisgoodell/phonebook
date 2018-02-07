import os
from time import sleep
import pickle

contactList = []

class Contact(object):
    def __init__(self, first, last, number):
        self.first = first
        self.last = last
        self.number = number
    
    def __repr__(self):
        return "%s %s -- %s" % (self.first, self.last, self.number)

    def fetchFirst(self, first):
        return self.first
    
    def fetchLast(self, last):
        return self.last

    def fetchNumber(self, number):
        return self.number

def sortByLast(contact):
    return contact.fetchLast()

def sortByFirst(contact):
    return contact.fetchFirst()

def sortByNumber(contact):
    return contact.fetchNumber()



# look up contact
def findContact():
    # global contactList
    print "-- Find a contact --"
    print " "
    if len(contactList) == 0:
        print "No contacts stored."
    else:
        firstNameLookup = raw_input("Enter first name: ")
        lastNameLookup = raw_input("Enter last name:  ")
        for contact in contactList:
            first = contact.first() #contact.fetchFirst(firstNameLookup)
            last = contact.last() #contact.fetchLast(lastNameLookup)
            if lastNameLookup == last:
                sleep(1)
                print "\nRecord found! \n", \
                "First Name:   ", contact.first, \
                "\nLast Name:    ", contact.last, \
                "\nPhone Number: ", contact.number, " \n"
                raw_input("Press any key to continue...\n")
                menu()
            else:
                print "Contact not found.\n"
                raw_input("Press any key to continue...\n")
                sleep(1)
                menu()


# add contact
def addContact():
    global contactList
    os.system('clear')
    print "-- Enter a new contact --"
    print " "
    firstname = raw_input("First Name:   ")
    lastname = raw_input("Last Name:    ")
    phone = raw_input("Phone Number: ")
    newContact = Contact(firstname, lastname, phone)
    contactList.append(newContact)
    sleep(1)
    print("\nEntry stored for %s %s\n" % (firstname, lastname))
    return contactList
    sleep(1)


# delete contact
def delContact():
    global contactList
    os.system('clear')
    print "-- Delete a contact --"
    print " "
    update_count = 0
    firstNameLookup = raw_input("Enter first name: ")
    lastNameLookup = raw_input("Enter last name: ")
    for i in contactList:
        first = i.fetchFirst(firstNameLookup)
        last = i.fetchLast(lastNameLookup)
        full = first + last 
        if lastNameLookup == last:
            if raw_input(("Please confirm delete %s %s (y/n)") % (firstNameLookup, lastNameLookup)) == 'y':
                print "Contact deleted for %s %s" % (first, last)
                contactList.pop(contactList.index(i))
                update_count += 1
            else:
                print "Contact retained."
        else:
            if update_count == 0:
                print "Contact not found.\n"               
    return contactList


# list contacts
def listContacts():
    global contactList
    # global choice
    os.system('clear')
    print "-- List contacts --"
    print " "
    choice = ""
    sortedList = []
    if len(contactList) == 0:
        print "No contacts found."
    else:
        for contact in contactList:
            print "First Name:   ", contact.first, "\nLast Name:    ", contact.last, "\nPhone Number: ", contact.number, " \n"
    raw_input("\nPress any key to continue...")


# exit
def quit_program():
    exit()


def menu():
    print ("""Welcome to Phone Book
=====================
1. Look up an entry
2. Add an entry
3. Delete an entry
4. List all entries
5. Quit
 """)
    choice = int(raw_input("What do you want to do (1-5)? "))
    if choice == 1:
        findContact()
        menu()
    elif choice == 2:
        addContact()
        menu()
    elif choice == 3:
        delContact()
        menu()
    elif choice == 4:
        listContacts()
        menu()
    elif choice == 5:
        quit_program()
    else:
        print "\nThat is not a valid option. Please try again.\n"
        sleep(1)
        menu()

os.system('clear')
menu()
