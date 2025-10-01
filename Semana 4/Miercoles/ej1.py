def find_words(words):
    keyboard_1 = "qwertyuiop"
    keyboard_2 = "asdfghjkl"
    keyboard_3 = "zxcvbnm"
    final_words = []
    for word in words:
        word_is_valid_1 = True
        word_is_valid_2 = True
        word_is_valid_3 = True
        for letter in word.lower():
            if letter not in keyboard_1:
                word_is_valid_1 = False
            
            if letter not in keyboard_2:
                word_is_valid_2 = False
            
            if letter not in keyboard_3:
                word_is_valid_3 = False

        if word_is_valid_1 or word_is_valid_2 or word_is_valid_3:
            final_words.append(word)
    return final_words

result = find_words(["Hello", "Alaska", "Dad", "Peace"])
print(result)