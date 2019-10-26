import random

class Rand:

    def num(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)

        return first, second

obj1 = Rand()
print(obj1.num())