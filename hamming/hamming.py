# We read DNA using the letters C,A,G and T
# Haming Distance only calculates equal length 

def distance(strand_a, strand_b):
    if len(strand_a) != strand_b:
        raise Exception("Not the same length") 
    
    #Compare the diff
    diff = 0
    for i in len(strand_a):
        if strand_a[i] != strand_b[i]:
           


    #C,A,T, and G 
        #count the num and prints out 


#Test to pass 2 diff strings to compare 