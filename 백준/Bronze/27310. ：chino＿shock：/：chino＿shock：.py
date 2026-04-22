emoji = list(input())
length = len(emoji)
colon = 0
underbar = 0
for i in emoji:
    if i == ':':
        colon += 1
    elif i == '_':
        underbar += 1
difficult = length + colon + underbar*5
print(difficult)