def two_fer(name):
    return f"One for {name}, one for me."

x = input("Enter your name : ")
if x: 
    pass 
else: 
    x = "you"
print(two_fer(x))
