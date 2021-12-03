program prime_numbers
  implicit none
  integer i, j, n
  logical is_prime
  print *, "N primes"
  read *, n
  do i = 2, n
    is_prime = .true.
    do j = 2, int(sqrt(dble(i)))
      if (mod(i,j) == 0) then
        is_prime = .false.    
        exit
      end if
    end do
    if (is_prime) print *, i   
  end do
end program

