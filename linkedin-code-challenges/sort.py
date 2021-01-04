def sort_words(input):
    words = input.split()
    return sorted(words, key=str.lower)