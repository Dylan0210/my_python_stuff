# while loop

count = 1
while count <= 4:
    print("looping")
    count +=1



# for loop

n = 5
for number in range(0, n):
    if number <= n:
        print(number ** 2)


 
# for loop w/ tuples

point = (1, 2, 3)
for value in point:
    print(value)
   
    
    
# for loop w/ dictionaries

ages = {'dylan': 31, 'ashlee': 29, 'kenslee': 6}
for key in ages:
    print(key)
    
   
    
# for loop w/ strings

for letter in "dylan":
    print(letter)