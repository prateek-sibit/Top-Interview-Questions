''' 

Problem : "A palindrome is a string that reads the same 
forward and backward"

For example: radar or madam

Our task is to design an optimal
algorithm for checking whether a given string is palindrome or not!

''' 

# O(N) Running time complexity
def checkPalindrome(string):
    
    # Returns True if string is palindrome ; False otherwise
    return string[:] == string[::-1]

# Testing
if __name__ == '__main__':
    
    string = input('Enter String to Check : ')
    isPalindrome = checkPalindrome(string)
    print('{} is Palindrome : {}'.format(string, isPalindrome))
