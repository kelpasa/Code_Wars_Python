'''
Oh no! You have stumbled upon a mysterious signal consisting of beeps of various lengths, and it is of utmost importance that you find out the secret message hidden in the beeps. There are long and short beeps, the longer ones roughly three times as long as the shorter ones. Hmm... that sounds familiar.

That's right: your job is to implement a decoder for the Morse alphabet. Rather than dealing with actual beeps, we will use a common string encoding of Morse. A long beep is represened by a dash (-) and a short beep by a dot (.). A series of long and short beeps make up a letter, and letters are separated by spaces (). Words are separated by double spaces.

You should implement the International Morse Alphabet. You need to support letters a-z and digits 0-9 as follows:
'''

def decode(s):
    if s == '':
        return ''
    else:
        conener = {
            '.-':'a',
            '-...':'b',
            '-.-.':'c',
            '-..':'d',
            '.':'e',
            '..-.':'f',
            '--.':'g',
            '....':'h',
            '..':'i',
            '.---':'j',
            '-.-':'k',
            '.-..':'l',
            '--':'m',
            '-.':'n',
            '---':'o',
            '.--.':'p',
            '--.-':'q',
            '.-.':'r',
            '...':'s',
            '-':'t',
            '..-':'u',
            '...-':'v',
            '.--':'w',
            '-.--':'y',
            '--..':'z',
            '': ' ',
            '.----':'1',
            '..---':'2',
            '...--':'3',
            '....-':'4',
            '.....':'5',
            '-....':'6',
            '--...':'7',
            '---..':'8',
            '----.':'9',
            '-----':'0',
            '-..-':'x'
        }
        lst = []
        for i in s.split(' '):
            lst.append(conener[i])
        return ''.join(lst)
