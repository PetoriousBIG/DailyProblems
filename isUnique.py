# Problem Descirption:
# Determine if a string contains at most one instance of a given character

def isUnique(string):
    charList = []
    for char in string:
        if char in charList:
            return False
        else:
            charList.append(char)
    return True

def main():
    print('Test String: Hello World, Expected False')
    print(isUnique('Hello World'))

    print('Test String: abc123, Expected True')
    print(isUnique('abc123'))

main()