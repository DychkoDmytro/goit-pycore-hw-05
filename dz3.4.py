contacts = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "This contact doesn't exist."
        except IndexError:
            return "Enter all arguments for the command."
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    return inner

@input_error
def add_contact(args):
    """Add a contact with a name and phone number."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def show_phone(args):
    """Show the phone number of a contact."""
    name = args[0]
    return f"{name}: {contacts[name]}"

@input_error
def show_all_contacts():
    """Show all contacts."""
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items()) if contacts else "No contacts available."

def main():
    while True:
        command = input("Enter a command: ").strip().lower()
        
        if command == "add":
            args = input("Enter the argument for the command: ").strip().split()
            print(add_contact(args))
        elif command == "phone":
            args = input("Enter the argument for the command: ").strip().split()
            print(show_phone(args))
        elif command == "all":
            print(show_all_contacts())
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Please use 'add', 'phone', 'all', or 'exit'.")

if __name__ == "__main__":
    main()