#include <stdio.h>
#include <stdlib.h>

int find_maximum(int n1, int n2, int n3)
{
  int maximum;

  maximum = n1;

  if(maximum < n2)
  {
      maximum = n2;
  }
  if(maximum < n3)
  {
      maximum = n3;
  }
  return maximum;
}


int main(void)
{
  int n1, n2, n3, max;

  printf("Enter three integers:\n");
  scanf("%i %i %i", &n1, &n2, &n3);

  max = find_maximum(n1, n2, n3);

  printf("The maximum of (%i, %i, %i) is %i!\n", n1, n2, n3, max);

  return 0;
}
