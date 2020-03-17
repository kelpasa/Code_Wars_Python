'''
The Earth has been invaded by aliens. They demand our beer and threaten to destroy the Earth if we do not supply the exact number of beers demanded.

Unfortunately, the aliens only speak Morse code. Write a program to convert morse code into numbers using the following convention:

1 .---- 2 ..--- 3 ...-- 4 ....- 5 ..... 6 -.... 7 --... 8 ---.. 9 ----. 0 -----
'''
def gropers(s):
    agrs = [iter(s)]*5
    return zip(*agrs)

def morse_converter(string):
    args = [''.join(i) for i in gropers(string)]
    contener ={
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '-----': '0'
    }
    new_str = ''
    for i in args:
        new_str +=contener[i]
    return int(new_str)
