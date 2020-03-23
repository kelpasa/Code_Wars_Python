'''
 word is defined as a sequence of ASCII characters between two white space characters or the first or last word of a sequence of words.

Each word will represent a hexadecimal value by taking the first three letters of each word and find the ASCII character code for each character. This will then give you one hexadecimal value that represents the colours red, green or blue. You will then combine these values into one readable RGB hexadecimal value, ie, #ffffff.

If your word consists of less than 3 letters, you should use the hexidecimal value '00', ie "It" would return a value #497400.

Your answer should be an array of hexadecimal values that correspond to each word that made up your original string.

Example:

The following string would be given:

"Hello, my name is Gary and I like cheese."

This string would return the following array:

['#48656c', '#6d7900', '#6e616d','#697300','#476172','#616e64','#490000','#6c696b','#636865']
'''
import itertools

def words_to_hex(words):

    words = [x[:3] for x in words.split()]
    words = [list(i) for i in words]
    lst = []
    for i in range(len(words)):
        if len(words[i]) == 2:
            words[i] += [0]
        elif len(words[i]) == 1:
            words[i] += [0, 0]
        for j in words[i]:
            try:
                lst.append(hex(ord(j)).replace('0x',''))
            except TypeError:
                lst.append(hex(j).replace('0x', '')+'0')
    lst = list(x for x in itertools.zip_longest(*[iter(lst)]*3))
    new = []
    for i in range(len(lst)):
        new.append('#' + ''.join(lst[i]))
    return new
