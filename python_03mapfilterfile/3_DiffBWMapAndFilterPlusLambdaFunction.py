import time

dates = ['15-mar', '12-jan', '10-feb', '22-jan', '20-dec', '31-jan']

curr_day = time.strftime("%a").lower()
curr_month = time.strftime("%b").lower()

#print(curr_day)			#Will return current day
#print(curr_month)			#Will return current month

def month(date):
    if time.strftime("%b").lower() == date.split("-")[1]:
        return date
    else:
        return None

res = map(month, dates)
print(list(res))			#Output : [None, None, '10-feb', None, None, None]

res = filter(month, dates)
print(list(res))			#Output : ['10-feb'] #as today's date is 2 Feb, 2016

#Teacher method to display current month from values of dates
res = map(lambda x:x.split("-")[1] == curr_month, dates)
print(list(res))

res = filter(lambda x:x.split("-")[1] == curr_month, dates)
print(list(res))

print(list(filter(lambda x:x.split("-")[1] == curr_month, dates)))

#Difference between map and filter is map will give you all the values even if it is false or None
#however, filter will separate the values or will not display the values who are either None or False