def mergeAlternately(self, word1, word2):
    str1 = ""
    for i, j in zip(word1, word2):
        str1 += i
        str1 += j
    str1 += word2[len(word1):] if len(word2) > len(word1) else word1[len(word2):]
    return str1
