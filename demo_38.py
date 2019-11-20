animals = ['alpaca', 'baboon']


def addAnimal(x):
    x.append('zebra')


print(hex(id(animals)), animals)
addAnimal(animals)
print(hex(id(animals)), animals)
animals2 = ('alpaca', 'baboon')


def addAnimal2(x):
    x += ('zebra',)
    print('inside, x={}'.format(x))

print(hex(id(animals2)), animals2)
addAnimal2(animals2)
print(hex(id(animals2)), animals2)