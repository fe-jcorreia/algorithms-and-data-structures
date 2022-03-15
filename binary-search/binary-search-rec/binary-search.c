#include <stdio.h>
#include <stdlib.h>

#include "binary-search.h"

int binarySearch(int list[], int key, int min, int max)
{
  if (list[min] == key)
    return list[min];
  else if (list[max] == key)
    return list[max];
  else if (max - min == 1)
    return -1;

  int index = 0;
  index = (min + max) / 2;
  if (list[index] == key)
    return list[index];

  if (list[index] < key)
    return binarySearch(list, key, index, max);
  else if (list[index] > key)
    return binarySearch(list, key, min, index);
}
