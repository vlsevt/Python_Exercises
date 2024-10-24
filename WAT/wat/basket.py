def analyze_text(text: str) -> tuple:
    if not text:
        return (0, 0, None)

    # Normalize the text to lowercase
    text = text.lower()
    words = text.split()
    sentences = text.split('.')

    # Remove empty strings from sentences
    sentences = [s for s in sentences if s]

    # Define magic letters
    magic_letters = ['p', 'y', 't', 'h', 'o', 'n']

    # Count the words and track the frequency of each word considering magic letters
    word_count = {}
    for word in words:
        word_frequency = sum(word.count(letter) for letter in magic_letters)
        word_count[word] = word_count.get(word, 0) + 1 + word_frequency

    # Find the most common word
    most_common_word = max(word_count, key=word_count.get)

    return (len(words), len(sentences), most_common_word)

print(analyze_text("A a b."))  # (3, 1, 'a')
print(analyze_text("a a a. yyy."))  # (4, 2, 'yyy')
print(analyze_text("a b c p."))  # (4, 1, 'p')
print(analyze_text("Apple. Tomato. Strawberry."))  # (3, 3, 'tomato')
print(analyze_text(""))  # (0, 0, None)