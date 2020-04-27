x = True


def execute_command(s):
    if s == 'load':
        with open('./sales.txt', 'r') as f:
            itemsdic = {}
            itemsdic = f.read()
            print(itemsdic)

    elif s == 'show items':
        with open('./list_of_items.txt', 'r') as f:
            mlaidic = {}
            mlaidic = f.read()
            print(type(mlaidic))
            print(mlaidic)
    elif s == 'sell':
        with open('./sales.txt', 'a') as f:
            item = str(input('Please enter sold item name'))
            ammount_sold = str(input('Please enter num of pieces sold'))
            f.write('{} {}'.format(item, ammount_sold))
            print('Item added successfully')
    elif s == 'add':
        with open('./list_of_items.txt', 'a') as f:
            new_item = str(input('Please enter name of product'))
            price = str(input('To complete please enter price of item'))
            mydic = {}
            mydic[new_item] = price
            f.write(mydic[new_item])
            print('New item added')


while x == True:
    user_input = str(input("please enter your command- "))
    if user_input == 'exit':
        x = False
        print('thanks for your time')
    else:
        execute_command(user_input)
