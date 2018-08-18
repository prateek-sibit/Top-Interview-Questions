'''

Problem : Our task is to design an efficient 
algorithm to reverse a given integer. 
For example if the input of the algorithm 
is 1234 then the output should be 4321.

'''

# O(N) Time complexity
def reverseInt_python(integer):
    
    return int(str(integer)[::-1])

# O(N) Time complexity
def reverseInt(integer):
    
    tn = integer
    rev = 0
    
    while(tn>0):
        rev = (rev*10) + (tn%10)
        tn = tn//10
    return rev
        

# Testing
if __name__ == '__main__':
    
    numToRev = int(input('Enter Integer to Reverse : '))
    reversedInt = reverseInt(numToRev)
    print('Reverse of integer {0} is : {1}'.format(numToRev, reversedInt))
    