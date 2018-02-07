import os, pickle
from time import sleep

contactList = []

class Contact(object):
    def __init__(self, first, last, number):
        self.first = first
        self.last = last
        self.number = number
    
    def __repr__(self):
        return "%s %s -- %s" % (self.first, self.last, self.number)

    def fetchFirst(self):
        return self.first
    
    def fetchLast(self):
        return self.last

    def fetchNumber(self):
        return self.number

# sort list of contacts by last name
def sortByLast(contact):
    return contact.last


# look up contact
def findContact():
    results = 0    
    os.system('clear')
    print "-- Find a contact --"
    print " "
    firstNameLookup = raw_input("Enter first name: ")
    lastNameLookup = raw_input("Enter last name:  ")
    if len(contactList) == 0:
        print "No contacts stored."
    else:
        for contact in contactList:
            first = contact.fetchFirst() 
            last = contact.fetchLast()
            number = contact.fetchNumber()
            if lastNameLookup == last:
                sleep(1)
                print "\nRecord found! \n", \
                "First Name:   ", first, \
                "\nLast Name:    ", last, \
                "\nPhone Number: ", number, " \n"
                results += 1
        if results == 0:
            sleep(1)
            print "\nContact not found.\n"
        sleep(1)
        raw_input("Press any key to continue...\n")
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
    sortedList = []
    sortedList = sorted(contactList, key = sortByLast)
    # choice = ""
    if len(contactList) == 0:
        print "No contacts found."
    else:
        for contact in sortedList:
            print "First Name:   ", contact.first, "\nLast Name:    ", contact.last, "\nPhone Number: ", contact.number, " \n"
    raw_input("\nPress any key to continue...")

# save entries to file
def saveEntries():
    myfile = open('phonebook.pickle', 'w')
    pickle.dump(contactList, myfile)
    myfile.close()

# load previous entries from file
def restoreEntries():
    global contactList
    try:
        myfile = open('phonebook.pickle', 'r')
        contactList = pickle.load(myfile)
        return contactList
    except:
        pass
    menu()

# exit
def quit_program():
    saveEntries()    
    exit()


def menu():
    print ("""Welcome to Phone Book
=====================
1. Look up an entry
2. Add an entry
3. Delete an entry
4. List all entries
5. Load stored entries
6. Quit
 """)

    choice = int(raw_input("What do you want to do (1-6)? "))

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
        restoreEntries()
    elif choice == 6:
        quit_program()
    else:
        print "\nThat is not a valid option. Please try again.\n"
        sleep(1)
        menu()

os.system('clear')
menu()
