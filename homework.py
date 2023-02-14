# Excercise 1:
class Cart():
    
    def __init__ (self, food, items):
        self.food = food
        self.item = items
        self.grocery_list = []
        
    def add_items(self):
        question = input('Would you like to add food or an item? - Type: food or item')
        if question == 'food':
            self.add_food()
        elif question == 'item':
            self.add_item()
            
    def add_item(self):
        item = input('\n' + 'What would you like to add to your list?')
        if item != 'done':
            print('\n' + f'{item} has been added to your list.')
            print('\t' + 'If finished adding, type "done".')
            self.grocery_list.append(item.title())
            self.add_item()
        elif item == 'done':
            self.display_list()
            print('\n')
            grocerylist.runner()
            
            
    def add_food(self):
        food = input('\n' + 'What would you like to add to your list?')
        if food != 'done':
            print('\n' + f'{food} has been added to your list.')
            print('\t' + 'If finished adding, type "done".')
            self.grocery_list.append(food.title())
            self.add_food()
        elif food == 'done':
            self.display_list()
            print('\n')
            grocerylist.runner()
        
    
    def remove_items(self):
        removing = input('\n' + 'What would you like to remove from the list?')
        if removing != 'done':
            print('\n' + f'{removing} has been removed from your list.' + '\n')
            print('\t' + 'If finished removing, type "done".')
            self.grocery_list.remove(removing.title())
            self.remove_items()
        elif removing == 'done':
            print('\n')
            self.display_list()
            print('\n')
            grocerylist.runner()
        
    def display_list(self):
        for items in self.grocery_list:
            print(items)
        print('\n')
            
    def runner(self):
        while True:
            options = int(input('What would you like to do? 1: Add | 2: Remove | 3: Display list | 0: Exit' ))
            if options == 1:
                self.add_items()
            elif options == 2:
                self.remove_items()
            elif options == 3:
                self.display_list()
                grocerylist.runner()
            elif options == 0:
                print('\n' + f'The final {self.food} items and {self.item} in your list are:')
                print('\n')
                self.display_list()
                print('\n')
                print('Have a great day!')
            break
           
        
grocerylist = Cart('food', 'items')
grocerylist.runner()

print('\n')


# Excercise 2:
class Python():
    def __init__(self, user_input):
        self.user_input = input('Please write a sentence here: ')
    def get_String(self):
        return f'Thank you'

class Printing(Python):
    def __init__(self, print_string):
        super().__init__(print_string)
        
    def print_String(self):
        return f'This is the final string: {(self.user_input).upper()}'

printedString = Printing(Python)

printedString = Printing(printedString.user_input)

print(printedString.print_String())