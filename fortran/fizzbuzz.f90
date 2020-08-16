program fizzbuzz
  use simple_fizzbuzz_mod, only : simple_fizzbuzz
  integer, parameter :: start = 1
  integer, parameter ::  end = 101

  !call naive_fizzbuzz()
  call simple_fizzbuzz(start, end)
  
end program fizzbuzz

subroutine naive_fizzbuzz()
  integer :: i = 1
  
  print *, "Beginning Fizzbuzz from", start, "to", end, "..."
  
  do while(i < 16)
     if ( modulo(i,3).eq.0 .and. modulo(i,5).eq.0 ) then
        write(*,*) "Fizzbuzz"
     elseif ( modulo(i,3).eq.0 ) then
        write(*,*) "Fizz"
     elseif ( modulo(i,5).eq.0 ) then
        write(*,*) "Buzz"
     else
        write(*,'(I3)') i
     end if
     i = i + 1
  enddo
     
end subroutine naive_fizzbuzz

module simple_fizzbuzz_mod
  implicit none

  contains

  function divisible_by(num, denom)
    integer, intent(in) :: num, denom
    logical :: divisible_by

    divisible_by = .false.

    if( modulo(num, denom) .eq. 0 ) then
       divisible_by = .true.
    end if

  end function divisible_by

  subroutine simple_fizzbuzz(start, end)
    integer, intent(in) :: start, end
    integer :: iter

    iter = start
    print *, "Beginning Fizzbuzz from", start, "to", end, "..."

    do while(iter < end)

       if ( (divisible_by(iter,3)) .and. divisible_by(iter,5) ) then
          write(*,*) "Fizzbuzz"
       elseif ( modulo(iter,3).eq.0 ) then
          write(*,*) "Fizz"
       elseif ( modulo(iter,5).eq.0 ) then
          write(*,*) "Buzz"
       else
          write(*,'(I3)') iter
       end if
       iter = iter + 1
    enddo

  end subroutine simple_fizzbuzz

end module simple_fizzbuzz_mod
