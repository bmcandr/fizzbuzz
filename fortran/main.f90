program fizzbuzz
  use simple_fizzbuzz_mod, only : simple_fizzbuzz
  integer :: start, end

  call read_range(start, end)

  !call naive_fizzbuzz()
  call simple_fizzbuzz(start, end)
  
end program fizzbuzz

subroutine read_range(start, end)
  integer, intent(out) :: start, end

  write(*,*) 'Enter an integer to start at: '
  call read_input(start)
     
  write(*,*) 'Enter an integer to end at: '
  call read_input(end)
     
end subroutine read_range

subroutine read_input(value)
  integer, intent(out) :: value
  integer :: ierror

  do
     read (*, '(i10)', iostat=ierror) value

     if ( ierror == 0) then
        exit
     else
        write(*,*) 'Please enter an integer...'
     endif
  enddo
  
end subroutine read_input

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
