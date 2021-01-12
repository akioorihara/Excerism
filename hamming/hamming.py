# We read DNA using the letters C,A,G and T
# Haming Distance only calculates equal length 

def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError(" {strand_a} and {strand_b} are not the same length")
    
    #Compare the diff
    diff = 0
    for i in range(len(strand_a)):
    
        if strand_a[i] != strand_b[i]:
            diff += 1 
            # print(diff)
    
    return diff

#Test to pass 2 diff strings to compare 
# Demo 
strand_a = "GAGCCTACTAACGGGCT"
strand_b = "CATCGTAATGACGGCCT"
print(distance(strand_a, strand_b))