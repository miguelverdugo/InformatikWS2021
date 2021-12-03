PROGRAM SQUAREROOT

IMPLICIT NONE
REAL, PARAMETER :: e = 0.0001
REAL :: n, a, b, RESULT

PRINT *, 'Enter a number:'

READ *, n

IF (n < 0.0) THEN
  PRINT *, 'NOT A VALID NUMNER'
ELSE
  IF (n == 0.0) THEN
    RESULT = 0.0
  ELSE
    a = n
    b = 1.0
    DO WHILE (ABS(a - b) > e)
      a = (a + b) / 2.0
      b = n / a
    END DO
  END IF
  PRINT *, 'SQRT', n, '=', a
END IF

END PROGRAM SQUAREROOT

    
