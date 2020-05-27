# This is a naive and procedural approach to FizzBuzz.

def fizzbuzz():
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

fizzbuzz()

## Pros: it works, BUT...

## Cons: ...only for this limited use case...
##       ...it's repetetive...