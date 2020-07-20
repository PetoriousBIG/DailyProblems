# Problem Descirption:
# Determine if two strings are permutations of eachother

def arePerms(string1, string2):
    if len(string1) != len(string2):
        return False
    
    s1CharCount = {}
    s2CharCount = {}

    for i in range(len(string1)):
        s1Char = string1[i]
        s2Char = string2[i]

        s1CharCount = {}
        s2CharCount = {}

        if s1CharCount.get(s1Char) == None:
            s1CharCount[s1Char] = 0
        else:
            s1CharCount[s1Char] = s1CharCount[s1Char] + 1

        if s2CharCount.get(s2Char) == None:
            s2CharCount[s2Char] = 0
        else:
            s2CharCount[s2Char] = s2CharCount[s2Char] + 1
        
        return s1CharCount == s2CharCount

def main():
    print('Testing with Hello and World, expected false')
    print(arePerms('Hello', 'World'))

    print('Testing with Santa and Satan, expected true')
    print(arePerms('Santa', 'Satan'))

main()