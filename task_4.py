from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except (KeyError, IndexError):
            print("Enter the argument for the command")
    return inner

class Contact():
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone 
    def __str__(self):
        return f'Contact name: {self.name}, phone: {self.phone}'

class ContactList():
    def __init__(self):
        self.contacts = []    
    def add_contact(self, contact):
        self.contacts.append(contact)
        return (f'{contact} added.')
    def all_contacts(self):
        for i in self.contacts: 
            print(f'{i}')
    def get_phone(self, name):
        result = ''
        for i in self.contacts:
            if i.name == name: 
                result += f'Contact {i.name} phone is {i.phone} \n'
        if result == '': result = 'Phone not found'
        return result
    def change_contact(self, name, phone):
        result = 'Phone not found'
        for i in self.contacts:
            if i.name == name: 
                i.phone = phone
                result = f'Contact updated to {i}'
        return result

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def main():
    contacts = ContactList()
    print("Welcome to the assistant bot!")
    while True:
#        try:
         user_input = input("Enter a command: ")
         command, *args = parse_input(user_input)
#        except Exception as ex:
#            pass
         match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                contact = Contact(args[0], args[1])
                print(contacts.add_contact(contact))
            case "change":                
                print(contacts.change_contact(args[0], args[1]))
            case "phone":
                print(contacts.get_phone(args[0]))
            case "all":
                contacts.all_contacts()
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()

