class CodeJudge:

    def __init__(self):
        self.s = ""

    def print(self, *values: object):
        s = ""
        for v in values:
            s = s + str(v)

        self.s = self.s + s + "\n"

    def is_equals(self, input):

        return self.s[1:].__eq__(input)

    def get_res(self):
        return self.s