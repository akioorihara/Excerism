def two_fer(name):
    if name is None:
        return "One for you, one for me."
    else:
        return "One for ", name, ", and one for me."

x = input()
two_fer(x)
