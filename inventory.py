#Simple inventory items
products = []

def add_product():
    item = input("Enter the item: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price: "))
    total = quantity * price
    product = {"item": item, "quantity": quantity, "price": price, "total": total}
    products.append(product)

def display_products():
    print("\nProduct Details:")
    for product in products:
        print(f"Item: {product['item']}, Quantity: {product['quantity']}, Price: {product['price']}, Total: {product['total']}")

def update_product():
    item = input("Enter the name of the item to update: ")
    for product in products:
        if product["item"].lower() == item.lower():
            print(f"Current details for {item}: Quantity: {product['quantity']}, Price: {product['price']}")
            new_quantity = int(input("Enter the new quantity: "))
            new_price = float(input("Enter the new price: "))
            product['quantity'] = new_quantity
            product['price'] = new_price
            product['total'] = new_quantity * new_price
            print(f"Product '{item}' updated successfully.")
            break
    else:
        print(f"Product '{item}' not found in the inventory.")

while True:
    print("\n1. Add a new product")
    print("2. Display all products")
    print("3. Update a product")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_product()
    elif choice == '2':
        display_products()
    elif choice == '3':
        update_product()
    elif choice == '4':
        break
    else:
        print("Invalid choice, please try again.")
