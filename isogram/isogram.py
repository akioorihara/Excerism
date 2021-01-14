#isogram checker python 



def is_isogram(string):
    isogram = 0
    #check if the value is repated by for-loop 
    for u in range(len(string)):
        for i in range(len(string)):
            if u == i:
                break
                #skip this loop and no need to check 
            if string[u] == string[i]:
                if ' ' != string[i] or '-' != string[i]:
                    isogram += 1
    
    print(isogram)
    return isogram

test        = "backgroud"
testTwo     = "marioandpeach"
testThree   = "six-year-old"
testFour    = "six-year-six"
is_isogram(test)
is_isogram(testTwo)
is_isogram(testThree)
is_isogram(testFour)

