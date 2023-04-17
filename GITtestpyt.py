
'''
dictedto = {
    'harry' :'griffindoor',
    'melfoy' : 'sledirin',
    'hamadi' : 'zawiyt sheikh'
    
    }

print(dictedto)

dictedto['hermoyni'] = 'sledirin'

print(dictedto)
'''

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity         # tyara = flight(4) tyara.capacity() == 4
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.free_seats():
            return False
        self.passengers.append(name)
        return True
    
    def free_seats(self):
        return self.capacity - len(self.passengers)


tyara = Flight(4)
people = ['harry', 'marry', 'ali', 'hamada', 'ouahid', 'moha']

for person in people:
    success = tyara.add_passenger(person)
    if success:
        print(f'{person} has got a seat successfuly.')
    else :
        print(f'there is no seats left.')

print(tuple(tyara.passengers))