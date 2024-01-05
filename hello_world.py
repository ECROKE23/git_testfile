print("Hello World")
print('----')

print ('test_dbrenn branch code')

print("added branch test_dbrenn")

# list of animals
animals = [ 'lion', 'dog', 'cats', 'tiger', 'monkey', 'horse', 'snake' ]

# print list until there is a snake
for pet in animals:
    if pet == 'snake':
        break
    print(pet)

print('----')

#print all animals except monkey and cat
for pet in animals:
    if pet != 'monkey' and pet != 'cat':
        print(pet)
        
print('----')

# print list but skip horse
for pet in animals:
    if pet == 'horse':
        continue
    print(pet)

print('----')

animals.reverse()
for pet in animals:
    if len(pet) <= 3:
        print(pet)
print('----')

for pet in animals:
    if len(pet) >= 5:
        print(pet)
print('----')

print(animals)

print('----')

pet_owners = ['ashley', 'brian', 'chris', 'naomi', 'richard', 'samantha', 'tina', 'venus']
print('Our pet owners dictionary will include important details')

for owner in pet_owners:
    print (owner)
    
