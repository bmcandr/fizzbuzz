from functools import reduce


# This is a naive and procedural approach to FizzBuzz.
# Pros: it works, BUT...
# Cons: ...only for this limited use case...
#       ...it's repetetive...
#
# Example call:
# naive_fizzbuzz()


def naive_fizzbuzz():
    for i in range(1, 100):
        mod3 = (i % 3 == 0)
        mod5 = (i % 5 == 0)

        if mod3 and (not mod5):
            print('Fizz')
        elif mod5 and (not mod3):
            print('Buzz')
        elif mod3 and mod5:
            print('FizzBuzz')
        else:
            print(i)

# This is an improved, but still naive and procedural approach to FizzBuzz.
# Pros: it works, BUT...
# Cons: ...still only for this limited use case...
#       ...it's still repetitive...
#
# Example call:
# improved_naive_fizzbuzz()


def improved_naive_fizzbuzz():
    fizz = 'fizz'
    buzz = 'buzz'

    def divisible_by(numerator, denominator):
        return numerator % denominator == 0

    for i in range(1, 100):
        mod3 = divisible_by(i, 3)
        mod5 = divisible_by(i, 5)

        if mod3 and (not mod5):
            print(fizz)
        elif mod5 and (not mod3):
            print(buzz)
        elif mod3 and mod5:
            print(fizz + buzz)
        else:
            print(i)


# This is a parameterized, and still procedural, approach to FizzBuzz.
# Pros: less repetitive and more flexible
# Cons: The loop might not be the most efficient approach...

# Example call:
# parameterized_fizzbuzz(range(1, 100),[
#     ('Fizz', lambda i: i % 3 == 0),
#     ('Buzz', lambda i: i % 5 == 0)
# ])


def parameterized_fizzbuzz(rng: list, triggers: list):
    for i in rng:
        result = ''
        for text, trigger in triggers:
            if trigger(i):
                result += text
        print(result or i)


# This version takes a functional programming approach. The loop from previous versions is replaced with a call to map.

# Example call:
# simple_fp_fizzbuzz(range(1, 100), [
#     ('Fizz', lambda i: i % 3 == 0),
#     ('Buzz', lambda i: i % 5 == 0)
# ])

def simple_fp_fizzbuzz(rng: list, triggers: list) -> list:
    def evaluate(i):
        result = ''
        for (text, predicate) in triggers:
            if predicate(i):
                result += text
        return result or i

    print(list(map(evaluate, rng)))


# This version takes a, probably unnecessarily, strict functional programming approach.
# Pros: it works
#       it's concsise
# Cons: it's difficult to understand
#       it's overengineered (YAGNI)

# Example call:
# complex_fp_fizzbuzz(range(1, 100), [
#     {'text' : 'Fizz', 'trigger' : lambda i: i % 3 == 0},
#     {'text' : 'Buzz', 'trigger' : lambda i: i % 5 == 0}
# ])

def complex_fp_fizzbuzz(rng: list, triggers: list) -> list:

    # return text if trigger is true; if none are true, return i
    def evaluate(i):
        # filter triggers to those that evaluate to true
        parts = list(filter((lambda j: j['trigger'](i)), triggers))
        # return combined text of true triggers if parts is not empty, otherwise return i
        return reduce(lambda x, y: x + y, map(lambda part: part['text'], parts)) if parts else i

    # map evaluate to every element in rng
    return list(map(evaluate, rng))


# This will be an approach that uses functional programming and lazy generation (i.e., enumerators/generators).

def lazy_gen_fizzbuzz(rng: list, triggers: list) -> list:
    # A project for another day...
    return []
