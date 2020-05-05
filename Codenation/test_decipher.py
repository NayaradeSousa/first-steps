import unittest

from JulioCesarCryptography import decipher_cod


class TestDecipher(unittest.TestCase):

    def test_decipher(self):
        response = decipher_cod(3, "d oljhlud udsrvd pduurp vdowrx vreuh r fdfkruur fdqvdgr")
        self.assertEquals("a ligeira raposa marrom saltou sobre o cachorro cansado", response)

    def test_decipher2(self):
        response = decipher_cod(1,"po uif joufsofu, opcpez lopxt zpv bsf b eph. 1qfufs tufjofs")
        self.assertEquals("on the internet, nobody knows you are a dog. 1peter steiner", response)