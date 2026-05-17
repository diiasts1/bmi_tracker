import sys
from app.models import User
from app.storage import save_to_json, load_from_json
from app.utils import my_logger, check_number_format, print_ascii_chart, find_bad_bmis


@my_logger
def main():
    # Load past data at start
    database = load_from_json()

    while True:
        print("\n--- FITNESS TRACKER MENU ---")
        print("1. Create New Profile")
        print("2. Enter Today's Weight")
        print("3. Show My Weight Graph (ASCII)")
        print("4. Check Dangerous High BMIs")
        print("5. Close Program")

        user_choice = input("Type a number (1-5): ")

        if user_choice == '1':
            name = input("Enter your name: ")
            try:
                height = float(input("Enter your height (meters, like 1.75): "))
                database[name] = User(name, height)
                save_to_json(database)
                print(f"Success! Profile for {name} is ready.")
            except ValueError:
                print("Error: Please write a correct decimal number for height.")

        elif user_choice == '2':
            name = input("Enter your name: ")
            if name in database:
                weight_text = input("Enter your weight in kg (like 72.5): ")
                if check_number_format(weight_text):
                    database[name].add_new_weight(float(weight_text))
                    save_to_json(database)
                    print("Success! Your weight is saved.")
                else:
                    print("Error: Wrong number format. Use only digits.")
            else:
                print("Error: Name not found in our system.")

        elif user_choice == '3':
            name = input("Enter your name: ")
            if name in database and database[name].history:
                print_ascii_chart(database[name].history)
            else:
                print("Error: No weight records found for this person.")

        elif user_choice == '4':
            name = input("Enter your name: ")
            if name in database:
                high_bmis = find_bad_bmis(database[name].history)
                print(f"Warning! BMIs higher than 25 found: {high_bmis}")
            else:
                print("Error: Name not found.")

        elif user_choice == '5':
            print("Closing the program. Goodbye!")
            sys.exit()
        else:
            print("Wrong option. Please select from 1 to 5.")


if __name__ == "__main__":
    main()