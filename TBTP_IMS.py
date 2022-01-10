def Display_Menu():
    print("=================="
          "\n   TBTP IMS   \n"
          "==================")

    print("A - Add item\n"
          "R - Remove item\n"
          "L - List of items\n"
          "U - Update item\n"
          "S - Search item\n"
          "M - Menu\n"
          "X - Exit")

    choice = input('> ').lower()
    print()

    Selection(choice)


def Selection(choice):
    match(choice):
        case 'a':
            add()

        case 'r':
            remove()

        case 'l':
            list()

        case 'u':
            ""

        case 's':
            ""

        case 'm':
            Display_Menu()

        case 'x':
            exit()

        case _:
            Display_Menu()

def add():
    f = open('storage.txt', 'a')
    for _ in range(0, int(input("Enter number of items to add: "))):

        print()
        item_name = input("Item Name: ").lower()
        item_quantity = input("Item Quantity: ")

        f.write(item_name + '\n')
        f.write(item_quantity + '\n')

    f.close()
    print()
    Display_Menu()

def remove(): 
    for _ in range(0, int(input("Enter number of items to remove: "))):

        try :
            f = open('storage.txt', 'r+')
            items = f.readlines()
            f.seek(0)
            remove_item = input("Item to remove: ").lower()
            remove_quantity = int(input("Quantity to remove: "))

            for i, item in enumerate(items) :

                if item.strip("\n") == remove_item :
                    remaining = int(items[i + 1])

                    if remaining - remove_quantity <= 0 :
                        items.pop(i + 1)

                    else :
                        value = remaining - remove_quantity
                        f.write(items[i])
                        items.pop(i + 1)
                        f.write(str(value)+ "\n")

                elif item.strip("\n") != remove_item :
                    f.write(item)

        except :
            print("Error, please follow the instructions carefully.")
                
        f.truncate()
        f.close()
        
    print()
    Display_Menu()

def list():
    f = open("storage.txt", 'r')
    for x in f.read():
        print(x, end='')

    f.close()
    print()
    Display_Menu()


Display_Menu()
