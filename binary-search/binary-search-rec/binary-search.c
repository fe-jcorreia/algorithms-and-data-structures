#include <stdio.h>
#include <stdlib.h>

#include "binary-search.h"

int binarySearch(int list[], int key, int min, int max)
{
  if (min > max) return -1;

  int mid = (min + max) / 2;
  if (list[mid] == key)
    return list[mid];
  else if (list[mid] > key)
    return binarySearch(list, key, min, mid-1);
  else
    return binarySearch(list, key, mid+1, max);
}
