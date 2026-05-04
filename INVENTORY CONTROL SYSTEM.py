#INVENTORY CONTROL SYSTEM
"""

Product   ( PID , Pname , Price , Pdesc )
Stock     ( PID , Quantity , Ministock , LastUpdated )
sales     ( PID , Qtysold, TotalPrice )

1 - Add Product
2 - View All Products
3 - Update Product
4 - Delete Prouct
5 - Add Stock
6 - View Stock
7 - Sell Product
8 - View Sales Report
9 - Low Stock Alert
0 - Exit

"""
# REQUIRED LIBRARIES
import pickle
import os

# A METHOD TO ADD A PRODUCTS INFO
def addProducts():
    file = open('products.bin','ab')
    pid = input("\n\t Create Product ID : ")
    pname = input("\t Enter Product Name : ")
    price = input("\t Enter Product Price : ")
    pdesc = input("\t Write About The Product : ")
    pickle.dump(pid,file)
    pickle.dump(pname,file)
    pickle.dump(price,file)
    pickle.dump(pdesc,file)
    print("\n\t Product Added Succesfully!")
    file.close()
    input("\t Press Enter To Continue...")

# A METHOD TO VIEW ALL PRODUCT's INFO
def viewAllProducts():
    file = open('products.bin','rb')
    try:
        while True:
            print("\n\t Product ID :",pickle.load(file))
            print("\t Product Name :",pickle.load(file))
            print("\t Product Price :",pickle.load(file))
            print("\t About Product :",pickle.load(file))
    except:
        print("\n\t Here is your all products..")
    file.close()
    input("\t Press Enter To Continue...")

# A METHOD TO UPDATE PRODUCT PRICE
def updateProduct():
    file1 = open('products.bin','rb')
    file2 = open('temp.bin','ab')
    pid = input("\n\t Enter Product ID To Update : ")
    flag = 0
    try:
        while True:
            data = pickle.load(file1)
            if data==pid:
                pickle.dump(data,file2)
                name = pickle.load(file1)
                pickle.dump(name,file2)
                print("\t Product Name :",name)
                print("\t Old Price :",pickle.load(file1))
                price = input("\t Enter New Price : ")
                pickle.dump(price,file2)
                pickle.dump(pickle.load(file1),file2)
                flag = 1
            else:
                pickle.dump(data,file2)
    except:
        if flag==1:
            print("\t Price Updated Successfully!")
        else:
            print("\t Product Not Found!")
    file1.close()
    file2.close()
    os.remove('products.bin')
    os.rename('temp.bin','products.bin')
    input("\t Press Enter To Continue...")

# A METHOD TO DELETE A PRODUCT'S INFORMATION
def deleteProducts():
    file1 = open('products.bin','rb')
    file2 = open('temp.bin','ab')
    pid = input("\t Enter Product ID To Delete : ")
    flag = 0
    try:
        while True:
            data = pickle.load(file1)
            if data==pid:
                print("\t Product Name :",pickle.load(file1))
                pickle.load(file1)
                pickle.load(file1)
                flag = 1
            else:
                pickle.dump(data,file2)
    except:
        if flag==1:
            print("\n\t Product Deleted Successfully!")
        else:
            print("\n\t Product Not Found!")
    file1.close()
    file2.close()
    os.remove('products.bin')
    os.rename('temp.bin','products.bin')
    input("\t Press Enter To Continue...")

# A METHOD TO ADD A STOCK INFO
def addStock():
    file = open('stock.bin','ab')
    pid = input("\n\t Enter Product ID : ")
    quantity = input("\t Enter Quantity  : ")
    ministock = input("\t Enter Ministock : ")
    lastUpdated = input("\t Enter LastUpdated  : ")
    pickle.dump(pid,file)
    pickle.dump(quantity,file)
    pickle.dump(ministock,file)
    pickle.dump(lastUpdated,file)
    print("\n\t Stock Added Succesfully!")
    file.close()
    input("\t Press Enter To Continue...")
# A METHOD TO VIEW ALL STOCK's INFO
def viewAllStocks():
    file = open('stock.bin','rb')
    try:
        while True:
            print("\n\t Product ID :",pickle.load(file))
            print("\t Quantity :",pickle.load(file))
            print("\t Ministock :",pickle.load(file))
            print("\t LastUpdated :",pickle.load(file))
    except:
        print("\n\t Here is your all Stocks..")
    file.close()
    input("\t Press Enter To Continue...")

# A METHOD TO GET A PRODUCT'S INFORMATION
def getProduct(pid):
    prod = []
    file = open('products.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            if data==pid:
                prod.append(data)
                prod.append(pickle.load(file))
                prod.append(pickle.load(file))
                prod.append(pickle.load(file))
    except:
        pass
    file.close()
    return prod

# A METHOD TO GET A STOCK INFORMATION
def getStock(pid):
    stock = []
    file = open('stock.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            if data==pid:
                stock.append(data)
                stock.append(pickle.load(file))
                stock.append(pickle.load(file))
                stock.append(pickle.load(file))
    except:
        pass
    file.close()
    return stock


# A METHOD TO SELL PRODUCT
def sellProduct():
    pid = input("\n\t Enter Product ID : ")
    prod=getProduct(pid)
    if len(prod)!=0:
        print("\t product Name :",prod[1])
        print("\t product price :",prod[2])
        stock = getStock(pid)
        if len(stock)!=0:
            print("\t Available Stock :",stock[1])
            print("\t Lastupdated :",stock[3])
            qty = input("\t Enter Quantity : ")
            AvailableStock=int(stock[1])
            stock_file = open('stock.bin', 'rb')
            temp_file = open('temp.bin', 'ab')

    found = False

    try:
        while True:
            product_id = pickle.load(stock_file)
            available_stock = int(pickle.load(stock_file))
            ministock = pickle.load(stock_file)
            lastupdated = pickle.load(stock_file)

            if product_id == pid:
                found = True

                if available_stock >= int(qty):   
                    remaining_stock = available_stock - int(qty)

                    print("\n\t Product Sold Successfully!")
                    print("\t Total Bill : ", int(qty) * int(prod[2]))
                    print("\t Remaining Stock :", remaining_stock)

                    sale_file = open('sales.bin', 'ab')
                    pickle.dump(pid, sale_file)
                    pickle.dump(qty, sale_file)
                    sale_file.close()
                    
                    #  save sales file
                    pickle.dump(product_id, temp_file)
                    pickle.dump(remaining_stock, temp_file)
                    pickle.dump(ministock, temp_file)
                    pickle.dump(lastupdated, temp_file)

                else:
                    print("\n\t Not enough stock!")

                    #  keep original stock
                    pickle.dump(product_id, temp_file)
                    pickle.dump(available_stock, temp_file)
                    pickle.dump(ministock, temp_file)
                    pickle.dump(lastupdated, temp_file)

            else:
                pickle.dump(product_id, temp_file)
                pickle.dump(available_stock, temp_file)
                pickle.dump(ministock, temp_file)
                pickle.dump(lastupdated, temp_file)

    except:
        pass

    stock_file.close()
    temp_file.close()

    os.remove("stock.bin")
    os.rename("temp.bin", "stock.bin")

    if found == False:
        print("\n\t Product ID not found!")

    input("\t Press Enter To Continue...")


# METHOD TO View Sales Report
def viewSalesReport():
    file = open('sales.bin','rb')
    try:
        while True:
            pid=pickle.load(file)
            qty=pickle.load(file)
            prod=getProduct(pid)
            print("\t Product ID :", pid)
            print("\t Product name :", prod[1])
            print("\t Quantity Sold :", qty)
            print("\t Total Bill Amount :", int(qty)*int(prod[2]))
    except:
        print("\n\t All Sales Records Displayed!")
    file.close()
    input("\t Press Enter To Continue...")

# METHOD TO Low Stock Alert

def lowStockAlert():
    file = open('stock.bin','rb')
    flag=0

    try:
        while True:
            pid = pickle.load(file)
            quantity = int(pickle.load(file))
            ministock = int(pickle.load(file))
            lastupdated = pickle.load(file)
            prod=getProduct(pid)

            if quantity < ministock:
                print("\n\t  LOW STOCK ALERT ")
                print("\t Product ID :", pid)
                print("\t Product Name :", prod[1])
                print("\t Available Quantity :", quantity)
                print("\t Minimum Required :", ministock)
                flag=1

    except:
        if flag==0:
            print("\n\t All products have sufficient stock!")

    file.close()
    input("\t Press Enter To Continue...")
# DASHBOARD
while True:
    print("\n\t **** INVENTORY CONTROL SYSTEM  ****")
    print('''
            1- Add Product
            2- View All Products
            3- Update Product
            4- Delete Prouct
            5- Add Stock
            6- View Stock
            7- Sell Product
            8- View Sales Report
            9- Low Stock Alert
            0- Exit
    ''')
    ch = int(input("\t Enter Your Choice : "))
    if ch==0:
        print("\n\t\tBye-Bye Admin!")
        break
    elif ch==1:
        addProducts()
    elif ch==2:
        viewAllProducts()
    elif ch==3:
        updateProduct()
    elif ch==4:
        deleteProducts()
    elif ch==5:
        addStock()
    elif ch==6:
        viewAllStocks()
    elif ch==7:
        sellProduct()
    elif ch==8:
        viewSalesReport()
    elif ch==9:
        lowStockAlert()
