print("Hello World")
print()

# tuple of animals
animals = ( 'lion', 'dog', 'cat', 'tiger', 'monkey', 'horse', 'snake' )

# print list until there is a snake
for pet in animals:
    if pet == 'snake':
        break
    print(pet)

print()

for pet in animals:
    if pet 1= 'monkey' and pet != 'cat':
        print(pet)
        


print('----')
# print list but skip horse
for pet in animals:
    if pet == 'horse':
        continue
    print(pet)
