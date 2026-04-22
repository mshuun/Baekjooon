word = input()
words = []
for i in range(1,len(word)-1):
    for j in range(i+1,len(word)):
        word1 = word[0:i]
        word2 = word[i:j]
        word3 = word[j:]
        word1 = word1[::-1]
        word2 = word2[::-1]
        word3 = word3[::-1]
        word4 = word1 + word2 + word3
        words.append(word4)
words.sort()
print(words[0])