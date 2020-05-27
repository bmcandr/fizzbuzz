# This is a parameterized, and still procedural, approach to FizzBuzz.

def fizzbuzz(rng: list, triggers):
    
    for i in rng:
        result = ''
        for text, trigger in triggers:
            if i % trigger == 0:
                result += text
        print(result or i)

fizzbuzz(range(1, 100),[
    ('Fizz', 3),
    ('Buzz', 5)
])