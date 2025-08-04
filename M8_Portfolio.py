#changing step1 to a setter getter method
class ItemToPurchase:   
    def __init__(self, item_name='none', item_description='none', item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

    @property
    def item_name(self):
        return self._item_name
    
    @property
    def item_description(self):
        return self._item_description
    
    @property
    def item_price(self):
        return self._item_price
    
    @property
    def item_quantity(self):
        return self._item_quantity
   
    @property
    def item_total(self):
        return self.item_price * self.item_quantity
    
    @item_name.setter
    def item_name(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Item name must be a string")
        self._item_name = value 
    
    @item_description.setter
    def item_description(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Description must be a string")
        self._item_description = value
    
    @item_price.setter
    def item_price(self, value: float):
        if not isinstance(value, (int, float)):
            raise ValueError("Item price must be a number")
        if value < 0:
            raise ValueError("Item price cannot be negative")
        self._item_price = value
    
    @item_quantity.setter
    def item_quantity(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Item quantity must be an integer")
        if value < 0:
            raise ValueError("Item quantity cannot be negative")
        self._item_quantity = value
    
    @item_total.setter
    def item_total(self, value: float):
        raise AttributeError("item_total is a read-only property")  

    def print_item_cost(self):
        print(f'{self.item_name} on hand {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_total:.2f}')

class ShoppingCart:
    def __init__(self, customer_name = 'none', current_date = "January 1, 2020"):  
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items =[]
#add item to the cart
    def add_item(self, item: ItemToPurchase):
        if not isinstance(item, ItemToPurchase):
            raise ValueError("Item must be an instance of ItemToPurchase")
        # Check if item already exists in the cart
        for existing_item in self.cart_items:
            if existing_item.item_name == item.item_name:
                existing_item.item_quantity += item.item_quantity
                return 
        self.cart_items.append(item)
#item to remove from cart
    def remove_item(self, item_name: str):
        found = any(item.item_name == item_name for item in self.cart_items)
        self.cart_items = [item for item in self.cart_items if item.item_name != item_name]
        if not found:
            print("Item not found in cart. Nothing removed")       
#modify the cart
    def modify_item(self, updated_item: ItemToPurchase):
        for item in self.cart_items:
            if item.item_name == updated_item.item_name:
                if updated_item.item_description:
                    item.item_description = updated_item.item_description
                if updated_item.item_price != 0:
                    item.item_price = updated_item.item_price
                if updated_item.item_quantity != 0:
                    item.item_quantity = updated_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")
# Get the number of items in the cart
    def get_num_items_in_cart(self):
        total = 0
        for item in self.cart_items:
            total += item.item_quantity
        return total
# Get the total cost of the cart
    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            total += item.item_total
        return total
# Print the shopping cart summarydef print_total(self):
    def print_total(self): 
        print(f"{self.customer_name}'s Shopping Cart - { self.current_date}")   
        if not self.cart_items:
            print("Number of Items : 0")
            print("SHOPPING CART IS EMPTY")
            return
        else:
            print(f"Number of Items : {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                print(f"{item.item_name} {item.item_quantity} @ ${item.item_price:.2f} = ${item.item_total:.2f}")
            print(f"Total: ${self.get_cost_of_cart():.2f}")
#part 6 print the description
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")
# Main menu for the shopping cart
    def print_menu(self):
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print("Choose an option:",end="")
    
    def main(self):
        print("\nWelcome to the Shopping Cart System!")
        print("Enter your name and current date to start shopping.")
        self.customer_name = input("Enter your name: ")
        self.current_date = input("Enter the current date (e.g., January 1, 2020): ")
        print(f"\nCustomer name: {self.customer_name}")      
        print(f"\nToday's date: {self.current_date}")

# fixing the prompt to add two items to the cart
        print("\nEnter details for two items to add to your cart")
        for i in range(2):
            print(f"\nItem {i + 1}:")
            name = input(f"Enter the item name for item {i + 1}: ")
            description = input(f"Enter the item description for item {i + 1}: ")
            while True:
                try:
                    price = float(input(f"Enter the item price for item {i + 1}: "))
                    break
                except ValueError:
                    print("Invalid entry. Please enter a number for price.")
            while True:
                try:
                    quantity = int(input(f"Enter the item quantity for item {i + 1}: "))
                    break
                except ValueError:
                    print("Invalid entry. Please enter a whole number for quantity.")
            item = ItemToPurchase(name, description, price, quantity)
            self.add_item(item)

        # Print total cost of the two items
        print("\nTOTAL COST")
        for item in self.cart_items:
            item.print_item_cost()
        print(f"Total: ${self.get_cost_of_cart():.2f}")

        while True:
            self.print_menu()
            choice = input().strip().lower()
            if choice == 'a':
                name = input("Enter the item name: ")
                description = input("Enter the item description: ")
                price = float(input("Enter the item price: "))
                quantity = int(input("Enter the item quantity: "))
                item = ItemToPurchase(name, description, price, quantity)
                self.add_item(item)
            elif choice == 'r':
                name = input("Enter the item name to remove: ")
                self.remove_item(name)
            elif choice == 'c':
                name = input("Enter the item name to modify: ")
                description = input("Enter new description (or leave blank): ")
                price = input("Enter new price (or leave blank): ")
                quantity = input("Enter new quantity (or leave blank): ")

                # Find the item in the cart
                for item in self.cart_items:
                    if item.item_name == name:
                        if description:
                            item.item_description = description
                        if price:
                            try:
                                item.item_price = float(price)
                            except ValueError:
                                print("Invalid price entered. No change made.")
                        if quantity:
                            try:
                                item.item_quantity = int(quantity)
                            except ValueError:
                                print("Invalid quantity entered. No change made.")
                        break
                else:
                    print("Item not found in cart. Nothing modified.")
            elif choice == 'i':
                self.print_descriptions()
            elif choice == 'o':
                self.print_total()
            elif choice == 'q':
                print("Thank you for using the shopping cart!")
                break
            else:
                print("Invalid option. Please try again.")



if __name__ == "__main__":
    cart = ShoppingCart()
    cart.main()