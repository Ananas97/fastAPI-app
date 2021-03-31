from typing import Optional
import string

''' Implemented Caesar Cipher'''


class CaesarCipher:
    def __init__(self, shift: Optional[int] = 3, message: string = ''):
        self.shift = shift
        self.message = message
        self.unranks = unrank_symbols()

    '''Check whether message public field is within range of accepted input'''

    def check_input_message(self):
        try:
            for char in self.message:
                if char not in ALLOWED_SYMBOLS:
                    raise Exception('InputOutOfRange')
                else:
                    pass
        except Exception as e:
            print(type(e), e.args)
        finally:
            return self

    '''Check whether shift public field is within range of accepted input'''

    def check_input_shift(self):
        try:
            if self.shift < 1:
                raise Exception('InputOutOfRange')
            else:
                pass
        except Exception as e:
            print(type(e), e.args)
        finally:
            return self

    '''Encrypt method for Caesar cipher'''

    def encrypt(self):
        encrypted = ''
        self.check_input_message().check_input_shift()
        for char in self.message:
            index = self.unranks.index(char)
            index = index + self.shift
            encrypted = encrypted + self.unranks[index]
        return encrypted

    '''Decrypt method for Caesar cipher'''

    def decrypt(self):
        decrypted = ''
        self.check_input_message() \
            .check_input_shift()
        for char in self.message:
            index = self.unranks.index(char) - self.shift
            decrypted = decrypted + self.unranks[index]
        return decrypted


'''below constants fro allowed symbols and temp lists for decoded ASCII chars'''
ALLOWED_PUNCTUATION = string.punctuation
ALLOWED_WHITESPACE = string.whitespace
ALLOWED_LATIN_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALLOWED_LATIN_LOWER = ALLOWED_LATIN_UPPER.lower()

ALLOWED_SYMBOLS = ALLOWED_PUNCTUATION + ALLOWED_WHITESPACE + ALLOWED_LATIN_UPPER + ALLOWED_LATIN_LOWER

ranks = []
unranks = []

'''Helper Function to have ranked(with ASCII codes) list of expected symbols'''


def rank_symbols():
    for symbol in ALLOWED_SYMBOLS:
        ranks.append(ord(symbol))
    ranks.sort()
    return ranks


'''Function to have unranked(without ASCII codes) list of expected symbols'''


def unrank_symbols():
    ranks = rank_symbols()
    for rank in ranks:
        unranks.append(chr(rank))
    return unranks


'''Function to find rank of char in a list'''


def find_rank(char, list):
    rank = 0
    for l in list:
        if char == l:
            rank = list.index(l)
    return rank


'''Uncomment a below code block yo test how encrypt method works'''
# if __name__ == "__main__":
#     cipher = CaesarCipher(3, 'akaLJHGHmar')
#     print(cipher.encrypt())
