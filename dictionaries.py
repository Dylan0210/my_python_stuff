# creating dictionaries

ages = {'dylan': 31, 'ashlee': 29, 'kenslee': 6}
print(ages)

weights = dict(dylan=155, ashlee=135, kenslee=55)
print(weights)

color = dict([('dylan','red'), ('ashlee', 'blue'), ('kenslee', 'pink')])   # using tuples to create dictionary
print(color)



# adding to dictionaries

ages['denise'] = 60           # adding key 'denise' to the ages dictionary
print(ages)



# re-assigning values in dictionaries

weights['kenslee'] = 52         # re-assigning value to 'kenslee' in the weights dictionary
print(weights)



# deleting from dictionaries

del color['dylan']        # deletes the key 'dylan' from the 'color' dictionary
print(color)



# using the 'ages' dictionary to view content within 

print(ages.items())      # gives the keys and values of dictionary

print(ages.values())     # gives JUST values of dictionary

print(ages.keys())       # gives JUST keys of dictionary



# returning a list from dictionary 'weights'

names = list(weights.keys())   # returns the keys
print(names)

weights_list = list(weights.values())   # returns the values
print(weights_list)



# returning a list of tuples called 'pairs' representing the key/values from dictionary 'color'

pairs = list(color.items())
print(pairs)