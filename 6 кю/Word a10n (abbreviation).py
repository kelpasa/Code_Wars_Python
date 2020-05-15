'''
The word i18n is a common abbreviation of internationalization in the developer community, used instead of typing the whole word and trying to spell it correctly. Similarly, a11y is an abbreviation of accessibility.

Write a function that takes a string and turns any and all "words" (see below) within that string of length 4 or greater into an abbreviation, following these rules:

A "word" is a sequence of alphabetical characters. By this definition, any other character like a space or hyphen (eg. "elephant-ride") will split up a series of letters into two words (eg. "elephant" and "ride").
The abbreviated version of the word should have the first letter, then the number of removed characters, then the last letter (eg. "elephant ride" => "e6t r2e").
'''


def abbreviate(s):
    word = ''
    sentence = []
    output = []
    for character in s:
        if character.isalpha():
            word = word + character
        else:
            sentence.append(word)
            sentence.append(character)
            word = ''
    sentence.append(word)
    for word in sentence:
        l = len(word)
        if l > 3:
            a10n = word[0] + str(l - 2) + word[l - 1]
            output.append(a10n)
        else:
            output.append(word)
    output = ''.join(output)
    return output
