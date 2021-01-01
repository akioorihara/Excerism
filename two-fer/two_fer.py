

def two_fer(name=''):
    if name == '': 
        name ="you"
    return f"One for {name}, one for me."

x = input("Enter your name : ")
print(two_fer(x))
