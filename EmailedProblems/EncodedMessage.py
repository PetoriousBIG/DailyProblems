# Problem Descirption:
# 
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '123' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# 
# You can assume that the messages are decodable. For example, '001' is not allowed.


# Dynamic Programming Solution

def buildMap():
    theMap = {}
    asciiNum = 97
    i = 1
    for i in range(1, 27):
        theMap[str(i)] = chr(asciiNum)
        asciiNum += 1

    return theMap

def findPossibleEncodedMessageOutputs(message):
    
    encodingMap = buildMap()
    possibilitiesForFirstNChars = [[encodingMap[message[0]]]]
    
    for i in range(1, len(message)):
        
        thisSubProblemResults = []
        charToDecode = message[i]
        lastNCharsRes = possibilitiesForFirstNChars[-1]

        for choice in lastNCharsRes:
            concat = choice + encodingMap[charToDecode]
            thisSubProblemResults.append(concat)

            key = str(ord(choice[-1]) - 96) + charToDecode

            if key in encodingMap:
                otherPossiblity = choice + encodingMap[key]
                thisSubProblemResults.append(otherPossiblity)

        possibilitiesForFirstNChars.append(thisSubProblemResults)

    return [possibilitiesForFirstNChars[-1]]

        
def main():
    print("Testing with '111', expected output: 3 - ['aaa', 'ka', 'ak']")
    print(findPossibleEncodedMessageOutputs("111"))
    print("Testing with '123', expected output: 3 - ['abc', 'w', 'lc']")
    print(findPossibleEncodedMessageOutputs("123"))
    print("Testing with '576321198', ")
    print(findPossibleEncodedMessageOutputs("576321198"))

main()