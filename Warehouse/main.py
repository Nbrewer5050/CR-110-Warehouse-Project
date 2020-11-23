"""
Program: Warehouse control
Author: Nicholas Brewer
Date: Nov. 2020
Functionality:
    -Register products
        - id (auto generated)
        - title
        - category
        - stock
        - price

"""

# imports
from menu import clear, print_menu, print_header, print_product_info
from product import Product
import pickle

#global vars
catalog = []
next_id = 1


# functions
def serialized_data():

    try:
        writer = open('warehouse.data', '(wb') # wb = write binary
        pickle.dump(catalog, writer)
        writer.close()
        print("** Data serialized!")
    except:
        print("** Error, data not saved. Dont close system")


def deserialized_data():
    global next_id

    try:
        reader = open('warehouse.data', 'rb') # rd = read binary
        temp_list =pickle.load(reader)
        reader.close() 

        for prod in temp_list:
            catalog.append(prod)

        last = catalog[-1]
        next_id = last.id + 1
    
        how_many = len(catalog)
        print("** Read: " + str(how_many) + " products")

    except:
        print("** Error, no data file found")
    
    
def register_product():
    global next_id

    try:
        print_header("Register new Product")
        title = input('Please provide the Title: ')
        cat = input('Please provide the Category: ')
        stock = int(input("Please provide initial Stock: "))
        price = float(input("Please provide the Price: "))

        #validations
        if(len(title) < 1):
            print("*Error: Title should not be empty")

        product = Product(next_id, title, cat, stock, price)
        next_id += 1
        catalog.append(product)
    except:
        print("** Error, try again")        
   

   

def display_catalog():
    print_header("Current Catalog")
    for prod in catalog:
        print_product_info(prod)
 

def display_no_stock():
    print_header("Product out of stock")
    for prod in catalog:
        if(prod.stock == 0):
            print_product_info(prod)
  

def total_stock_value():
    print_header("Total Stock Value")
    total = 0
    for prod in catalog:
        total = prod.price * prod.stock
    
    print("Total stock value: $" + str(total))


def cheapest_product():
    print_header("Print the cheapest product")            


def delete_product():
    display_catalog()
    id = int(input("ID of item to delete: "))

    found = False
    for prod in catalog:
        if(prod.id == id):
            found = True
            catalog.remove(prod)
            print("** Item removed!")

    if(not found):
        print("** Incorrect id, try again")        

def update_product_price():
    print_header("Update product price")
    display_catalog()

    try:
        id = int(input("id of the product to update: "))

        found = False
        for prod in catalog:
            if(prod.id == id):
                found = True
                price = float(input("Please provide the new price: $"))
                prod.price = price
                print("** Price updated")

        if(not found):
            print("Incorrect Id, try again")    

        return found # True if catalog was modified, False if not         
    except:
        print("** Unexpected error!")
        return False
# instructions

def update_product_stock():
    print_header("Update product stock")
    display_catalog()

    try:
        id = int(input("Id of the product to update: "))

        found = False
        for prod in catalog:
            if(prod.id == id):
                found = True
                stock = float(input("Please provide the new price: $"))
                prod.stock = stock
                print("** Stock updated")

        if(not found):
            print("Incorrect Id, try again")    

        return found # True if catalog was modified, False if not         
    except:
        print("** Unexpected error!")
        return False

def most_expensive_items():
    print_header(" 3 most expensive products prices")
    # Create an array of prices (numbers only)
    prices = []
    for prod in catalog:
        prices.append(prod.price)

    # Sort the array 
    prices.sort(reverse=True)

    #print
    print(prices[0]) #find a product
    print(prices[1])
    print(prices[2])

def distinct_categories():
    print_header("** Distinct Categories")
    category = []
    for prod in catalog:
        category.append(prod.category)
    print(category[0])
    print(category[1])
    print(category[2])


deserialized_data()
input("press Enter to continue...")

opc = ''
while(opc != 'x'):
    clear()
    print_menu()
    opc = input('Please select an option: ')

    if(opc == '1'):
        register_product()
    elif(opc == '2'):
        display_catalog()
    elif(opc == '3'):
        display_no_stock()
    elif(opc == '4'):
        total_stock_value()
    elif(opc == '5'):
        cheapest_product()
    elif(opc == '6'):
        delete_product()
        serialized_data()
    elif(opc == '7'):
        if(update_product_price()):
            serialized_data()
    elif (opc == '8'):
        update_product_stock()
        serialized_data()
    elif(opc == '10'):
        most_expensive_items()
    elif(opc == '11'):
        distinct_categories()        
    elif(opc == 's'):
        serialized_data   


    input('Press Enter to continue...')


print('Good byte!')
