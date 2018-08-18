'''

Problem : Create an algorithm to find the sum 
of contiguous subarray within a 
one-dimensional array of numbers 
which has the largest sum!

Applications : 

1) Computer vision : to detect the brightest area in an image
    It is crucial in haar features, deep learning, self driving cars

2) Genomic sequence analysis : We can identify important segments of protein
    sequences and the information to be able to predict outcomes

3) Data mining : largest subarray problem is important when dealing 
    with association rules and forseeing customer behaviour
    
'''

# O(N) Time Complexity
def kadane_algorithm(nums):
    
    max_global = nums[0]
    max_current = nums[0]
    
    for i in range(1,len(nums)):
        
        max_current = max(nums[i], max_current+nums[i])
        
        if max_current > max_global:
            max_global = max_current
    
    return max_global

# Testing
if __name__ == '__main__':
    
    nums = [1,-2,3,4,-5,8]
    
    print(kadane_algorithm(nums))