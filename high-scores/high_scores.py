import random

def latest(scores): 
    return scores[-1]
    
def personal_best(scores):
    scores.sort()
    return scores[-1]

def personal_top_three(scores):
    #sort and then list the last three of the list 
    scores.sort()
    return scores[-1], scores[-2], scores[-3]
    


scores = []
for i in range(0,9):
    y = (random.randint(1,10))
    scores.insert(i,y) 
    print(scores[i], end=" ")

x = int(input("| Enter a value : "))
scores.append(x)
print("The late number is : ", latest(scores))
print("The highest number is : ", personal_best(scores))
print("The top three numbers are : ", personal_top_three(scores))