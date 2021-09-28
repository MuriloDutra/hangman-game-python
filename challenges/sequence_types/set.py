
#Collections of the type "<class 'set'>" don't allow repetition. So, every item in the collection, must be unique.
#If the add() function receives as parameter a item that already exists in the colletion, this parameter will be
#ignored and not included in the collection

ids = {1, 2, 3}
ids.add(4)
ids.add(4) #It'll be ignored and not included
print(f"Type: {type(ids)}")
print(f"IDs: {ids}")
