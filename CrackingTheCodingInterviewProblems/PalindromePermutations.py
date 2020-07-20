# Problem Description:
#
# Palindrome Permutation - Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters
# The palindrome does not need to be limited to just dictionary words.
#
# EXAMPLE - Input: "Tact Coa" Output: True (via "taco cat", "atco cta", and others)

# Solution note: a palindrome can only have at most one character with an odd number of instances within the string
# The same holds for a permutation of a palindrome

def isPermutationOfPalindrome(text):
    textNoWhiteSpace = text.replace(" ", "")
    textFormatted = textNoWhiteSpace.lower()
    lettersInText = {}
    oddCount = 0

    for i in range(0, len(textFormatted)):
        char = textFormatted[i]
        if char in lettersInText:
            lettersInText[char] += 1
        else:
            lettersInText[char] = 1
    
    for key in lettersInText:
        if lettersInText[key] % 2 == 1:
            oddCount += 1
    
    return oddCount < 2

def main():
    print("Testing 'Tact Coa', expected output is true")
    print(isPermutationOfPalindrome("Tact Coa"))

    print("Testing 'bhhhbi', expected output is false")
    print(isPermutationOfPalindrome("bhhhbi"))
    
main()