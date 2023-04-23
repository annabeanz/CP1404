"""
Word Occurrences
Estimate: 40 minutes
Actual:   23 minutes
"""


def main():
    """A program that takes a sentence and returns how many times each word is used"""
    user_sentence = str(input("Write your text here:"))
    extracted_words = get_words(user_sentence)
    count = word_count(extracted_words)
    longest_word_length = get_longest_word(count.keys())
    print(f"Text: {user_sentence}")
    for word, num_count in count.items():
        print(f"{word:<{longest_word_length}} : {num_count}")


def word_count(word_list):
    """Tracks the occurrences of all the words in a dictionary"""
    words_to_count = {}
    for word in word_list:
        words_to_count[word] = words_to_count.get(word, 0) + 1
    return words_to_count


def get_words(sentence):
    """Extracts only the words from a string, removes all while spaces or duplicate spacings"""
    words = sentence.split(" ")
    while " " in words or '' in words:
        if ' ' in words:
            words.remove(' ')
        if '' in words:
            words.remove('')
    words.sort()
    return words


def get_longest_word(words):
    "Gets the length of the longest word and returns it as an integer"
    longest_word = 0
    for word in words:
        if len(word) > longest_word:
            longest_word = len(word)
    return longest_word


main()
