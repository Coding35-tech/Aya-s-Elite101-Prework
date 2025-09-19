print('~*~Welcome to the Pretty in Pink Boutique Chatbot!')
name = input('What is your name? ')
age = input('Hello ' + name + ', how old are you? ')
print ('Hello' + name + str (age) + ',Welcome! I know you are going to like it here! XD')
print (' 1. Give input for a new item \n 2. Return an item \n 3. Ask for the price of an item. \n 4. Check out a dress \n 5. Check out a jewlery set. \n 6. Check out a random trendy outfit ')
user_input = int(input('Select an option(1-6): '))
if user_input == 1:
    print('You have selected to give input for a new item.')
    new_item = input('Suggest an item here: ')
elif user_input == 2:
    print('You have selected return an item.')
    return_item = input('Type which item you wish to return here please: ')
elif user_input == 3:
    print('You have selected the price check.')
    price_check = input('Which item to check the price of? ')
elif user_input == 4:
    print ('You have selected a dress to purchase.')
elif user_input == 5:
    print ('You have selected a jewlery set to purchase.')
elif user_input == 6:
    print('You have selected a random trendy outfit to purchase.')
else:
    print('The user input is not valid.')
