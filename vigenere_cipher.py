import math


class VigenereCipher(object):
    """Шифр Виженера"""

    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.len_of_alph = len(alphabet)
        self.tabl = self.enter_tabl([[0] * self.len_of_alph for i in range(self.len_of_alph)])

    def allign(self, key, string):
        res = list(key)
        if len(res) > len(string):
            return res[0:len(string)]
        elif len(res) < len(string):
            num = math.ceil((len(string) - len(res)) / len(res))
            res += res * int(num)
            for i in range(len(string)):
                if not string[i].isalpha():
                    res.insert(i, ' ')
            res = ''.join(res)
            return res[0:len(string)]
        else:
            return res

    def shift(self, k):
        lst = list(self.alphabet)
        for _ in range(k):
            last = lst.pop(0)
            lst.append(last)
        return lst

    def enter_tabl(self, tabl):
        for i in range(self.len_of_alph):
            mas = self.shift(i)
            for j in range(self.len_of_alph):
                tabl[i][j] = mas[j]
        return tabl

    def encode(self, string):
        # string = ''.join(string.split())
        if (self.alphabet[0].islower()):
            num = 97
        else:
            num = 65
        # res = ""
        res = []
        count = []

        for j in range(len(string)):
            if string[j] == ' ':
                count.append(j)

        string = ''.join(string.split())

        self.key = self.allign(self.key, string)  # выравниваем ключ

        for i in range(len(string)):
            if string[i].isalpha():
                var = self.tabl[ord(string[i]) - num][ord(self.key[i]) - num]
                res += (str(var))
            else:
                res += string[i]
        for j in count:
            res.insert(j, ' ')
        return ''.join(res)

    def decode(self, string):
        count = []

        for j in range(len(string)):
            if string[j] == ' ':
                count.append(j)

        string = ''.join(string.split())

        if (self.alphabet[0].islower()):
            num = 97
        else:
            num = 65
        res = []

        self.key = self.allign(self.key, string)  # выравниваем ключ
        for i in range(len(string)):
            for j in range(self.len_of_alph):
                if string[i].isalpha():
                    if self.tabl[ord(self.key[i]) - num][j] == string[i]:
                        res += (chr(j + num))
                        break
                else:
                    res += string[i]
                    break

        for j in count:
            res.insert(j, ' ')
        return ''.join(res)


a = VigenereCipher("asdq", "abcdefghijklmnopqrstuvwxyz")

print(a.encode('coding'))
print(a.decode('cggyny'))
