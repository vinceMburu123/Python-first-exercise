"#Simple inventory of items"



products = []

while True:
    print("\n1. Add a new product")
    print("2. Display all products")
    print("3. Update a product")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        item = input("Enter the item: ")
        quantity = int(input("Enter the quantity: "))
        price = float(input("Enter the price: "))
        
        total = quantity * price
        
        product = {
            "item": item,
            "quantity": quantity,
            "price": price,
            "total": total
        }
        
        products.append(product)
        
    elif choice == '2':
        for product in products:
            print("\nProduct Details:")
            print(f"Item: {product['item']}")
            print(f"Quantity: {product['quantity']}")
            print(f"Price: {product['price']}")
            print(f"Total: {product['total']}")
            print()
    
    elif choice == '3':
        item = input("Enter the name of the item to update: ")
        
        for product in products:
            if product["item"].lower() == item.lower():
                print(f"Current details for {item}:")
                print(f"Quantity: {product['quantity']}")
                print(f"Price: {product['price']}")
                
                new_quantity = int(input("Enter the new quantity: "))
                new_price = float(input("Enter the new price: "))
                
                product['quantity'] = new_quantity
                product['price'] = new_price
                product['total'] = new_quantity * new_price
                
                print(f"Product '{item}' updated successfully.")
                break
        else:
            print(f"Product '{item}' not found in the inventory.")
    
    elif choice == '4':
        break
    
    else:
        print("Invalid choice, please try again.")
