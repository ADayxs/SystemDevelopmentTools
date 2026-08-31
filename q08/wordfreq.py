words = open("words.txt", encoding="utf-8").read().split()
unique = []
seen = set()
for word in words:
    if word not in seen:
        aeen.add(word)
        unique.append(word)
print("count =", len(unique))
