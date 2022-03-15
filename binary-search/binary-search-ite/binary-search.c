#include <stdio.h>
#include <stdlib.h>

#include "binary-search.h"

int binarySearch(int list[], int key, int min, int max)
{
  if (list[min] == key)
    return list[min];
  if (list[max] == key)
    return list[max];

  int index = 0;
  while (max - min != 1)
  {
    index = (min + max) / 2;
    if (list[index] == key)
      return list[index];

    if (key > list[index])
      min = index;
    else if (key < list[index])
      max = index;
  }

  return -1;
}
