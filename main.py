from classes.AddressBook import AddressBook
from file_loader import load_data, save_data
from handlers import add_birthday, birthdays, parse_input, add_contact, change_contact, show_all, show_birthday, show_phone


def main():
  book = load_data()
  print("Welcome to the assistant bot!")
  while True:
    user_input = input("Enter a command: ")
    command, *args = parse_input(user_input)

    if command in ["close", "exit"]:
      print("Good bye!")
      break

    elif command == "hello":
      print("How can I help you?")
    elif command == "add":
      print(add_contact(args, book))
    elif command == "change":
      print(change_contact(args, book))
    elif command == "phone":
      print(show_phone(args, book))
    elif command == "all":
      print(show_all(book))
    elif command == "add-birthday":
      print(add_birthday(args, book))
    elif command == "show-birthday":
      print(show_birthday(args, book))
    elif command == "birthdays":
      print(birthdays(book))
    else:
      print("Invalid command.")

  save_data(book)


if __name__ == "__main__":
  main()
