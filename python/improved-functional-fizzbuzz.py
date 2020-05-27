# This version takes a, probably unnecessarily, strict functional programming approach.

from functools import reduce


def fizzbuzz(rng: list, triggers: list) -> list:

    # return text if trigger is true; if none are true, return i
    def evaluate(i):
        # filter triggers to those that evaluate to true
        parts = list(filter((lambda j: j['trigger'](i)), triggers))
        # return combined text of true triggers if parts is not empty, otherwise return i
        return reduce(lambda x, y: x + y, map(lambda part: part['text'], parts)) if parts else i

    # map evaluate to every element in rng
    return list(map(evaluate, rng))


result = fizzbuzz(range(1, 100), [
    {'text' : 'Fizz', 'trigger' : lambda i: i % 3 == 0},
    {'text' : 'Buzz', 'trigger' : lambda i: i % 5 == 0}
])

print(result)

## Pros: it works, it's concsise
## Cons: it's difficult to understand
##       it's overengineered (YAGNI)