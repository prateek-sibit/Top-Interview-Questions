'''

Problem : We want to 
find duplicates in a one-dimensional 
array of integers in O(N) running time where 
the integer values are smaller than the length of the array!

Three approaches :
1) Brute Force comparing items with the rest -> O(N^2)
2) Hashmaps : Not an in place algorithm
3) Using Absolute values : O(N) running time that is inplace
    
'''

# O(N) Time complexity
def duplicates(array):
    
    for num in array:
        
        if array[abs(num)]>=0:
            array[abs(num)] = -array[abs(num)]
        else:
            print('Repetition Found : ',abs(num))

# Testing
if __name__ == '__main__':
    
    nums = [2,6,5,1,4,3,2]
    duplicates(nums)
    
   
        