module simple_fizzbuzz_mod
  ! Reduces code reuse at the expense of overall length.
  ! Slight gain in flexibility?
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
    integer :: i

    do i=start, end
       if ( (divisible_by(i,3)) .and. divisible_by(i,5) ) then
          write(*,*) "Fizzbuzz"
       elseif ( divisible_by(i,3) ) then
          write(*,*) "Fizz"
       elseif ( divisible_by(i,5) ) then
          write(*,*) "Buzz"
       else
          write(*,'(I3)') i
       end if
    enddo

  end subroutine simple_fizzbuzz

end module simple_fizzbuzz_mod
