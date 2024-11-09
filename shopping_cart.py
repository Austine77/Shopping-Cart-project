# Shopping Cart Program - Final Version
# This program allows users to add items with prices, remove items, and compute the total price.
# Additional features: 
# - Item removal functionality.
# - Total price calculation.
# - Error handling for invalid price inputs and menu choices.

def display_menu():
    """Displays the menu options for the shopping cart program."""
    print("\nWelcome to the Shopping Cart Program!")
    print("Instructions: Choose an option by entering the corresponding number and follow the prompts.")
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

def main():
    """Main function to run the shopping cart program."""
    cart = []  # List to store item names
    prices = []  # List to store item prices

    while True:
        display_menu()  # Show menu options
        try:
            choice = int(input("Please enter an action: "))  # Ensure choice is an integer
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue  # Restart the loop for valid input

        if choice == 1:  # Add item
            item = input("What item would you like to add? ")
            while True:
                try:
                    price = float(input(f"What is the price of '{item}'? "))  # Get price input
                    break  # Exit loop if price is valid
                except ValueError:
                    print("Invalid price entered. Please enter a numeric value.")
            
            cart.append(item)  # Add item to the cart
            prices.append(price)  # Add price to the prices list
            print(f"'{item}' has been added to the cart.")

        elif choice == 2:  # View cart
            print("The contents of the shopping cart are:")
            for index, (item, price) in enumerate(zip(cart, prices), start=1):
                print(f"{index}. {item} - ${price:.2f}")  # Display items with prices

        elif choice == 3:  # Remove item
            print("The contents of the shopping cart are:")
            for index, item in enumerate(cart, start=1):
                print(f"{index}. {item}")  # Display items for removal
            try:
                item_number = int(input("Which item would you like to remove? ")) - 1
                
                if 0 <= item_number < len(cart):  # Check if item number is valid
                    removed_item = cart.pop(item_number)  # Remove item from cart
                    prices.pop(item_number)  # Remove corresponding price
                    print(f"Item '{removed_item}' removed.")
                else:
                    print("Sorry, that is not a valid item number.")
            except ValueError:
                print("Invalid input. Please enter a valid item number.")

        elif choice == 4:  # Compute total
            total = sum(prices)  # Calculate total price
            print(f"The total price of the items in the shopping cart is ${total:.2f}")

        elif choice == 5:  # Quit
            confirm = input("Are you sure you want to quit? (yes/no): ").strip().lower()
            if confirm == 'yes':
                print("Thank you. Goodbye.")
                break  # Exit the loop and end program
            else:
                continue  # Go back to the menu if not quitting

        else:
            print("Invalid option, please try again.")  # Handle invalid menu choices

if __name__ == "__main__":
    main()  # Run the main function