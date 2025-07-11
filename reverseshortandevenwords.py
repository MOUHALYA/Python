def reverse_short_words(text):
    """Reverses words with 4 or fewer letters in a string, excluding longer words."""
    words = text.split()
    reversed_words = []
    for word in words:
        if len(word) <= 4:
            reversed_words.append(word[::-1])  # Reverse using slicing
    return " ".join(reversed_words)

s = "i am python code"
r = reverse_short_words(s)
print(r)




def reverse_even_words(text):
    """Reverses even-length words in a string, excluding others."""
    words = text.split()
    reversed_words = []
    for word in words:
        if len(word) % 2 == 0:
            reversed_words.append(word[::-1])
    return " ".join(reversed_words)

s = "i will try python code"
r = reverse_even_words(s)
print(r)
