def is_similar(word1, word2):
    if abs(len(word1) - len(word2)) > 1:return False
    if len(word1) == len(word2):
        diff_count = sum(1 for a, b in zip(word1, word2) if a != b)
        if diff_count == 0:
            return True
        elif diff_count == 1:
            return True
        elif diff_count == 2:
            indices = [i for i, (a, b) in enumerate(zip(word1, word2)) if a != b]
            if len(indices) == 2 and word1[indices[0]] == word2[indices[1]] and word1[indices[1]] == word2[indices[0]]:
                return True
    if len(word1) > len(word2):word1, word2 = word2, word1  
    for i in range(len(word2)):
        if word2[:i] + word2[i+1:] == word1:return True
    return False

n = int(input())
dictionary = [input() for _ in range(n)]
q = int(input())
for _ in range(q):
    word = input().strip()
    if word in dictionary:
        print(f"{word} is correct")
    else:
        found_similar = False
        for dict_word in dictionary:
            if is_similar(word, dict_word):
                print(f"{word} is a misspelling of {dict_word}")
                found_similar = True
                break
        if not found_similar:
            print(f"{word} is unknown")

