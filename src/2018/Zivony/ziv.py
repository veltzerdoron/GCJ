from fractions import Fraction


class Num:
    def __init__(self, n):
        self.val = n
        self.prio = 9
        self.txt = str(n)

    def combine(self, other, op, new_prio):
        l = self.txt if self.prio > new_prio else "(%s)" % self.txt
        r = other.txt if other.prio > new_prio else "(%s)" % other.txt
        return l + op + r

    def __add__(self, other):
        if self.val == None or other.val == None: return Num(None)
        new = Num(self.val + other.val)
        new.prio = 1
        new.txt = self.combine(other, "+", new.prio)
        return new

    def __sub__(self, other):
        if self.val == None or other.val == None: return Num(None)
        new = Num(self.val - other.val)
        new.prio = 1
        new.txt = self.combine(other, "-", new.prio)
        return new

    def __mul__(self, other):
        if self.val == None or other.val == None: return Num(None)
        new = Num(self.val * other.val)
        new.prio = 2
        new.txt = self.combine(other, "*", new.prio)
        return new

    def __truediv__(self, other):
        if self.val == None or other.val == None: return Num(None)
        if other.val == 0: return Num(None)
        new = Num(Fraction(self.val, other.val))
        new.prio = 2
        new.txt = self.combine(other, "/", new.prio)
        return new

    def __eq__(self, other):
        if isinstance(other, Num): return self.val == other.val
        return self.val == other

    def __str__(self):
        return f"{self.txt} = {self.val}"

    def __hash__(self):
        return (self.val, self.txt).__hash__()

    __repr__ = __str__


def breakup(nums):
    for i, n in enumerate(nums):
        rest = nums[:]
        n = rest.pop(i)
        for j, m in enumerate(rest):
            rest2 = rest[:]
            rest2.pop(j)
            yield rest2 + [n + m]
            yield rest2 + [n * m]
            yield rest2 + [n - m]
            try:
                yield rest2 + [n / m]
            except ZeroDivisionError:
                pass


def find_nums(nums):
    options = [nums]
    while options:
        op = options.pop(0)
        if len(op) == 1:
            yield op[0]
            continue
        for op2 in breakup(op):
            if not op2 in options: options.append(op2)


nums = [1, 2, 2, 1]
for n in set(find_nums([Num(n) for n in nums])):
    # if n!=50: continue
    print(n)
