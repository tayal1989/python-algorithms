import time

start = time.clock()	#From CPU clocks, based on hardware timers
s = time.time()			#From system time

print("Hello")

for i in range(1, 11):
    print(i)

print("End of main")

end = time.clock()
e = time.time()

print(end-start)
print(e - s)			#We should evaluate based on system timing
