import os
from time import sleep

phone_book = [] #{}


def menu():
    #os.system('clear')
    print ("""Electronic Phone Book
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit
     """)
    choice = int(raw_input("What do you want to do (1-5)? "))
    if choice == 1:
        find_entry()
        menu()
    elif choice == 2:
        set_entry()
        menu()
    elif choice == 3:
        del_entry()
        menu()
    elif choice == 4:
        list_entries()
        menu()
    elif choice == 5:
        quit_program()
    else:
        print """
        That is not a valid option. Please try again.

        """
        sleep(1)
        menu()

def find_entry():
    # os.system('clear')
    print("1. Search by name\n" \
    "2. Search by number")
    search_option = int(raw_input("Do you want to search by name (1) or number (2)?"))
    if search_option == 1:
        name = raw_input("Name: ")
        for i in phone_book:
            if i[name]:
                # print i.keys()
                print i, i[name]
            # if i[name] in phone_book[i]:
        # if name in phone_book[name]:
                print("Found entry for %s: %s" % (i, i[name]))
            else:
                print("Entry not found in phone book.")    
    elif search_option == 2:
        phone = raw_input("Phone number: ")
        if phone in phone_book[phone]:
            print("Found entry for %s: %s" % (name, phone_book[name]))
        else:
            print("Entry not found in phone book.")

def set_entry():
    name = raw_input("Name: ")
    phone = raw_input("Phone Number: ")
    phone_book.append({name:phone})
    print("Entry stored for %s" % (name))
    sleep(1)

def del_entry():
    os.system('clear')
    name = raw_input("Name: ")
    if (name in phone_book):
        del phone_book[name]
        print("Entry deleted for %s" % (name))
    else:
        print("Entry not found in phone book.")

def list_entries():
    os.system('clear')
    for i in phone_book:
        print i, phone_book[i]
    sleep(1)

def quit_program():
    exit()

menu()