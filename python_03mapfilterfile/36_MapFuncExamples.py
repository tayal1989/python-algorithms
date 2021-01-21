#Convert these names to upper case
names = ['arun', 'hari', 'john', 'manu']

def uppercase(name):
    return name.upper()

res = map(uppercase, names)
print(list(res))

#Convert all the elements to int & find the total sum
arr = ["10", "20", "30", "40", "50"]

def convertToInt(num):
    return int(num)

res = map(convertToInt, arr)
print(sum(list(res)))

#Swap the first and last letter of each name
names = ['arun', 'hari', 'john', 'manu']

def swap(name):
    return name[-1] + name[1:-1] + name[0]

res = map(swap, names)
#res = map(lambda x:x[-1] + x[1:-1] + x[0], names)
print(list(res))

#Get the month field from the dates
dates = ['12-jan', '15-dec', '20-mar', '11-oct']

def month(date):
    return date.split("-")[1]

res = map(month, dates)
#res = map(lambda date:date.split("-")[1], dates)
print(list(res))

#Get sum of all the values of zones
zones = ['north=10', 'south=20', 'east=30', 'west=40']

def direction(zone):
    return int(zone.split("=")[1])

res = map(direction, zones)
#res = map(lambda zone:int(zone.split("=")[1]), zones)
print(sum(list(res)))