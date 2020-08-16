# Given a string you need to print longest possible substring that has exactly k unique characters. 
# If there are more than one substring of longest possible length, then print any one of them.

# Examples:
# "aabbcc", k = 1
# Max substring can be any one from {"aa" , "bb" , "cc"}.

# "aabbcc", k = 2
# Max substring can be any one from {"aabb" , "bbcc"}.

# "aabbcc", k = 3
# There are substrings with exactly 3 unique characters
# {"aabbcc" , "abbcc" , "aabbc" , "abbc" }
# Max is "aabbcc" with length 6.

# "aaabbb", k = 3
# There are only two unique characters, thus show error message. 

def LongestSubStringSizeKDictChars(s, k):
    ans = ''
    subS = ans
    leftIndex = 0
    lastOccurenceOfChar = {}
    uniqueCount = 0


    for rightIndex in range(0, len(s)):
        nextChar = s[rightIndex]
        if nextChar in lastOccurenceOfChar:
            lastOccurenceOfChar[nextChar] = rightIndex
            subS += nextChar
        
        else:
            uniqueCount += 1
            lastOccurenceOfChar[nextChar] = rightIndex
            subS += nextChar
            while(uniqueCount > k):
                backChar = s[leftIndex]
                if leftIndex == lastOccurenceOfChar[backChar]:
                    uniqueCount -= 1 
                    del lastOccurenceOfChar[backChar]
                leftIndex += 1
                subS = s[leftIndex:rightIndex]

        
        if len(subS) > len(ans):
            ans = subS

    if uniqueCount != k:
        return 'Error'
    return ans

def main():
    print("Testing 'aabbcc', k = 1. Expected output is 'aa'")
    print(str(LongestSubStringSizeKDictChars('aabbcc', 1)))

    print("Testing 'aabbcc', k = 2. Expected output is 'aabb'")
    print(str(LongestSubStringSizeKDictChars('aabbcc', 2)))

    print("Testing 'aabbcc', k = 3. Expected output is 'aabbcc'")
    print(str(LongestSubStringSizeKDictChars('aabbcc', 3)))

    print("Testing 'aaabbb', k = 3. Expected output is 'Error'")
    print(str(LongestSubStringSizeKDictChars('aaabbb', 3)))

main()