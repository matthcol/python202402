# define function palidrome
# palindrome('kayak') -> True

# module: palindrome

def palindrome(text):
    return text == text[::-1]

if __name__ == '__main__':        
    ok1 = palindrome('kayak')
    ok2 = palindrome('canoe')
    print(ok1, ok2)