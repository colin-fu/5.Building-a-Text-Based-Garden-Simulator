# This game is about farming

import random


title = 'Farming Simulator'


class Plant():

    growth_stages = ['seed', 'sprout', 'plant', 'flower', 'harvest-ready']

    def __init__(self, name, harvest_yield):
        self.name = name
        self.plant_yield = harvest_yield
        self.current_growth_stage = 'seed'
        self.harvestable = False

    def grow(self):
            
        if self.current_growth_stage != 'harvest-ready':
            self.current_growth_stage = self.growth_stages[self.growth_stages.index(self.current_growth_stage) + 1]
            if self.current_growth_stage == 'harvest-ready':
                self.harvestable = True
                print(f'The: {self.name} is ready for harvest.')

    def harvest(self):

        if self.harvestable:
            self.harvestable = False
            self.current_growth_stage = 'seed'
            return True
        else:
            print(f'The: {self.name} is not ready for harvest.')

    
def select_item(items):
    if type(items) == dict and len(items) > 0:
        for indx, item in enumerate(list(items.keys())):
            print(f'{indx+1}: {item}')
    
    elif type(items) == list and len(items) > 0:
        for indx, item in enumerate(items):
            print(f'{indx+1}: {item.name}')


    else:
        print('Value Error')
        return None
    
    while True:
        user_input = input("Chose your plant: ") #Look in the solution if an try: statement is used. correct if so.
        try:
            user_input = int(user_input)
        except ValueError:
            print('Enter an integer')
            continue
        if user_input <= len(items):
            if type(items) == dict:
                return list(items.keys())[user_input - 1]
            else:
                return items[user_input-1]
        else:
            print(f'Please type in a number with a corresponding item.')


class Tomato(Plant):

    harvest_yield = 3
    growth_stages = ['seed', 'sprout', 'plant', 'flower', 'fruiting', 'harvest-ready']
    def __init__(self, name):
        super().__init__(name, Tomato.harvest_yield)


class Carrot(Plant):
    harvest_yield = 4
    growth_stages = ['seed', 'sprout', 'plant', 'flower', 'harvest-ready']
    def __init__(self, name):
        super().__init__(name, Carrot.harvest_yield)


class Lettuce(Plant):
    harvest_yield = 5
    growth_stages = ['seed', 'sprout', 'plant', 'flower', 'harvest-ready']
    def __init__(self, name):
        super().__init__(name, Lettuce.harvest_yield)

seeds = ['Tomato', 'Carrot', 'Lettuce']

class Gardener():
    '''

    The Gardener class models the player:
    -name represents the player's name
    -planted_plants is a list of the plants that are currently planted
    -inventory is a dictionary that stores the gardener's collections of seeds and harvested plants

    '''
    plant_dict = {'Tomato': Tomato, 'Carrot': Carrot, 'Lettuce': Lettuce}

    def __init__(self, name):
        self.name = name
        self.inventory = {} #The key is the name of the plant and the value the number of seeds of the plant
        self.planted_plants = [] #stores instances from class Plants

    def plant(self):
        print('Which plant would you like to plant?')
        self.select_item = select_item(self.inventory)
        if self.select_item in self.inventory and self.inventory[self.select_item] > 0:
            self.inventory[self.select_item] -= 1
            if self.inventory[self.select_item] == 0:
                del self.inventory[self.select_item]
            
            self.planted_plants.append(self.plant_dict[self.select_item](input('How should your plant be called?')))
            print(f'A {self.select_item} has successfully been planted.')

    def tend(self):
        for plant in self.planted_plants:
            if plant.harvestable == True:
                print(f'The {plant.name} is ready for harvest.')

            else:
                plant.grow()
                print(f'{plant.name} ({plant.__class__.__name__}) reach the the next growth stage: {plant.current_growth_stage}')

    def harvest(self):
        print('Which Plant would you like to harvest?')
        self.select_item = select_item(self.planted_plants)
        if self.select_item != None:
            if self.select_item.harvestable:
                if self.select_item.__class__.__name__ in self.inventory:
                    self.inventory[self.select_item.__class__.__name__] += self.select_item.harvest_yield
                else: 
                    self.inventory[self.select_item.__class__.__name__] = self.select_item.harvest_yield
            
                self.planted_plants.remove(self.select_item)
                print(f'The {self.select_item.name} have been harvested. The yield was {self.select_item.harvest_yield}.')
            else:
                print('Your plant is not ready for harvest!')
        else:
            print('There are no plants to harvest.')

    def forage_for_seeds(self):
        self.found_seed = random.choice(seeds)
        if self.found_seed in self.inventory:
            self.inventory[self.found_seed] += 1
        else: 
            self.inventory[self.found_seed] = 1
        print(f'You found a {self.found_seed} seed.')

    def display_inventory(self):
        print(self.inventory)

    def show_plants_growth_stage(self):
        print('You have planted the following plants: ')
        for plant in self.planted_plants:
            print(f'{plant.name} ({plant.__class__.__name__}): {plant.current_growth_stage}')



while True:
    player_name = input('Set you username: ')
    try:
        player_name = str(player_name)
        player = Gardener(player_name)
        break
    except ValueError:
        print('Please enter a valid Name.')
        continue

action_list = ['plant', 'tend', 'harvest', 'forage for seeds', 'show inventory', 'show growth stages',  'quit', 'exit', 'help']

print('Welcome to the Farming Simulator.')
print('Use the following commands to interact: ')
for indx, command in enumerate(action_list):
    print(f'{indx}: {command}')


while True:
    action = input('Choose your action: ')

    try:
        action = str(action)
        if action in action_list:
            if action == 'plant':
                player.plant()
            elif action == 'tend':
                player.tend()
            elif action == 'harvest':
                player.harvest()
            elif action == 'forage for seeds':
                player.forage_for_seeds()
            elif action == 'help':
                print('Use the following commands to interact:')
                for indx, command in enumerate(action_list):
                    print(f'{indx}: {command}')
            elif action == 'show inventory':
                player.display_inventory()
            elif action == 'show growth stages':
                player.show_plants_growth_stage()
            else:
                print(f'You left with {player.inventory}')
                break
            continue
        else:
            print('Please enter a existing action.')
            continue
    except ValueError:
        print('Please enter a existing action.')
        continue

    
#The harvest action is not working