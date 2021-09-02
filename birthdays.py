import pickle
BIRTHDAY = 'birthdays_list.dat'

def main():
    birthdays = {}
    try:
        birthdays = load_dictionary(birthdays)
    except:
        store_dictionary(birthdays)
    choice = 0
    while choice != 7:
        choice = get_choice()
        if choice == 1:
            lookup(birthdays)
        elif choice == 2:
            birthdays = add_birthday(birthdays)
        elif choice == 3:
            birthdays = change_birthday(birthdays)
        elif choice == 4:
            birthdays = del_birthday(birthdays)
        elif choice == 5:
            store_dictionary(birthdays)
        elif choice == 6:
            view_birthdays(birthdays)


def get_choice():
    try:
        print()
        print('Friends and Their Birthdays')
        print('---------------------------')
        print('1. Look up a birthday')
        print('2. Add a new birthday')
        print('3. Change a birthday')
        print('4. Delete a birthday')
        print('5. Store birthdays')
        print('6. View all birthdays')
        print('7. Quit the program')
        user_choice = int(input('\nEnter your choice: '))
        while user_choice < 1 or user_choice > 7:
            user_choice = int(input('Please enter a valid choice: '))
        return user_choice
    except :
        print('Please enter a valid number')
    


def lookup(dictionary):
    lookup_name = input('\nEnter a name: ')
    print()
    print(dictionary.get(lookup_name, 'Not Found'))

def add_birthday(dictionary):
    name = input('\nEnter a name: ')
    birthday = input('Enter the birthday: ')
    if name not in dictionary:    
        dictionary[name] = birthday
    else:
        print('That entry already exists')
    return dictionary

def change_birthday(dictionary):
    name = input('\nEnter a name: ')
    if name in dictionary:
        birthday = input('Enter the new birthday: ')
        dictionary[name] = birthday
    else:
        print('That name is not found')
    return dictionary

def del_birthday(dictionary):
    name = input('\nEnter a name: ')
    if name in dictionary:
        del dictionary[name]
    else:
        print('That name is not found')
    return dictionary

def store_dictionary(dictionary):
    outfile = open(BIRTHDAY, 'wb')
    pickle.dump(dictionary, outfile)
    outfile.close()
    print('\nBirthdays dictionary stored!')


def load_dictionary(dictionary):
    infile = open(BIRTHDAY, 'rb')
    dictionary = pickle.load(infile)
    infile.close()
    return dictionary

def view_birthdays(dictionary):
    print()
    for key in dictionary:
        print(key, dictionary[key])








main()