def clean_text(text) :
    cleaned = "".join(ch.lower() for ch in text if (ch.isalpha() or ch.isnumeric()))
    print('Clean text =',cleaned)
    return cleaned

def is_palindrome(cleaned) :
    if cleaned == cleaned[::-1] :
        return True
    else :
        return False
    
text = input('Enter a sentence: ')
cleaned = clean_text(text)
result = is_palindrome(cleaned)
if result == True :
    print('That is a palindrome.')
else :
    print('That is not a palindrome.')