#Accept a snack name from the user
#If the snack name is there, display snack name and its price
#If not, display all the snack names vertically
'''
menu = {'vada' : 40, 'bhel' : 35, 'pizza' : 25, 'puri' : 35, 'idli' : 50}

snack_name = input("Enter snack name : ")

if snack_name in menu:
    print(snack_name, " - ", menu[snack_name])
else:
    #print(list(menu.keys()))
    print("Valid are ", "\n".join(menu))
    #for i in menu.keys():
    #    print(i)
'''

#Create a empty dict named "studs" with name as a key and total marks as value
#print the dict using for loop
data = ['arun 10-20-30-40-50',
        'john 32-45-56-34-65',
        'hari 43-43-76-65-34',
        'mani 23-54-87-45-87'
        ]

studs = {}

for i in data:
    marks = i.split(" ")[1]
    mark = marks.split("-")
    mark[:] = map(int, mark)
    studs[i.split(" ")[0]] = sum(mark)

for i in studs:
    print(i, " - ", studs[i])

print(studs)
