price = {"pizza":10,"burger":7.5,"shawarma":7.5,"coolcake":15,"pasta":8,"biryani":15,
             "tea":4,"coffee":4}

grocery_items = []
amount = 0
quant = 0
menu =input("You Want Menu Card[Y/N] :").lower()
if "y" == menu:
    print("------------------------------------")
    print("->       Welcome To My Hotel      <-")
    print("------------------------------------")
    print("->             Menu               <-")
    print("------------------------------------")
    print(" Items                 Prices       ")
    print("------------------------------------")
    print(" 1.Pizza                10 $\n",
        "2.Burger              7.5 $\n",
        "3.Shawarma            7.5 $\n",
        "4.Cool_cake           15 $ / kg\n",
        "5.Pasta               8 $\n",
        "6.Biryani             15 $\n",
        "7.Tea                 4 $\n",
        "8.coffee              4 $")
    print("------------------------------------") 
elif "n" == menu:
    print("Okay Thank You ")
else:
    print("Choose any one option [Y/N]......")
while True:
    item_name = input("Enter the item what do you want to order [or type ok to finish] : ").strip().lower()
    if item_name == "ok":
        break
    if item_name  not in price:
        print("item not found in Grocery list.....\n")
        continue
    prices = price[item_name]
    try:
        quantity = int(input("Enter the quantity : "))
        quant += quantity
        
    except ValueError:
        print("IN valid quantity...\n")
        continue
    item_total = prices * quantity
    amount += item_total
    grocery_items.append([item_name,prices,quantity,item_total])
    print("Items added to cart!!!\n")
    
    

    def view_bill():
        bill = input("If You want Bill Enter Yes:").lower()
        if bill == "yes":
            
            print("-"*40)
            print("            Welcome To My Shop        ")
            print("-"*40)
            print("Item    cost/item    qunatity      Total")
            #print("-"*40)
            #print("-"*40)
            #print(f"{item_name:<12}{prices:<12}{quantity:<12}{amount:<12}")
            print("-"*40)
        
            for item in grocery_items:
                print(f"{item[0]:<12}{item[1]:<12}{item[2]:<12}{item[3]:.2f}")
            print("-"*40)
            print(f"Grand total            {quant}          {amount:.2f}$" )
            print("-"*40)
            print("        Thank for visting         ")
        elif bill == "no":
            exit()
        
        else:
            print("Please Enter Yes or No Only...???")
    brake = input("You wnt to add more items [Y/N] : ").lower()
    if brake == "y":
        continue
    elif brake == "n":
        break

    else:
        print("you enter wrong word .......")
view_bill()
   
            
   

    

    
    
