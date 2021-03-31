from typing import Optional
import string
from .data import data, helper

class CaesarCipher:
    def __init__(self, shift: Optional[int] = 3, message: string = ''):
        self.shift = shift
        self.message = message
        self.unranks = helper.unrank_symbols()

    def check_input_message(self):
        try:
            for char in self.message:
                if char not in data.ALLOWED_SYMBOLS:
                    raise Exception('InputOutOfRange')
                else:
                    pass
        except Exception as e:
            print(type(e), e.args)
    def check_input_shift(self):
        try:
                if self.shift < 1:
                    raise Exception('InputOutOfRange')
                else:
                    pass
        except Exception as e:
            print(type(e), e.args)

    def encrypt(self):
        encrypted = ''
        self.check_input_message().check_input_shift()
        for char in range(len(self.message)):
            index = helper.find_rank(char, self.unranks) + self.shift
            encrypted += self.unranks[index]
        return encrypted

    def decrypt(self):
        decrypted = ''
        self.check_input_message().check_input_shift()
        for char in range(len(self.message)):
            index = helper.find_rank(char, self.unranks) - self.shift
            decrypted += self.unranks[index]
        return decrypted