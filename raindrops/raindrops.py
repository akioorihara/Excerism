

def convert(number):
    if (number % 3):
        return "Pling"
    elif (number % 5):
        return "Plang"
    elif(number % 7):
        return "Plong"
    else:
        return "not mod by 3, 5, or 7"
     
x = int(input("Raindrop number: "))
# xprint(type(x))
print(convert(x))
