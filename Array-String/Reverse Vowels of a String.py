def reverseVowels(self, s: str) -> str:
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    temp = [char for char in s if char in vowels]
    s = list(s)
    s = [temp.pop() if char in vowels else char for char in s]
    s = ''.join(s)
    return s
