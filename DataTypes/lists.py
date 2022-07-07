# create list
color = ["red", "blue", "green", "yellow"]
print(color)
 # color = []
 # color = list()
 
# read list
color = ["red", "blue", "green", "yellow"]
print(color[1])

# return the last value in a list
print(color[-1])

# finding length of list
print(len(color))                                              

# append item to list
color.append("pink")
print(color)

# insert item to specific point in list
color.insert(2,"black")
print(color)

# organizing list
print(sorted(color))                                # sorted does not alter the original order of list

color.sort()                                        # sort alters the list permanently
print(color)

color.reverse()                                     # reverse list permanently
print(color)

# delete item from list
del color[1]
print(color)