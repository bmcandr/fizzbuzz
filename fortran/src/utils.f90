module utils

  implicit none
  
  private

  public :: read_range, divisible_by
  
  contains

  function read_integer() result(value)
    integer :: value, ierror

    do
       read (*, '(i10)', iostat=ierror) value

       if ( ierror == 0) then
          exit
       else
          write(*,*) 'Please enter an integer...'
       endif
    enddo

  end function read_integer
  
  subroutine read_range(start, end)
    integer, intent(out) :: start, end

    write(*,*) 'Enter an integer to start at: '
    start = read_integer()

    write(*,*) 'Enter an integer to end at: '
    end = read_integer()

  end subroutine read_range
  
  function divisible_by(num, denom)
    integer, intent(in) :: num, denom
    logical :: divisible_by

    divisible_by = .false.

    if( modulo(num, denom) .eq. 0 ) then
       divisible_by = .true.
    end if

  end function divisible_by
  
end module utils
