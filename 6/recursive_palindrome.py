def recursive_palindrome(word):
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:  
        return False
    return recursive_palindrome(word[1:-1])



print(recursive_palindrome('racecarr'), False)
print(recursive_palindrome('deleveled'), True)
print(recursive_palindrome(''), True)
print(recursive_palindrome('a'), True)
print(recursive_palindrome('releveler'), True)
print(recursive_palindrome('deified'), True)
print(recursive_palindrome('ivva'), False)
print(recursive_palindrome('avvaa'), False)
# print(recursive_palindrome('no x in nixon'))

