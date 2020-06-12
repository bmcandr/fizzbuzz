program fizzbuzz

    integer :: i
    
    i=1
    do while(i < 101)
        if ( modulo(i,3).eq.0.and.modulo(i,5).eq.0 ) then
            write(*,*) "FizzBuzz"
        elseif ( modulo(i,3).eq.0 ) then
            write(*,*) "Fizz"
        elseif ( modulo(i,5).eq.0 ) then
            write(*,*) "Buzz"
        else
            write(*,*) i
        end if
        i = i + 1
    enddo
        
end program fizzbuzz