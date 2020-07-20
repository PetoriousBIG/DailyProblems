# Problem Descirption:
# 
# Replace all spaces in a string with '%20' You may assume that the string has sufficient 
# space at the end  to hold the additional characters, and that you are given the "true"
# length of the string.
#
# Example: Input - ("Mr John Smith    ", 13)
#          Output - "Mr%20John%20Smith"
#
# 
#

def URLify(string, stringTrueLength):
    
    whiteSpaces = 0
    whiteSpace = " "
    replacementString = "%20"
    
    for i in range(stringTrueLength - 1, -1, -1):
        if string[i] == " ":
            whiteSpaces += 1
    
    return string.replace(" ", replacementString, whiteSpaces)

        

def main():
    print("Testing 'Mr John Smith    ', expected output is Mr%20John%20Smith")
    print(URLify("Mr John Smith    ", 13))

main()