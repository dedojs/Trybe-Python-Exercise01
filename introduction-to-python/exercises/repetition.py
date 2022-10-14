def append_each_letter_of_the_word_in_a_list(word):
    result = []

    for letter in word:
        result.append(letter)

    return result


def return_index_of_the_uppercase_letter(word):
    result = -1

    for letter in word:
        if letter.isupper():
            result = word.index(letter)
    return result


def return_element_from_list_that_is_string(input_list):
    result = []

    for string in input_list:
        if isinstance(string, str):
            result.append(string)
    return result[0]
