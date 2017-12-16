import pickle
import sys, os

UI = '''
A.View Contacts
B.Add New Contact
C.Delete Contact
D.Reset Contact Dictionary
E.Search
Z.Exit
'''

class Contact:
    def __init__(self,firstName=None,lastName=None,email=None,phoneNumber=None):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phoneNumber = phoneNumber

    def __str__(self):
        return "{} {:>10} {:>10} {:>10} {:>10}".format(self.firstName, self.lastName, self.email,self.phoneNumber)

class ContactsInterface(object):
    
    def __init__(self,db):
        self.db = db
        self.contacts = {}
        if os.path.exists(self.db):
            with open(self.db, 'rb') as person_list:
                self.persons = pickle.load(person_list)
        else:
            file_pntr = open(self.db, 'wb')
            pickle.dump({}, file_pntr)
            file_pntr.close()

    def add(self):
        firstName, lastName, email, phoneNumber = self.getdetails()
        if name in self.persons:
            print('The contact already exists')
        else:
            self.persons[name] = Person(firstName,lastName,email,phoneNumber)

    def viewall(self):
        if self.persons:
            print("{} {:>10} {:>10} {:>10} {:>10}".format('firstName','lastName','email','phoneNumber'))
            for person in self.persons.values():
                print(person)
        else:
            print('No contacts in database.')

    def search(self):
        name = input('Enter firstName')
        if name in self.persons:
            print(self.persons[name])
        else:
            print('Contact not found.')
    
    def getContactDetails(self):
        firstName = input('First Name: ')
        lastName = input('Last Name: ')
        email = input('Email: ')
        phoneNumber = input('Phone Number:')
        return firstName, lastName, email, phoneNumber

    def delete(self):
        name = input('Enter the name to delete: ')
        if name in self.persons:
            del self.persons[name]
            print('Deleted the contact.')
        else:
            print('Contact not found in the app')

    def reset(self):
        self.persons = {}
    
    def __del__(self):
        with open(self.db, 'w') as db1:
            pickle.dump(self.persons, db1)

    def __str__(self):
        return UI

    
def main():
    app = ContactsInterface('contact.data')
    choice = ''
    while choice != 'Z':
        print(app)
        choice = input('Choose: ')
        if choice == 'A':
            app.viewall
        elif choice == 'B':
            app.add()
        elif choice == 'C':
            app.delete()
        elif choice == 'D':
            app.reset()
        elif choice == 'E':
            app.search()
        elif choice == 'Z':
            print('Exiting.')
        else:
            print('Invalid choice.')

if __name__ == '__main__':
    main()


