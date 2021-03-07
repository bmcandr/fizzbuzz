#include <stdio.h>
#include <string.h>

void simple_fizzbuzz();

int main() {
    void simple_fizzbuzz();
    void naive_fizzbuzz();
    void improved_naive_fizzbuzz();

    simple_fizzbuzz();
    printf("\n");
    naive_fizzbuzz();
    printf("\n");
    improved_naive_fizzbuzz();

    return 0;
}

void simple_fizzbuzz() {
    int i;

    for ( i = 1; i < 100; i++ ) {
        if ( ( i % 3 == 0 ) ) {
            printf("Fizz");
        }
        if ( ( i % 5 == 0) ) {
            printf("Buzz");
        }
        if ( !( i % 3 == 0 ) && !( i % 5 == 0) ) {
            printf( "%d", i);
        }
        printf(" ");
    }
}

void naive_fizzbuzz() {
    int i, mod3, mod5;

    for ( i = 1; i < 100; i++ ) {
        mod3 = ( i % 3 == 0 );
        mod5 = ( i % 5 == 0 );

        if ( mod3 ) {
            printf("Fizz");
        }
        if ( mod5 ) {
            printf("Buzz");
        }
        if ( !mod3 && !mod5 ) {
            printf("%d", i);
        }
        printf(" ");
    }
}

int divisible_by(int num, int denom) {
    return num % denom == 0;
}

void improved_naive_fizzbuzz() {

    int divisible_by(int, int);

    int i, mod3, mod5;

    for ( i = 1; i < 100; i++ ) {
        mod3 = divisible_by(i, 3);
        mod5 = divisible_by(i, 5);

        if ( mod3 ) {
            printf("Fizz");
        }
        if ( mod5 ) {
            printf("Buzz");
        }
        if ( !mod3 && !mod5 ) {
            printf("%d", i);
        }
        printf(" ");
    }
}