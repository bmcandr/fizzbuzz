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
    """
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
            print(fizz)
        elif mod5 and (not mod3):
            print(buzz)
        elif mod3 and mod5:
            print(fizz + buzz)
        else:
            print(i)


def parameterized_fizzbuzz(rng: list, triggers: list):
    """
    Prints each element in rng except where the conditions in list are triggered and the text associated
    with that trigger is printed.

    This is a parameterized, and still procedural, approach to FizzBuzz.

    Pros: less repetitive and more flexible
    Cons: The loop might not be the most efficient approach...

    Example call:
    >>> parameterized_fizzbuzz(range(10, 16), [
    ... ('Fizz', lambda i: i % 3 == 0),
    ... ('Buzz', lambda i: i % 5 == 0)
    ... ])
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz

    :param rng: a list
    :param triggers: a list of tuples of text to print and lambda function of condition that triggers text
    :return: None
    """
    for i in rng:
        result = ''
        for text, trigger in triggers:
            if trigger(i):
                result += text
        print(result or i)


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


# This will be an approach that uses functional programming and lazy generation (i.e., enumerators/generators).

# def lazy_gen_fizzbuzz(rng: list, triggers: list) -> list:
#     # A project for another day...
#     return []
