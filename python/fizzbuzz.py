from functools import reduce


def naive_fizzbuzz():
    """
    Prints each integer from 1-100, but instead prints "Fizz" for multiples of three and "Buzz"
    for the multiples of five . For numbers which are multiples of both three and five print "FizzBuzz".

    This is a naive and procedural approach to FizzBuzz.

    Pros: it works, BUT...
    Cons: ...only for this limited use case...
          ...it's repetetive...

    Example call:
    >>> naive_fizzbuzz()
    1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz
    """
    for i in range(1, 100):
        mod3 = (i % 3 == 0)
        mod5 = (i % 5 == 0)

        if mod3 and (not mod5):
            print('Fizz', end=" ")
        elif mod5 and (not mod3):
            print('Buzz', end=" ")
        elif mod3 and mod5:
            print('FizzBuzz', end=" ")
        else:
            print(i, end=" ")


def improved_naive_fizzbuzz():
    """
    Prints each integer from 1-100, but instead prints "Fizz" for multiples of three and "Buzz"
    for the multiples of five . For numbers which are multiples of both three and five print "FizzBuzz".

    This is an improved, but still naive and procedural approach to FizzBuzz.

    Pros: it works, BUT...
    Cons: ...still only for this limited use case...
          ...it's still repetitive...

    Example call:
    >>> improved_naive_fizzbuzz()
    """

    fizz = 'fizz'
    buzz = 'buzz'

    def divisible_by(numerator, denominator):
        return numerator % denominator == 0

    for i in range(1, 100):
        mod3 = divisible_by(i, 3)
        mod5 = divisible_by(i, 5)

        if mod3 and (not mod5):
            print(fizz, end=" ")
        elif mod5 and (not mod3):
            print(buzz, end=" ")
        elif mod3 and mod5:
            print(fizz + buzz, end=" ")
        else:
            print(i, end=" ")


def parameterized_fizzbuzz(rng: list, triggers: list):
    """
    Prints each element in rng except where the conditions in list are triggered and the text associated
    with that trigger is printed.

    This is a parameterized, and still procedural, approach to FizzBuzz.

    Pros: less repetitive and more flexible
    Cons: The loop might not be the most efficient approach...

    Example call:
    >>> parameterized_fizzbuzz(range(1, 16), [
    ... ('Fizz', lambda i: i % 3 == 0),
    ... ('Buzz', lambda i: i % 5 == 0)
    ... ])
    1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz

    :param rng: a list
    :param triggers: a list of tuples of text to print and lambda function of condition that triggers text
    :return: None
    """
    for i in rng:
        result = ''
        for text, trigger in triggers:
            if trigger(i):
                result += text
        print(result or i, end = " ")


def simple_fp_fizzbuzz(rng: list, triggers: list) -> list:
    """
    Returns a list of elements in rng except where elements are replaced based on conditions in triggers.

    This version takes a functional programming approach. The loop from previous versions is replaced with a call to map.

    Example call:
    >>> simple_fp_fizzbuzz(range(10, 16), [
    ... ('Fizz', lambda i: i % 3 == 0),
    ... ('Buzz', lambda i: i % 5 == 0)
    ... ])
    ['Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']

    :param rng: a list
    :param triggers: a list of tuples containing an object and a boolean lambda function
    :return: list
    """
    def evaluate(i):
        result = ''
        for (text, predicate) in triggers:
            if predicate(i):
                result += text
        return result or i

    return list(map(evaluate, rng))


def complex_fp_fizzbuzz(rng: list, triggers: list) -> list:
    """
    Returns a list of elements in rng except where elements are replaced based on conditions in triggers.

    This version takes a strict functional programming approach.

    Pros: it works
          it's concsise
    Cons: it's difficult to understand
          it's overengineered (YAGNI)

    Example call:
    >>> complex_fp_fizzbuzz(range(10, 16), [
    ... {'text' : 'Fizz', 'trigger' : lambda i: i % 3 == 0},
    ... {'text' : 'Buzz', 'trigger' : lambda i: i % 5 == 0}
    ... ])
    ['Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']

    :param rng: a list
    :param triggers: a list of tuples containing an object and a boolean lambda function
    :return: list
    """
    # return text if trigger is true; if none are true, return i
    def evaluate(i):
        # filter triggers to those that evaluate to true
        parts = list(filter((lambda j: j['trigger'](i)), triggers))
        # return combined text of true triggers if parts is not empty, otherwise return i
        return reduce(lambda x, y: x + y, map(lambda part: part['text'], parts)) if parts else i

    # map evaluate to every element in rng
    return list(map(evaluate, rng))



def lazy_gen_fizzbuzz(start: int=1, end: int=16, triggers: list=[]):
    """
    This will be an approach that uses functional programming and lazy generation (i.e., enumerators/generators).

    Usage:
    >>> for x in lazy_gen_fizzbuzz(triggers=[
    ...     {'text' : 'Fizz', 'trigger' : lambda i: i % 3 == 0},
    ...     {'text' : 'Buzz', 'trigger' : lambda i: i % 5 == 0}
    ...     ]):
    ...     print(x, end=" ")
    1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz
    """

    i = start
    while i < end:
        # filter triggers to those that evaluate to true
        parts = list(filter((lambda j: j['trigger'](i)), triggers))
        # return combined text of true triggers if parts is not empty, otherwise return i
        yield reduce(lambda x, y: x + y, map(lambda part: part['text'], parts)) if parts else i
        i += 1

