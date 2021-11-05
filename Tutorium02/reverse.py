import sys
"""
word = sys.argv[1]

n = len(word) - 1
s = ''

while n >= 0:
    s = s + word[n]
    n = n - 1

print(s)
"""










#Für die Profis
"""
words = sys.argv[1:]

def reverse(word):
    n = len(word) - 1
    s = ''

    while n >= 0:
        s = s + word[n]
        n = n - 1

    return s

r_words = []
for word in words:
    r_words.append(reverse(word))

print(r_words)
    
"""














#Oder für die ganz Krassen

#print(sys.argv[1][::-1])
#print([word[::-1] for word in sys.argv[1:]])
