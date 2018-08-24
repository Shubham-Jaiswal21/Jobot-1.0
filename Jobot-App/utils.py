import random


def id_generator():
    rs = (''.join(random.choice(string.ascii_uppercase)
                  for i in range(16)))
    return rs
