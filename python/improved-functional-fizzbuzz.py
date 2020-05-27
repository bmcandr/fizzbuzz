# This version takes a functional programming approach. The loop from previous versions is replaced with a call to map.

def fizzbuzz(rng: list, triggers: list) -> list:
    def evaluate(i):
        result = ''
        for (text, predicate) in triggers:
            if predicate(i):
                result += text
        return result or i
  
    print(list(map(evaluate, rng)))



fizzbuzz(range(1, 100), [
    ('Fizz', lambda i: i % 3 == 0),
    ('Buzz', lambda i: i % 5 == 0)
])