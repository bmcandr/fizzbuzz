program fizzbuzz
  use utils, only: read_range
  use simple_fizzbuzz_mod, only : simple_fizzbuzz
  
  integer :: start, end

  call read_range(start, end)

  !call naive_fizzbuzz()
  call simple_fizzbuzz(start, end)
  
end program fizzbuzz

subroutine naive_fizzbuzz()
  integer :: i = 1
  
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
