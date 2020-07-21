# Problem Description:
#
# There are three types of edits that can be performed on strings:
#   Insert a character
#   Remove a character
#   Replace a chacters
#
# Given two strings, write a function that to check if if they are within one edit from eachother.
# EXAMPLES
#   pale, ple -> true
#   pales, pale -> true
#   pale, bale -> true
#   pale, bake -> false

def oneEditAway(s1, s2):
    s1Length = len(s1)
    s2Length = len(s2)
    areStringOneEditAway = False
    
    if(s1Length == s2Length):
        areStringsOneEditAway = checkIfReplacement(s1, s2)
    elif(s1Length - 1 == s2Length):
        areStringsOneEditAway = checkIfInsertion(s1, s2)
    elif(s1Length + 1 == s2Length):
        areStringsOneEditAway = checkIfInsertion(s2, s1)

    return areStringsOneEditAway

def checkIfReplacement(s1, s2):
    diffChars = 0

    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            diffChars += 1
        if diffChars > 1:
            return False
    return True

def checkIfInsertion(s1, s2):
    #s1 is the string that's longer
    j = 0
    mismatches = 0
    for i in range(0, len(s2)):
        if s1[i] != s2[j]:
            mismatches += 1
        else:
            j += 1
    

    return mismatches < 2
def main():
    print("Testing pale and ple; expected True")
    print(oneEditAway('pale', 'ple'))
    print("Testing pales and pale; expected True")
    print(oneEditAway('pales', 'pale'))
    print("Testing pale and bale; expected True")
    print(oneEditAway('pale', 'bale'))
    print("Testing pale and bake; expected True")
    print(oneEditAway('pale', 'bake'))

    

main()