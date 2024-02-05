from palindrome import palindrome

def test_palindrome_ok():
    assert palindrome('kayak')
    
def test_palindrome_ko():
    assert not palindrome('canoe')