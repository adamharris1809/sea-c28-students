#!/usr/bin/env python

"""Creating a function that accepts any text each letter is replaced by the letter 13 characters away from it."""

def rot13(user_input = raw_input(u"Input text to scramble. ")):
    new_text = ""

    for letters in user_input:
        if letters.isalpha():
            alphabet = ord(letters)+13
            if alphabet > ord('z'):
                alphabet -= 26
            if letters.isupper() and alphabet > ord('Z'):
                alphabet -= 26
            lastletter = chr(alphabet)
        new_text += lastletter
    print(new_text)
    return(new_text)

rot13()

if __name__ == "__main__":
    """Checking to see if the function works properly."""
    assert rot13("abcdefghijklmnopqrstuvwxyz") == "nopqrstuvwxyzabcdefghijklm"
    assert rot13("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "NOPQRSTUVWXYZABCDEFGHIJKLM"