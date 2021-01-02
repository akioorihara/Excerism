

def convert(number):
    a = ""
    if (number % 3 == 0):
        a += "Pling"
    if (number % 5 == 0):
        a += "Plang"
    if(number % 7 == 0):
        a += "Plong"
    if(a is ""):
        return number
    
    return a
     
x = int(input("Raindrop number: "))
print(convert(x))
