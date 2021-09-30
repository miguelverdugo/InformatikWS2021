#include <stdio.h>
#include <stdlib.h>

/*
Struct for positional ouput
*/

struct coord {
  unsigned int x;
  unsigned int y;
  unsigned int max;
};

/*
Function for reading in the input file
*/

void get_array_from_file(unsigned int *array, char *inputfile, unsigned int width, unsigned int height)
{
    FILE* f;
    unsigned int i;

    if((f = fopen(inputfile, "r")) == NULL)
        exit(1);

    for(i=0; i<width*height; i++)
        if(fscanf(f, "%ui", &array[i]) != 1)
            exit(1);
    fclose(f);

    return;
}

/*
Function for postion determination
*/

struct coord get_position(unsigned int *array, unsigned int width, unsigned int height)
{
  unsigned int i, tmp, tmp_pos;
  struct coord output;

  tmp = array[0];
  tmp_pos = 0;

  for (i=1; i < width*height; i++)
  {
    if (array[i] > tmp)
    {
      tmp = array[i];
      tmp_pos = i;
    }
  }
  output.x = tmp_pos % width;
  output.y = tmp_pos / width;
  output.max = tmp;

  return output;
}

/*
Main function
*/

int main(void)
{
  unsigned int *image;
  char *input = "./Photometry_example.txt";
  struct coord result;
  unsigned int width = 200;
  unsigned int height = 200;

  image = malloc(width*height*sizeof(unsigned int));

  get_array_from_file(image, input, width, height);

  result = get_position(image, width, height);

  printf("%i %i %i\n", result.x, result.y, result.max);

  return 0;
}
