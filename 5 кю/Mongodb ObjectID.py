from datetime import datetime


class Mongo(object):

    @classmethod
    def is_valid(self, s):
        hexdigits = set("0123456789abcdef")
        return isinstance(s, str) and len(s) == 24 and all(char in hexdigits for char in s)

    @classmethod
    def get_timestamp(self, s):
        if not self.is_valid(s):
            return False
        return datetime.fromtimestamp(int(s[0:8], 16))
