# This is an improved, but still naive and procedural approach to FizzBuzz.

fizz = 'fizz'
buzz = 'buzz'

def fizzbuzz():

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

fizzbuzz()

## Pros: it works, BUT...

## Cons: ...still only for this limited use case...
##       ...it's still repetetive...