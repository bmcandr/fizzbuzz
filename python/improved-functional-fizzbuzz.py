# This version takes a functional programming approach. The loop from previous versions is replaced with a call to map.

from functools import reduce


def fizzbuzz(rng: list, triggers: list) -> list:

    def evaluate(i):
        parts = list(filter((lambda j: j['trigger'](i)), triggers))
        return reduce(lambda x, y: x + y, map(lambda part: part['text'], parts)) if parts else i

    return list(map(evaluate, rng))


result = fizzbuzz(range(1, 100), [
    {'text' : 'Fizz', 'trigger' : lambda i: i % 3 == 0},
    {'text' : 'Buzz', 'trigger' : lambda i: i % 5 == 0},
])

print(result)