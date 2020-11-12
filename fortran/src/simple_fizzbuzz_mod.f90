module simple_fizzbuzz_mod
  ! Reduces code reuse at the expense of overall length.
  ! Slight gain in flexibility?
  
  use utils
  
  implicit none

  contains

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
