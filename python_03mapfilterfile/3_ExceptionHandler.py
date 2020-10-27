#For finding the error in particular line, we use traceback
import sys, traceback

c = 0

try:
    a = input("Enter a no : ")
    b = input("Enter a no : ")
    c = int(a) + int(b)

    #User defined exception can be used with keyword raise
    #raise EOFError("End of file error")

except ValueError as e :
    print("Value Error : ", e)
    print(type(e))
    print("System info : ", sys.exc_info())
    traceback.print_exc()

#Exception will handle all type of error so it is compulsory to put Exception in the last
except Exception as e1:
    print("Exception : ", e1)
    print(type(e1), e1)


#Else part will execute only when "try" block gets executed successfully
else:
    print("Result : ", c)

#Finally part will execute every time even if try block is pass or fail
finally:
    print("Done")
