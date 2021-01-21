text = input("Enter a string : ")
text = text.lower()

if(text.split()[0] == text.split()[-1]):
    print("Yes")
else :
    print("No")
