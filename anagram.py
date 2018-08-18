'''

Problem : Construct an algorithm to 
check whether two words (or phrases) 
are anagrams or not!

The original word or phrase is called the subject

Any word or phrase that reproduces the letters in another order
is called anagram

'''

def is_anagram(str1, str2):
    
    # if the strings have different lengths they cannot be anagrams
    if len(str1) != len(str2):
        return False
    
    # sort the strings alphabetically
    # bottleneck because it as O(NlogN) running time ; N : No. of characters
    str1 = sorted(str1)
    str2 = sorted(str2)
    
    # linear search with O(N) but the overall time is 
    # O(NlogN) + O(N) = O(NlogN) linearthimic running time
    for i in range(0,len(str1)):
        if str1[i] != str2[i]:
            return False
        
    return True

# Testing 
if __name__ == '__main__':
    
    str1 = 'restful'
    str2 = 'fusterl'
    
    check = is_anagram(str1, str2)
    print(check)