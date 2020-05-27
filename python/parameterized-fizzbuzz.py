# This is a parameterized, and still procedural, approach to FizzBuzz.

def fizzbuzz(rng: list, triggers: list):
    for i in rng:
        result = ''
        for text, trigger in triggers:
            if trigger(i):
                result += text
        print(result or i)

fizzbuzz(range(1, 100),[
    ('Fizz', lambda i: i % 3 == 0),
    ('Buzz', lambda i: i % 5 == 0)
])

## Pros: less repetitive and more flexible
## Cons: The loop might not be the most efficient approach...