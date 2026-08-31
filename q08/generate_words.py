import random
random.seed(20260831)
vocab = [f"w{i}" for i in range(1000)]
with open("words.txt", "w", encoding="utf-8") as f:
    for _ in range(30000):
        f.write(random.choice(vocab))
        f.write(" ")
