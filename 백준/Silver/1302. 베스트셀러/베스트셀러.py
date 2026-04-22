n = int(input())
books = dict()
for i in range(n):
    title = input()
    if title in books:
        books[title] += 1
    else:
        books[title] = 1
max_books = max(books.values())
max_title = []
for title, count in books.items():
    if count == max_books:
        max_title.append(title)
print(sorted(max_title)[0])