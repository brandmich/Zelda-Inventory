inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], 
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
} #in the inventory there is gold, a pouch, and a backpack

#In the inventory is a burlap bag, and in the burlap bag is an apple, small ruby, and three toed sloth
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

#in the inventory is a pocket, and in the pocket is a seashell, strange berry, and lint
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

inventory['pouch'].sort() #sorts pouch items 
inventory['backpack'].sort() #sorts backpack items
inventory['backpack'].remove('dagger') #removes dagger from the backpack

inventory['gold'] = 550 #adds 50 gold

print(inventory)

