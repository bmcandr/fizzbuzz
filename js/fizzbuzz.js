// Methods to implement:

/* naive_fizzbuzz

Prints each integer from 1-100, but instead prints "Fizz" for multiples of three and "Buzz"
for the multiples of five . For numbers which are multiples of both three and five print "FizzBuzz".

This is a naive and procedural approach to FizzBuzz.

Pros: it works, BUT...
Cons: ...only for this limited use case...
    ...it's repetitive...

Usage:
> naive_fizzbuzz()
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz 
*/

function naive_fizzbuzz() {
  for (var i = 1; i < 100; i++) {
    var mod3 = i % 3 == 0;
    var mod5 = i % 5 == 0;

    if (mod3 && !mod5) {
      console.log("Fizz");
    } else if (mod5 && !mod3) {
      console.log("Buzz");
    } else if (mod3 && mod5) {
      console.log("FizzBuzz");
    } else {
      console.log(i);
    }
  }
}

// naive_fizzbuzz();

// improved_naive_fizzbuzz

function improved_naive_fizzbuzz() {
  var fizz = "Fizz";
  var buzz = "Buzz";

  function divisible_by(numerator, denominator) {
    return numerator % denominator == 0;
  }

  for (var i = 1; i < 100; i++) {
    var mod3 = divisible_by(i, 3);
    var mod5 = divisible_by(i, 5);

    if (mod3 && !mod5) {
      console.log(fizz);
    } else if (mod5 && !mod3) {
      console.log(buzz);
    } else if (mod3 && mod5) {
      console.log(fizz + buzz);
    } else {
      console.log(i);
    }
  }
}

improved_naive_fizzbuzz();
// parameterized_fizzbuzz
// simple_fp_fizzbuzz
// complex_fp_fizzbuzz
// lazy generation
